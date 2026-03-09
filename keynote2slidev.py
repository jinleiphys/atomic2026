#!/usr/bin/env python3
"""
Keynote → Slidev / HTML Slideshow 转换工具

功能:
  1. 用 AppleScript 调用 Keynote 导出每页为 PNG
  2. 从 .key 包中提取嵌入的视频
  3. 生成 Slidev slides.md 或 HTML slideshow

用法:
  # 导出到指定目录，生成 Slidev markdown
  python keynote2slidev.py "课件.key" --output ./chapter1 --format slidev

  # 导出并生成 HTML slideshow（兼容现有格式）
  python keynote2slidev.py "课件.key" --output ./chapter1 --format html

  # 只导出资源，不生成展示文件
  python keynote2slidev.py "课件.key" --output ./chapter1 --format none

  # 从已导出的 PNG/视频目录生成 Slidev（跳过导出步骤）
  python keynote2slidev.py --from-dir ./前言 --format slidev
"""

import os
import re
import sys
import json
import shutil
import zipfile
import argparse
import subprocess
import tempfile
from pathlib import Path
from typing import List, Dict, Optional, Tuple


# ─────────────────────────── 1. Keynote 导出 ───────────────────────────

def export_keynote_slides(keynote_path: str, output_dir: str, dpi: int = 300) -> int:
    """
    用 AppleScript 调用 Keynote 将每页导出为 PNG

    Args:
        keynote_path: .key 文件的绝对路径
        output_dir: 输出目录
        dpi: 导出分辨率 (Keynote 默认 150, 推荐 300)

    Returns:
        导出的图片数量
    """
    keynote_path = os.path.abspath(keynote_path)
    output_dir = os.path.abspath(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    # 先用 Keynote 导出为图片文件夹
    # Keynote 的 AppleScript 导出会生成 Slide_XXXX.png 格式
    applescript = f'''
    tell application "Keynote"
        activate
        set theDoc to open POSIX file "{keynote_path}"
        delay 2

        -- 导出为图片
        set exportPath to POSIX file "{output_dir}"
        export theDoc as slide images to exportPath with properties {{image format:PNG, skipped slides:false}}

        delay 1
        close theDoc saving no
    end tell
    '''

    print(f"正在用 Keynote 导出幻灯片...")
    print(f"  源文件: {keynote_path}")
    print(f"  输出到: {output_dir}")

    try:
        result = subprocess.run(
            ['osascript', '-e', applescript],
            capture_output=True, text=True, timeout=120
        )
        if result.returncode != 0:
            print(f"  AppleScript 错误: {result.stderr.strip()}")
            # 尝试备选方案
            return _export_via_cli(keynote_path, output_dir)
    except subprocess.TimeoutExpired:
        print("  Keynote 导出超时，请手动导出")
        return 0
    except FileNotFoundError:
        print("  未找到 osascript，请确认在 macOS 上运行")
        return 0

    # 重命名文件: Keynote 导出的格式可能是各种命名
    # 统一重命名为 1.png, 2.png, ...
    return _rename_exported_slides(output_dir)


def _export_via_cli(keynote_path: str, output_dir: str) -> int:
    """备选导出方案：先导出为 PDF 再转 PNG"""
    print("  尝试备选方案: Keynote → PDF → PNG")

    pdf_path = os.path.join(output_dir, "_temp_export.pdf")

    applescript = f'''
    tell application "Keynote"
        activate
        set theDoc to open POSIX file "{keynote_path}"
        delay 2
        export theDoc as PDF to POSIX file "{pdf_path}" with properties {{PDF image quality:Best, skipped slides:false}}
        delay 1
        close theDoc saving no
    end tell
    '''

    try:
        result = subprocess.run(
            ['osascript', '-e', applescript],
            capture_output=True, text=True, timeout=120
        )
        if result.returncode != 0:
            print(f"  PDF 导出也失败: {result.stderr.strip()}")
            return 0
    except Exception as e:
        print(f"  PDF 导出异常: {e}")
        return 0

    if not os.path.exists(pdf_path):
        print("  PDF 文件未生成")
        return 0

    # 用 sips 将 PDF 每页转为 PNG
    print("  正在将 PDF 转换为 PNG...")
    try:
        # macOS 自带的 sips 不支持多页 PDF，用 Python 或 Quartz
        count = _pdf_to_pngs(pdf_path, output_dir)
        os.remove(pdf_path)
        return count
    except Exception as e:
        print(f"  PDF→PNG 转换失败: {e}")
        if os.path.exists(pdf_path):
            os.remove(pdf_path)
        return 0


def _pdf_to_pngs(pdf_path: str, output_dir: str) -> int:
    """用 macOS Quartz 框架将 PDF 每页转为 PNG"""
    try:
        import Quartz
        from CoreFoundation import CFURLCreateFromFileSystemRepresentation

        pdf_url = Quartz.CFURLCreateFromFileSystemRepresentation(
            None, pdf_path.encode('utf-8'), len(pdf_path.encode('utf-8')), False
        )
        pdf_doc = Quartz.CGPDFDocumentCreateWithURL(pdf_url)

        if pdf_doc is None:
            print("  无法打开 PDF")
            return 0

        page_count = Quartz.CGPDFDocumentGetNumberOfPages(pdf_doc)
        print(f"  PDF 共 {page_count} 页")

        for i in range(1, page_count + 1):
            page = Quartz.CGPDFDocumentGetPage(pdf_doc, i)
            rect = Quartz.CGPDFPageGetBoxRect(page, Quartz.kCGPDFMediaBox)

            # 2x 分辨率
            scale = 2.0
            width = int(rect.size.width * scale)
            height = int(rect.size.height * scale)

            cs = Quartz.CGColorSpaceCreateDeviceRGB()
            ctx = Quartz.CGBitmapContextCreate(
                None, width, height, 8, width * 4, cs,
                Quartz.kCGImageAlphaPremultipliedLast
            )

            # 白色背景
            Quartz.CGContextSetRGBFillColor(ctx, 1, 1, 1, 1)
            Quartz.CGContextFillRect(ctx, Quartz.CGRectMake(0, 0, width, height))

            Quartz.CGContextScaleCTM(ctx, scale, scale)
            Quartz.CGContextDrawPDFPage(ctx, page)

            image = Quartz.CGBitmapContextCreateImage(ctx)
            out_path = os.path.join(output_dir, f"{i}.png")
            out_url = Quartz.CFURLCreateFromFileSystemRepresentation(
                None, out_path.encode('utf-8'), len(out_path.encode('utf-8')), False
            )
            dest = Quartz.CGImageDestinationCreateWithURL(out_url, 'public.png', 1, None)
            Quartz.CGImageDestinationAddImage(dest, image, None)
            Quartz.CGImageDestinationFinalize(dest)

            print(f"    {i}/{page_count}: {i}.png")

        return page_count

    except ImportError:
        # Quartz 不可用，尝试用 sips（只支持单页）
        print("  Quartz 不可用，尝试用 ImageMagick 或 poppler...")
        return _pdf_to_pngs_external(pdf_path, output_dir)


def _pdf_to_pngs_external(pdf_path: str, output_dir: str) -> int:
    """用外部工具将 PDF 转 PNG"""
    # 尝试 pdftoppm (poppler)
    try:
        result = subprocess.run(
            ['pdftoppm', '-png', '-r', '300', pdf_path, os.path.join(output_dir, 'slide')],
            capture_output=True, text=True, timeout=300
        )
        if result.returncode == 0:
            return _rename_exported_slides(output_dir)
    except FileNotFoundError:
        pass

    # 尝试 ImageMagick
    try:
        result = subprocess.run(
            ['magick', pdf_path, '-density', '300', '-quality', '100',
             os.path.join(output_dir, 'slide-%03d.png')],
            capture_output=True, text=True, timeout=300
        )
        if result.returncode == 0:
            return _rename_exported_slides(output_dir)
    except FileNotFoundError:
        pass

    print("  请安装 poppler (brew install poppler) 或 ImageMagick (brew install imagemagick)")
    return 0


def _rename_exported_slides(output_dir: str) -> int:
    """
    将导出的图片统一重命名为 1.png, 2.png, ...
    支持 Keynote 导出的各种命名格式
    """
    dir_path = Path(output_dir)

    # 已经是数字命名的不处理
    existing = list(dir_path.glob('[0-9]*.png'))
    numeric_pattern = re.compile(r'^(\d+)\.png$')
    already_numbered = [f for f in existing if numeric_pattern.match(f.name)]
    if already_numbered:
        return len(already_numbered)

    # 收集所有 PNG，按名称排序
    all_pngs = sorted(dir_path.glob('*.png'))
    # 排除临时文件
    all_pngs = [f for f in all_pngs if not f.name.startswith('_')]

    if not all_pngs:
        return 0

    # 尝试按文件名中的数字排序
    def extract_number(path):
        nums = re.findall(r'\d+', path.stem)
        return int(nums[-1]) if nums else 0

    all_pngs.sort(key=extract_number)

    # 重命名
    for i, png in enumerate(all_pngs, 1):
        new_name = dir_path / f"{i}.png"
        if png != new_name:
            # 避免覆盖
            if new_name.exists():
                temp = dir_path / f"_temp_{i}.png"
                png.rename(temp)
            else:
                png.rename(new_name)
            print(f"  重命名: {png.name} → {i}.png")

    # 处理临时文件
    for temp in dir_path.glob('_temp_*.png'):
        num = re.search(r'_temp_(\d+)', temp.name).group(1)
        temp.rename(dir_path / f"{num}.png")

    return len(all_pngs)


# ─────────────────────────── 2. 视频提取 ───────────────────────────

def extract_videos(keynote_path: str, output_dir: str) -> Dict[str, str]:
    """
    从 .key 包中提取视频文件

    .key 文件本质是一个 zip 包，视频存储在 Data/ 目录下

    Returns:
        {文件名: 输出路径} 的字典
    """
    keynote_path = os.path.abspath(keynote_path)
    output_dir = os.path.abspath(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    videos = {}
    video_extensions = {'.mp4', '.mov', '.m4v', '.avi', '.webm'}

    print(f"\n正在从 Keynote 包中提取视频...")

    try:
        with zipfile.ZipFile(keynote_path, 'r') as zf:
            video_files = [
                name for name in zf.namelist()
                if Path(name).suffix.lower() in video_extensions
            ]

            if not video_files:
                print("  未找到嵌入的视频文件")
                return videos

            print(f"  找到 {len(video_files)} 个视频文件")

            for i, vf in enumerate(video_files, 1):
                # 提取文件名
                original_name = Path(vf).name
                # 生成简洁的文件名
                ext = Path(vf).suffix.lower()
                out_name = f"video_{i}{ext}" if len(video_files) > 1 else f"video{ext}"
                out_path = os.path.join(output_dir, out_name)

                # 提取
                with zf.open(vf) as src, open(out_path, 'wb') as dst:
                    shutil.copyfileobj(src, dst)

                size_mb = os.path.getsize(out_path) / (1024 * 1024)
                print(f"  提取: {original_name} → {out_name} ({size_mb:.1f} MB)")
                videos[out_name] = out_path

    except zipfile.BadZipFile:
        # .key 可能是目录格式（旧版 Keynote）
        print("  .key 文件不是 zip 格式，尝试目录方式...")
        if os.path.isdir(keynote_path):
            for root, dirs, files in os.walk(keynote_path):
                for f in files:
                    if Path(f).suffix.lower() in video_extensions:
                        src = os.path.join(root, f)
                        dst = os.path.join(output_dir, f)
                        shutil.copy2(src, dst)
                        size_mb = os.path.getsize(dst) / (1024 * 1024)
                        print(f"  复制: {f} ({size_mb:.1f} MB)")
                        videos[f] = dst
    except Exception as e:
        print(f"  提取视频出错: {e}")

    return videos


# ─────────────────────────── 3. 扫描已有资源 ───────────────────────────

def scan_existing_dir(directory: str) -> Tuple[List[str], Dict[str, str]]:
    """
    扫描目录中已有的 PNG 图片和视频

    Returns:
        (slides_list, videos_dict)
    """
    dir_path = Path(directory)
    png_pattern = re.compile(r'^(\d+)\.png$')
    mp4_pattern = re.compile(r'^(\d+)\.mp4$')

    slides = []
    videos = {}

    for f in sorted(dir_path.iterdir()):
        if f.is_file():
            match = png_pattern.match(f.name)
            if match:
                slides.append(f.name)

            match = mp4_pattern.match(f.name)
            if match:
                num = match.group(1)
                videos[num] = f.name

    # 按数字排序
    slides.sort(key=lambda x: int(re.search(r'\d+', x).group()))

    return slides, videos


# ─────────────────────────── 4. 生成 Slidev ───────────────────────────

def generate_slidev(slides: List[str], videos: Dict[str, str],
                    output_dir: str, title: str = "课程演示",
                    chapter_name: str = "") -> str:
    """
    生成 Slidev 的 slides.md 文件

    Args:
        slides: 幻灯片图片文件名列表 ['1.png', '2.png', ...]
        videos: 视频映射 {'1': '1.mp4', ...}
        output_dir: 输出目录
        title: 演示标题
        chapter_name: 章节名称

    Returns:
        生成的 slides.md 路径
    """
    output_dir = os.path.abspath(output_dir)

    # 创建 Slidev 项目结构
    slidev_dir = os.path.join(output_dir, 'slidev')
    public_dir = os.path.join(slidev_dir, 'public')
    images_dir = os.path.join(public_dir, 'images')
    videos_dir = os.path.join(public_dir, 'videos')

    os.makedirs(images_dir, exist_ok=True)
    os.makedirs(videos_dir, exist_ok=True)

    # 复制/链接图片和视频到 public 目录
    for slide in slides:
        src = os.path.join(output_dir, slide)
        dst = os.path.join(images_dir, slide)
        if os.path.exists(src) and not os.path.exists(dst):
            # 使用符号链接节省空间
            os.symlink(src, dst)

    for key, video_file in videos.items():
        src = os.path.join(output_dir, video_file)
        dst = os.path.join(videos_dir, video_file)
        if os.path.exists(src) and not os.path.exists(dst):
            os.symlink(src, dst)

    # 生成 slides.md
    md_lines = []

    # Frontmatter
    md_lines.append('---')
    md_lines.append(f'title: "{title}"')
    md_lines.append('theme: none')
    md_lines.append('class: text-center')
    md_lines.append('highlighter: shiki')
    md_lines.append('drawings:')
    md_lines.append('  persist: false')
    md_lines.append('transition: fade-out')
    md_lines.append('mdc: true')
    md_lines.append('---')
    md_lines.append('')

    for i, slide in enumerate(slides):
        slide_num = str(i + 1)

        if i > 0:
            # 幻灯片分隔符
            md_lines.append('---')
            md_lines.append('')

        # 每页用全屏背景图
        md_lines.append(f'<div class="slide-container">')
        md_lines.append(f'  <img src="/images/{slide}" class="slide-bg" />')

        # 如果该页有视频
        if slide_num in videos:
            video_file = videos[slide_num]
            md_lines.append(f'  <div class="video-overlay">')
            md_lines.append(f'    <video controls class="slide-video">')
            md_lines.append(f'      <source src="/videos/{video_file}" type="video/mp4" />')
            md_lines.append(f'    </video>')
            md_lines.append(f'  </div>')

        md_lines.append(f'</div>')
        md_lines.append('')

    slides_md = '\n'.join(md_lines)

    # 写入 slides.md
    md_path = os.path.join(slidev_dir, 'slides.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(slides_md)

    # 生成 package.json
    pkg = {
        "name": chapter_name or "slidev-presentation",
        "private": True,
        "scripts": {
            "dev": "slidev",
            "build": "slidev build",
            "export": "slidev export"
        },
        "dependencies": {
            "@slidev/cli": "latest",
            "@slidev/theme-default": "latest"
        }
    }
    pkg_path = os.path.join(slidev_dir, 'package.json')
    with open(pkg_path, 'w', encoding='utf-8') as f:
        json.dump(pkg, f, indent=2, ensure_ascii=False)

    # 生成自定义样式 (全屏图片)
    style_dir = os.path.join(slidev_dir, 'styles')
    os.makedirs(style_dir, exist_ok=True)

    style_css = '''\
/* 全屏幻灯片图片样式 */
.slidev-layout {
  padding: 0 !important;
  overflow: hidden;
}

.slide-container {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #000;
}

.slide-bg {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.video-overlay {
  position: absolute;
  bottom: 20px;
  right: 20px;
  z-index: 10;
}

.slide-video {
  max-width: 320px;
  border-radius: 8px;
  box-shadow: 0 4px 24px rgba(0,0,0,0.5);
}

/* 点击视频按钮样式 */
.video-trigger {
  position: absolute;
  bottom: 20px;
  right: 20px;
  background: rgba(0,0,0,0.6);
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 20px;
  cursor: pointer;
  font-size: 14px;
  backdrop-filter: blur(10px);
  z-index: 10;
}

.video-trigger:hover {
  background: rgba(0,0,0,0.8);
}
'''
    with open(os.path.join(style_dir, 'index.css'), 'w') as f:
        f.write(style_css)

    print(f"\nSlidev 项目已生成: {slidev_dir}")
    print(f"  slides.md: {len(slides)} 页")
    print(f"  视频: {len(videos)} 个")
    print(f"\n使用方法:")
    print(f"  cd {slidev_dir}")
    print(f"  npm install")
    print(f"  npm run dev")

    return md_path


# ─────────────────────── 5. 生成 HTML Slideshow ───────────────────────

def generate_html_slideshow(slides: List[str], videos: Dict[str, str],
                            output_dir: str, title: str = "幻灯片播放器") -> str:
    """
    生成 HTML 幻灯片播放器（兼容现有格式）
    使用现有的 generate_slideshow.py 的逻辑
    """
    output_dir = os.path.abspath(output_dir)

    # 检查是否已有 generate_slideshow.py
    gen_script = os.path.join(output_dir, 'generate_slideshow.py')
    if os.path.exists(gen_script):
        print(f"\n运行现有生成脚本: {gen_script}")
        result = subprocess.run(
            [sys.executable, gen_script, '--dir', output_dir, '--title', title],
            capture_output=True, text=True
        )
        print(result.stdout)
        if result.returncode != 0:
            print(f"错误: {result.stderr}")
        return os.path.join(output_dir, 'slideshow.html')

    # 否则生成简单版本
    slides_json = json.dumps(slides, ensure_ascii=False)
    videos_json = json.dumps(videos, ensure_ascii=False)

    html_path = os.path.join(output_dir, 'slideshow.html')
    # 复制前言目录的生成逻辑
    print(f"\n请将 generate_slideshow.py 复制到 {output_dir} 并运行")
    return html_path


# ─────────────────────── 6. 批量处理 ───────────────────────

def batch_convert(keynote_dir: str, output_base: str, fmt: str = 'slidev'):
    """
    批量转换目录下所有 .key 文件

    Args:
        keynote_dir: 包含 .key 文件的目录
        output_base: 输出基础目录
        fmt: 输出格式 (slidev/html/none)
    """
    keynote_dir = os.path.abspath(keynote_dir)
    output_base = os.path.abspath(output_base)

    key_files = sorted(Path(keynote_dir).glob('*.key'))
    if not key_files:
        print(f"在 {keynote_dir} 中未找到 .key 文件")
        return

    print(f"找到 {len(key_files)} 个 Keynote 文件:")
    for kf in key_files:
        print(f"  - {kf.name}")

    print()

    for kf in key_files:
        chapter_name = kf.stem.replace(' ', '_')
        output_dir = os.path.join(output_base, chapter_name)

        print(f"{'='*60}")
        print(f"处理: {kf.name}")
        print(f"输出: {output_dir}")
        print(f"{'='*60}")

        # 1. 导出幻灯片
        count = export_keynote_slides(str(kf), output_dir)
        print(f"  导出了 {count} 张幻灯片")

        # 2. 提取视频
        videos_found = extract_videos(str(kf), output_dir)

        # 3. 扫描结果
        slides, videos = scan_existing_dir(output_dir)

        # 4. 生成展示文件
        if fmt == 'slidev' and slides:
            generate_slidev(slides, videos, output_dir,
                           title=kf.stem, chapter_name=chapter_name)
        elif fmt == 'html' and slides:
            generate_html_slideshow(slides, videos, output_dir, title=kf.stem)

        print()


# ─────────────────────── 主程序 ───────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='Keynote → Slidev/HTML 转换工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例:
  # 单个文件转换
  python keynote2slidev.py "atomic physics_chapter 0.key" -o ./ch0 -f slidev

  # 批量转换目录下所有 .key
  python keynote2slidev.py --batch ~/Desktop/课件/南开/ -o ./chapters -f slidev

  # 从已有 PNG 目录生成 Slidev
  python keynote2slidev.py --from-dir ./前言 -f slidev -t "原子物理学前言"

  # 只提取资源不生成展示文件
  python keynote2slidev.py "课件.key" -o ./output -f none
        '''
    )

    parser.add_argument('keynote_file', nargs='?', help='.key 文件路径')
    parser.add_argument('-o', '--output', default='.', help='输出目录 (默认: 当前目录)')
    parser.add_argument('-f', '--format', choices=['slidev', 'html', 'none'],
                       default='slidev', help='输出格式 (默认: slidev)')
    parser.add_argument('-t', '--title', default='课程演示', help='演示标题')
    parser.add_argument('--from-dir', help='从已有的 PNG/视频目录生成（跳过导出步骤）')
    parser.add_argument('--batch', help='批量处理目录下所有 .key 文件')
    parser.add_argument('--dpi', type=int, default=300, help='导出分辨率 (默认: 300)')

    args = parser.parse_args()

    # 批量模式
    if args.batch:
        batch_convert(args.batch, args.output, args.format)
        return 0

    # 从已有目录生成
    if args.from_dir:
        from_dir = os.path.abspath(args.from_dir)
        if not os.path.isdir(from_dir):
            print(f"目录不存在: {from_dir}")
            return 1

        slides, videos = scan_existing_dir(from_dir)
        if not slides:
            print(f"在 {from_dir} 中未找到幻灯片图片 (1.png, 2.png, ...)")
            return 1

        print(f"扫描到 {len(slides)} 张幻灯片, {len(videos)} 个视频")

        if args.format == 'slidev':
            generate_slidev(slides, videos, from_dir, args.title)
        elif args.format == 'html':
            generate_html_slideshow(slides, videos, from_dir, args.title)
        return 0

    # 单文件模式
    if not args.keynote_file:
        parser.print_help()
        return 1

    keynote_path = os.path.abspath(args.keynote_file)
    if not os.path.exists(keynote_path):
        print(f"文件不存在: {keynote_path}")
        return 1

    output_dir = os.path.abspath(args.output)

    # 1. 导出
    count = export_keynote_slides(keynote_path, output_dir, args.dpi)
    if count == 0:
        print("\n导出失败。你也可以手动从 Keynote 导出图片后，使用 --from-dir 选项:")
        print(f'  python keynote2slidev.py --from-dir {output_dir} -f {args.format}')
        return 1

    # 2. 提取视频
    extract_videos(keynote_path, output_dir)

    # 3. 扫描
    slides, videos = scan_existing_dir(output_dir)

    # 4. 生成
    if args.format == 'slidev':
        generate_slidev(slides, videos, output_dir, args.title)
    elif args.format == 'html':
        generate_html_slideshow(slides, videos, output_dir, args.title)
    else:
        print(f"\n资源导出完成: {output_dir}")
        print(f"  {len(slides)} 张幻灯片, {len(videos)} 个视频")

    return 0


if __name__ == '__main__':
    sys.exit(main())
