#!/usr/bin/env python3
"""
Keynote → Slidev 可编辑 Markdown 转换工具

从 .key 文件中提取结构化文本、LaTeX 公式、图片和视频，
生成可编辑的 Slidev slides.md 文件。

用法:
  python key2slidev.py "原子物理第二章.key" -o ./第二章 -t "原子的量子态：玻尔模型"
"""

import os
import re
import sys
import json
import shutil
import zipfile
import argparse
from pathlib import Path
from typing import List, Dict, Tuple, Optional

from keynote_parser.file_utils import IWAFile
import yaml


EQUATION_SOURCE_KEY = '[TSWP.EquationInfoArchive.equation_source_text]'
OBJ_REPLACEMENT = '￼'  # U+FFFC - object replacement character


# ─────────────── 工具函数 ───────────────

def clean_text(text: str) -> str:
    """清理文本，去除特殊字符"""
    text = text.replace(OBJ_REPLACEMENT, '')
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def build_id_to_filename_map(zf: zipfile.ZipFile) -> Dict[str, str]:
    """
    建立 Data identifier -> 文件名 的映射
    Keynote Data/ 文件名格式: name-{id}.ext 或 name-small-{id}.ext
    """
    id_map = {}
    for name in zf.namelist():
        if not name.startswith('Data/'):
            continue
        fname = os.path.basename(name)
        # 提取文件名中最后的数字 ID (在扩展名之前)
        match = re.search(r'-(\d+)\.[^.]+$', fname)
        if match:
            fid = match.group(1)
            ext = Path(fname).suffix.lower()
            # 优先保留非 small 版本
            if fid not in id_map or 'small' not in fname.lower():
                id_map[fid] = fname
    return id_map


# ─────────────── 1. 解析 Keynote 文件 ───────────────

def parse_keynote(key_path: str) -> Tuple[List[Dict], Dict[str, str]]:
    """
    解析 .key 文件，按顺序提取每页幻灯片的文本、公式、图片和视频

    Returns:
        (slides, id_to_filename)
    """
    key_path = os.path.abspath(key_path)

    with zipfile.ZipFile(key_path, 'r') as zf:
        # 建立 ID -> 文件名映射
        id_to_fname = build_id_to_filename_map(zf)

        # 获取幻灯片顺序
        slide_order = _get_slide_order(zf)
        print(f"  幻灯片顺序: {len(slide_order)} 页")

        # 建立 slide id -> 文件名映射
        slide_files = [
            n for n in zf.namelist()
            if re.match(r'Index/Slide(-\d+)?\.iwa$', n)
        ]
        slide_map = {}
        for sf in slide_files:
            data = zf.read(sf)
            iwa = IWAFile.from_buffer(data)
            d = iwa.to_dict()
            for chunk in d.get('chunks', []):
                for archive in chunk.get('archives', []):
                    sid = archive.get('header', {}).get('identifier', '')
                    for obj in archive.get('objects', []):
                        if obj.get('_pbtype') == 'KN.SlideArchive':
                            slide_map[sid] = sf

        # 按顺序提取每页内容
        slides = []
        for sid in slide_order:
            if sid not in slide_map:
                continue
            sf = slide_map[sid]
            data = zf.read(sf)
            iwa = IWAFile.from_buffer(data)
            d = iwa.to_dict()
            slide_data = _extract_slide_content(d, id_to_fname)
            slides.append(slide_data)

    return slides, id_to_fname


def _get_slide_order(zf: zipfile.ZipFile) -> List[str]:
    """从 Document.iwa 获取幻灯片的 identifier 顺序"""
    data = zf.read('Index/Document.iwa')
    iwa = IWAFile.from_buffer(data)
    d = iwa.to_dict()

    slide_ids = []

    def find_slide_nodes(obj):
        if isinstance(obj, dict):
            pbtype = obj.get('_pbtype', '')
            if pbtype == 'KN.SlideNodeArchive':
                slide_ref = obj.get('slide', {})
                if isinstance(slide_ref, dict) and 'identifier' in slide_ref:
                    slide_ids.append(slide_ref['identifier'])
                for child in obj.get('children', []):
                    find_slide_nodes(child)
            for v in obj.values():
                find_slide_nodes(v)
        elif isinstance(obj, list):
            for item in obj:
                find_slide_nodes(item)

    find_slide_nodes(d)

    if not slide_ids:
        doc_yaml = yaml.dump(d, allow_unicode=True, default_flow_style=False)
        all_ids = re.findall(r"identifier: '(\d+)'", doc_yaml)
        return all_ids

    return slide_ids


def _extract_slide_content(iwa_dict: dict, id_to_fname: Dict[str, str]) -> Dict:
    """从单个 slide 的 IWA 字典中提取标题、正文、公式、图片、视频"""
    result = {
        'title': '',
        'body_parts': [],
        'images': [],      # [(filename, width, height)]
        'videos': [],      # [(filename, width, height)]
    }

    chunks = iwa_dict.get('chunks', [])

    # 第一遍：收集公式
    all_equations = []
    for chunk in chunks:
        for archive in chunk.get('archives', []):
            for obj in archive.get('objects', []):
                if EQUATION_SOURCE_KEY in obj:
                    latex = obj[EQUATION_SOURCE_KEY]
                    if isinstance(latex, str):
                        all_equations.append(latex.strip())

    # 第二遍：收集图片和视频引用
    for chunk in chunks:
        for archive in chunk.get('archives', []):
            for obj in archive.get('objects', []):
                pbtype = obj.get('_pbtype', '')

                if pbtype == 'TSD.ImageArchive':
                    data_ref = obj.get('data', {})
                    if isinstance(data_ref, dict):
                        img_id = data_ref.get('identifier', '')
                        if img_id and img_id in id_to_fname:
                            fname = id_to_fname[img_id]
                            ns = obj.get('naturalSize', {})
                            w = ns.get('width', 0)
                            h = ns.get('height', 0)
                            # 排除 0 尺寸的（公式图片等）
                            if w > 0 and h > 0:
                                result['images'].append((fname, w, h))

                elif pbtype == 'TSD.MovieArchive':
                    movie_ref = obj.get('movieData', {})
                    if isinstance(movie_ref, dict):
                        mov_id = movie_ref.get('identifier', '')
                        if mov_id and mov_id in id_to_fname:
                            fname = id_to_fname[mov_id]
                            ns = obj.get('naturalSize', {})
                            w = ns.get('width', 0)
                            h = ns.get('height', 0)
                            result['videos'].append((fname, w, h))

    # 第三遍：收集 StorageArchive 文本
    storage_texts = {}
    for chunk in chunks:
        for archive in chunk.get('archives', []):
            aid = archive.get('header', {}).get('identifier', '')
            for obj in archive.get('objects', []):
                if obj.get('_pbtype') == 'TSWP.StorageArchive' and 'text' in obj:
                    raw_texts = obj['text']
                    combined = '\n'.join(
                        t for t in raw_texts if isinstance(t, str)
                    ).strip()
                    if combined:
                        storage_texts[aid] = combined

    # 公式替换
    eq_idx = 0

    def replace_equations(text: str) -> str:
        nonlocal eq_idx
        parts = []
        for char in text:
            if char == OBJ_REPLACEMENT and eq_idx < len(all_equations):
                parts.append(f' ${all_equations[eq_idx]}$ ')
                eq_idx += 1
            else:
                parts.append(char)
        return ''.join(parts)

    # 第四遍：placeholder 信息
    title_storage_ids = []
    body_storage_ids = []

    for chunk in chunks:
        for archive in chunk.get('archives', []):
            for obj in archive.get('objects', []):
                if obj.get('_pbtype') == 'KN.PlaceholderArchive':
                    kind = obj.get('kind', '')
                    storage_id = _get_storage_id(obj)
                    if storage_id and storage_id in storage_texts:
                        if kind == 'kKindTitlePlaceholder':
                            title_storage_ids.append(storage_id)
                        elif kind == 'kKindBodyPlaceholder':
                            body_storage_ids.append(storage_id)

    # 收集所有 storage IDs（按出现顺序）
    all_storage_ids_ordered = []
    seen = set()
    for chunk in chunks:
        for archive in chunk.get('archives', []):
            aid = archive.get('header', {}).get('identifier', '')
            if aid in storage_texts and aid not in seen:
                seen.add(aid)
                all_storage_ids_ordered.append(aid)

    # 按顺序处理文本（公式替换）
    eq_idx = 0
    processed = {}
    for sid in all_storage_ids_ordered:
        processed[sid] = replace_equations(storage_texts[sid])

    # 组装
    if title_storage_ids:
        result['title'] = processed.get(title_storage_ids[0], '')
    elif all_storage_ids_ordered:
        result['title'] = processed.get(all_storage_ids_ordered[0], '')
        all_storage_ids_ordered = all_storage_ids_ordered[1:]

    if body_storage_ids:
        result['body_parts'] = [
            processed[sid] for sid in body_storage_ids if sid in processed
        ]
    else:
        title_sids = set(title_storage_ids)
        result['body_parts'] = [
            processed[sid] for sid in all_storage_ids_ordered
            if sid in processed and sid not in title_sids
        ]

    # 去重
    if result['title']:
        tc = clean_text(result['title'])
        result['body_parts'] = [p for p in result['body_parts'] if clean_text(p) != tc]

    result['body_parts'] = [p for p in result['body_parts'] if clean_text(p)]

    return result


def _get_storage_id(placeholder_obj: dict) -> Optional[str]:
    super_obj = placeholder_obj.get('super', {})
    for key in ('ownedStorage', 'deprecatedStorage'):
        storage = super_obj.get(key, {})
        if isinstance(storage, dict) and 'identifier' in storage:
            return storage['identifier']
    return None


# ─────────────── 2. 提取媒体资源 ───────────────

def extract_media(key_path: str, output_dir: str) -> Dict[str, str]:
    """从 .key 包中提取图片和视频到输出目录，返回 filename -> url 映射"""
    media_dir = os.path.join(output_dir, 'public', 'images')
    os.makedirs(media_dir, exist_ok=True)

    media = {}
    with zipfile.ZipFile(key_path, 'r') as zf:
        for name in zf.namelist():
            if name.startswith('Data/'):
                fname = os.path.basename(name)
                ext = Path(fname).suffix.lower()
                if ext in ('.png', '.jpg', '.jpeg', '.gif', '.svg',
                           '.mp4', '.mov', '.m4v'):
                    out_path = os.path.join(media_dir, fname)
                    if not os.path.exists(out_path):
                        with zf.open(name) as src, open(out_path, 'wb') as dst:
                            shutil.copyfileobj(src, dst)
                    media[fname] = f'/images/{fname}'

    print(f"  提取了 {len(media)} 个媒体文件")
    return media


# ─────────────── 3. 生成 Slidev Markdown ───────────────

def generate_slidev_md(slides: List[Dict], title: str = "课程演示",
                       output_dir: str = ".") -> str:
    """生成 Slidev slides.md，包含文本、公式、图片和视频"""
    os.makedirs(output_dir, exist_ok=True)

    lines = []

    # Frontmatter
    lines.append('---')
    lines.append(f'title: "{title}"')
    lines.append('theme: default')
    lines.append('highlighter: shiki')
    lines.append('drawings:')
    lines.append('  persist: false')
    lines.append('transition: slide-left')
    lines.append('mdc: true')
    lines.append('math: katex')
    lines.append('---')
    lines.append('')

    for i, slide in enumerate(slides):
        if i > 0:
            lines.append('---')
            lines.append('')

        slide_title = clean_text(slide.get('title', ''))
        body_parts = slide.get('body_parts', [])
        images = slide.get('images', [])
        videos = slide.get('videos', [])

        # 标题
        if slide_title:
            lines.append(f'# {slide_title}')
            lines.append('')

        # 正文
        for part in body_parts:
            text = part.strip()
            if not text or text == OBJ_REPLACEMENT:
                continue
            paragraphs = text.split('\n')
            for p in paragraphs:
                p = p.strip()
                if not p:
                    lines.append('')
                    continue
                lines.append(p)
                lines.append('')

        # 图片
        if images:
            for fname, w, h in images:
                # 限制最大宽度
                display_w = min(int(w), 500)
                lines.append(f'<img src="/images/{fname}" style="max-width: {display_w}px; max-height: 400px;" />')
                lines.append('')

        # 视频
        if videos:
            for fname, w, h in videos:
                display_w = min(int(w), 500)
                lines.append(f'<video controls style="max-width: {display_w}px;">')
                lines.append(f'  <source src="/images/{fname}" />')
                lines.append(f'</video>')
                lines.append('')

        # 空页占位
        if not slide_title and not body_parts and not images and not videos:
            lines.append('<!-- 此页内容待补充 -->')
            lines.append('')

    md_content = '\n'.join(lines)

    md_path = os.path.join(output_dir, 'slides.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)

    # 统计
    img_count = sum(len(s.get('images', [])) for s in slides)
    vid_count = sum(len(s.get('videos', [])) for s in slides)
    print(f"\n生成 slides.md: {len(slides)} 页, {img_count} 张图片, {vid_count} 个视频")
    print(f"  路径: {md_path}")

    return md_path


# ─────────────── 4. 生成 package.json ───────────────

def generate_package_json(output_dir: str, name: str = "slidev-presentation"):
    pkg = {
        "name": name,
        "private": True,
        "scripts": {
            "dev": "slidev",
            "build": "slidev build",
            "export": "slidev export"
        },
        "dependencies": {
            "@slidev/cli": "latest",
            "katex": "latest"
        }
    }
    pkg_path = os.path.join(output_dir, 'package.json')
    with open(pkg_path, 'w', encoding='utf-8') as f:
        json.dump(pkg, f, indent=2, ensure_ascii=False)


# ─────────────── 主程序 ───────────────

def main():
    parser = argparse.ArgumentParser(
        description='Keynote → Slidev 可编辑 Markdown 转换工具'
    )
    parser.add_argument('keynote_file', help='.key 文件路径')
    parser.add_argument('-o', '--output', default='.', help='输出目录')
    parser.add_argument('-t', '--title', default='课程演示', help='演示标题')

    args = parser.parse_args()

    key_path = os.path.abspath(args.keynote_file)
    if not os.path.exists(key_path):
        print(f"文件不存在: {key_path}")
        return 1

    output_dir = os.path.abspath(args.output)
    os.makedirs(output_dir, exist_ok=True)

    print(f"解析 Keynote 文件: {key_path}")

    # 1. 解析幻灯片内容
    slides, _ = parse_keynote(key_path)
    print(f"  共解析 {len(slides)} 页幻灯片")

    # 2. 提取媒体资源
    extract_media(key_path, output_dir)

    # 3. 生成 Slidev markdown
    generate_slidev_md(slides, args.title, output_dir)

    # 4. 生成 package.json
    generate_package_json(output_dir)

    print(f"\n完成！使用方法:")
    print(f"  cd {output_dir}")
    print(f"  npm install && npm run dev")

    return 0


if __name__ == '__main__':
    sys.exit(main())
