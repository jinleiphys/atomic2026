#!/usr/bin/env python3
"""
交互式幻灯片播放器生成器
扫描目录中的PNG图片和视频，生成可点击翻页的HTML播放器
"""

import os
import re
import json
import argparse
from pathlib import Path
from typing import List, Dict, Optional


def scan_slides(directory: str) -> Dict:
    """
    扫描目录中的幻灯片文件

    Args:
        directory: 目录路径

    Returns:
        包含slides和videos信息的字典
    """
    dir_path = Path(directory)

    # 扫描PNG图片 (数字命名: 1.png, 2.png, ...)
    png_pattern = re.compile(r'^(\d+)\.png$')
    slides = []

    for f in dir_path.iterdir():
        if f.is_file():
            match = png_pattern.match(f.name)
            if match:
                num = int(match.group(1))
                slides.append({
                    'num': num,
                    'filename': f.name,
                    'path': str(f.relative_to(dir_path))
                })

    # 按数字排序
    slides.sort(key=lambda x: x['num'])

    # 扫描视频文件
    videos = {}

    # 检查其他可能的视频 (格式: N.mp4 或 N-M.mp4 过渡视频)
    mp4_pattern = re.compile(r'^(\d+)\.mp4$')
    transition_pattern = re.compile(r'^(\d+)-(\d+)\.mp4$')

    for f in dir_path.iterdir():
        if f.is_file() and f.suffix.lower() == '.mp4':
            # 单页视频
            match = mp4_pattern.match(f.name)
            if match:
                num = match.group(1)
                videos[num] = f.name

            # 过渡视频
            match = transition_pattern.match(f.name)
            if match:
                key = f"{match.group(1)}-{match.group(2)}"
                videos[key] = f.name

    return {
        'slides': slides,
        'videos': videos,
        'total': len(slides)
    }


def generate_html(data: Dict, output_path: str, title: str = "幻灯片播放器"):
    """
    生成HTML播放器

    Args:
        data: 扫描得到的数据
        output_path: 输出HTML文件路径
        title: 页面标题
    """
    slides_json = json.dumps([s['path'] for s in data['slides']], ensure_ascii=False)
    videos_json = json.dumps(data['videos'], ensure_ascii=False)

    html_content = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            overflow: hidden;
            background: #1a1a2e;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        }}

        .container {{
            width: 100vw;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
        }}

        /* 幻灯片图片 */
        .slide-image {{
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
            display: none;
            cursor: pointer;
        }}

        .slide-image.active {{
            display: block;
        }}

        /* 视频播放器 - 全屏拉伸 */
        .video-player {{
            width: 100%;
            height: 100%;
            object-fit: fill;
            display: none;
            cursor: pointer;
        }}

        .video-player.active {{
            display: block;
        }}

        /* 页码指示器 */
        .indicator {{
            position: fixed;
            top: 20px;
            right: 20px;
            background: rgba(0, 0, 0, 0.7);
            padding: 12px 24px;
            border-radius: 25px;
            color: white;
            font-size: 16px;
            font-weight: 500;
            z-index: 100;
            backdrop-filter: blur(10px);
            user-select: none;
        }}

        /* 导航按钮 */
        .nav-btn {{
            position: fixed;
            top: 50%;
            transform: translateY(-50%);
            background: rgba(0, 0, 0, 0.5);
            border: none;
            color: white;
            font-size: 32px;
            padding: 20px 15px;
            cursor: pointer;
            z-index: 100;
            transition: all 0.3s;
            opacity: 0;
            border-radius: 8px;
        }}

        .nav-btn:hover {{
            background: rgba(0, 0, 0, 0.8);
        }}

        .container:hover .nav-btn {{
            opacity: 1;
        }}

        .nav-btn.prev {{
            left: 20px;
        }}

        .nav-btn.next {{
            right: 20px;
        }}

        .nav-btn:disabled {{
            opacity: 0.3;
            cursor: not-allowed;
        }}

        /* 控制提示 */
        .controls {{
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0, 0, 0, 0.7);
            padding: 12px 24px;
            border-radius: 25px;
            color: white;
            font-size: 14px;
            z-index: 100;
            backdrop-filter: blur(10px);
            opacity: 1;
            transition: opacity 0.3s;
            user-select: none;
        }}

        .controls.hidden {{
            opacity: 0;
            pointer-events: none;
        }}

        .controls span {{
            margin: 0 10px;
            color: #888;
        }}

        /* 进度条 */
        .progress-bar {{
            position: fixed;
            bottom: 0;
            left: 0;
            height: 4px;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            transition: width 0.3s;
            z-index: 100;
        }}

        /* 缩略图导航 */
        .thumbnail-nav {{
            position: fixed;
            bottom: 70px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0, 0, 0, 0.8);
            padding: 10px;
            border-radius: 10px;
            display: none;
            gap: 8px;
            max-width: 90vw;
            overflow-x: auto;
            z-index: 100;
        }}

        .thumbnail-nav.visible {{
            display: flex;
        }}

        .thumbnail {{
            width: 80px;
            height: 45px;
            object-fit: cover;
            cursor: pointer;
            border: 2px solid transparent;
            border-radius: 4px;
            opacity: 0.6;
            transition: all 0.2s;
        }}

        .thumbnail:hover {{
            opacity: 1;
        }}

        .thumbnail.active {{
            border-color: #667eea;
            opacity: 1;
        }}

        /* 视频图标标记 */
        .has-video::after {{
            content: "▶";
            position: absolute;
            bottom: 2px;
            right: 2px;
            font-size: 10px;
            color: #667eea;
        }}

        /* 加载指示 */
        .loading {{
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: white;
            font-size: 18px;
            z-index: 200;
            display: none;
        }}

        .loading.active {{
            display: block;
        }}

        .loading::after {{
            content: '';
            display: inline-block;
            width: 20px;
            height: 20px;
            margin-left: 10px;
            border: 2px solid #fff;
            border-radius: 50%;
            border-top-color: transparent;
            animation: spin 1s linear infinite;
        }}

        @keyframes spin {{
            to {{ transform: rotate(360deg); }}
        }}
    </style>
</head>
<body>
    <div class="container" id="container">
        <!-- 内容通过JS动态生成 -->
    </div>

    <button class="nav-btn prev" id="prevBtn">&#10094;</button>
    <button class="nav-btn next" id="nextBtn">&#10095;</button>

    <div class="indicator">
        <span id="current">1</span> / <span id="total">{data['total']}</span>
    </div>


    <div class="progress-bar" id="progress"></div>

    <div class="thumbnail-nav" id="thumbnails">
        <!-- 缩略图通过JS生成 -->
    </div>

    <div class="loading" id="loading">加载中</div>

    <script>
        // 数据
        const slidesData = {slides_json};
        const videosData = {videos_json};

        class SlideShowPlayer {{
            constructor() {{
                this.slides = slidesData;
                this.videos = videosData;
                this.currentSlide = 0;
                this.isVideoPlaying = false;
                this.showThumbnails = false;

                this.container = document.getElementById('container');
                this.currentIndicator = document.getElementById('current');
                this.totalIndicator = document.getElementById('total');
                this.progressEl = document.getElementById('progress');
                this.thumbnailsEl = document.getElementById('thumbnails');
                this.loadingEl = document.getElementById('loading');
                this.prevBtn = document.getElementById('prevBtn');
                this.nextBtn = document.getElementById('nextBtn');

                this.videoElement = null;
                this.imageElements = [];

                this.init();
            }}

            init() {{
                // 创建图片元素
                this.slides.forEach((slidePath, index) => {{
                    const img = document.createElement('img');
                    img.src = slidePath;
                    img.className = 'slide-image';
                    img.alt = `幻灯片 ${{index + 1}}`;
                    img.addEventListener('click', () => this.onSlideClick());
                    this.container.appendChild(img);
                    this.imageElements.push(img);
                }});

                // 创建视频元素
                this.videoElement = document.createElement('video');
                this.videoElement.className = 'video-player';
                this.videoElement.preload = 'auto';
                this.videoElement.addEventListener('click', () => this.toggleVideo());
                this.videoElement.addEventListener('ended', () => this.onVideoEnded());
                this.container.appendChild(this.videoElement);

                // 创建缩略图
                this.createThumbnails();

                // 更新总页数
                this.totalIndicator.textContent = this.slides.length;

                // 绑定事件
                this.bindEvents();

                // 显示第一页
                this.showSlide(0);

            }}

            createThumbnails() {{
                this.slides.forEach((slidePath, index) => {{
                    const thumb = document.createElement('img');
                    thumb.src = slidePath;
                    thumb.className = 'thumbnail';
                    thumb.addEventListener('click', () => this.goToSlide(index));
                    this.thumbnailsEl.appendChild(thumb);
                }});
            }}

            bindEvents() {{
                // 键盘控制
                document.addEventListener('keydown', (e) => {{
                    switch(e.key) {{
                        case 'ArrowLeft':
                        case 'ArrowUp':
                        case 'PageUp':
                            e.preventDefault();
                            this.previousSlide();
                            break;
                        case 'ArrowRight':
                        case 'ArrowDown':
                        case 'PageDown':
                            e.preventDefault();
                            this.nextSlide();
                            break;
                        case ' ':
                            e.preventDefault();
                            this.onSlideClick();
                            break;
                        case 'Home':
                            e.preventDefault();
                            this.goToSlide(0);
                            break;
                        case 'End':
                            e.preventDefault();
                            this.goToSlide(this.slides.length - 1);
                            break;
                        case 'f':
                        case 'F':
                            this.toggleFullscreen();
                            break;
                        case 't':
                        case 'T':
                            this.toggleThumbnails();
                            break;
                        case 'Escape':
                            if (this.showThumbnails) {{
                                this.toggleThumbnails();
                            }}
                            break;
                    }}
                }});

                // 导航按钮
                this.prevBtn.addEventListener('click', () => this.previousSlide());
                this.nextBtn.addEventListener('click', () => this.nextSlide());

                // 触摸滑动支持
                let touchStartX = 0;
                this.container.addEventListener('touchstart', (e) => {{
                    touchStartX = e.touches[0].clientX;
                }});

                this.container.addEventListener('touchend', (e) => {{
                    const touchEndX = e.changedTouches[0].clientX;
                    const diff = touchStartX - touchEndX;
                    if (Math.abs(diff) > 50) {{
                        if (diff > 0) {{
                            this.nextSlide();
                        }} else {{
                            this.previousSlide();
                        }}
                    }}
                }});
            }}

            showSlide(index) {{
                if (index < 0 || index >= this.slides.length) return;

                this.currentSlide = index;
                this.isVideoPlaying = false;

                // 隐藏所有
                this.imageElements.forEach(img => img.classList.remove('active'));
                this.videoElement.classList.remove('active');
                this.videoElement.pause();

                // 显示当前图片
                this.imageElements[index].classList.add('active');

                // 更新UI
                this.updateUI();
            }}

            updateUI() {{
                // 更新页码
                this.currentIndicator.textContent = this.currentSlide + 1;

                // 更新进度条
                const progress = ((this.currentSlide + 1) / this.slides.length) * 100;
                this.progressEl.style.width = progress + '%';

                // 更新按钮状态
                this.prevBtn.disabled = this.currentSlide === 0;
                this.nextBtn.disabled = this.currentSlide === this.slides.length - 1;

                // 更新缩略图
                const thumbs = this.thumbnailsEl.querySelectorAll('.thumbnail');
                thumbs.forEach((thumb, i) => {{
                    thumb.classList.toggle('active', i === this.currentSlide);
                }});
            }}

            onSlideClick() {{
                const slideNum = (this.currentSlide + 1).toString();

                if (this.isVideoPlaying) {{
                    // 正在播放视频，点击暂停/播放
                    this.toggleVideo();
                }} else if (this.videos[slideNum]) {{
                    // 有视频，播放视频
                    this.playVideo(this.videos[slideNum]);
                }} else {{
                    // 没有视频，下一页
                    this.nextSlide();
                }}
            }}

            playVideo(videoPath) {{
                this.loadingEl.classList.add('active');

                this.imageElements[this.currentSlide].classList.remove('active');
                this.videoElement.src = videoPath;
                this.videoElement.classList.add('active');

                // 第1页（封面）循环播放
                this.videoElement.loop = (this.currentSlide === 0);

                this.videoElement.onloadeddata = () => {{
                    this.loadingEl.classList.remove('active');
                    this.videoElement.play();
                    this.isVideoPlaying = true;
                }};

                this.videoElement.onerror = () => {{
                    this.loadingEl.classList.remove('active');
                    this.showSlide(this.currentSlide);
                }};
            }}

            toggleVideo() {{
                if (this.videoElement.paused) {{
                    this.videoElement.play();
                }} else {{
                    this.videoElement.pause();
                }}
            }}

            onVideoEnded() {{
                this.isVideoPlaying = false;
                // 视频播放完，显示当前页图片
                this.showSlide(this.currentSlide);
            }}

            nextSlide() {{
                if (this.isVideoPlaying) {{
                    // 跳过视频
                    this.videoElement.pause();
                    this.isVideoPlaying = false;
                }}

                if (this.currentSlide < this.slides.length - 1) {{
                    this.showSlide(this.currentSlide + 1);
                }}
            }}

            previousSlide() {{
                if (this.isVideoPlaying) {{
                    this.videoElement.pause();
                    this.isVideoPlaying = false;
                }}

                if (this.currentSlide > 0) {{
                    this.showSlide(this.currentSlide - 1);
                }}
            }}

            goToSlide(index) {{
                if (this.isVideoPlaying) {{
                    this.videoElement.pause();
                    this.isVideoPlaying = false;
                }}
                this.showSlide(index);
            }}

            toggleFullscreen() {{
                if (!document.fullscreenElement) {{
                    document.documentElement.requestFullscreen();
                }} else {{
                    document.exitFullscreen();
                }}
            }}

            toggleThumbnails() {{
                this.showThumbnails = !this.showThumbnails;
                this.thumbnailsEl.classList.toggle('visible', this.showThumbnails);
            }}
        }}

        // 启动播放器
        window.addEventListener('DOMContentLoaded', () => {{
            new SlideShowPlayer();
        }});
    </script>
</body>
</html>
'''

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"HTML播放器已生成: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description='生成交互式幻灯片HTML播放器',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例:
  # 在当前目录生成
  python generate_slideshow.py

  # 指定目录
  python generate_slideshow.py --dir /path/to/slides

  # 指定输出文件名和标题
  python generate_slideshow.py --output presentation.html --title "我的报告"

支持的文件格式:
  - 图片: 1.png, 2.png, 3.png, ... (数字命名)
  - 视频: N.mp4 (对应N.png)

操作说明:
  - 方向键翻页
  - 点击图片或Space: 播放该页视频(如有)
  - T: 显示/隐藏缩略图导航
  - F: 全屏
  - Home/End: 跳转首页/末页
  - 触摸滑动: 左右翻页(移动设备)
        '''
    )

    parser.add_argument(
        '--dir', '-d',
        default='.',
        help='幻灯片目录 (默认: 当前目录)'
    )

    parser.add_argument(
        '--output', '-o',
        default='slideshow.html',
        help='输出HTML文件名 (默认: slideshow.html)'
    )

    parser.add_argument(
        '--title', '-t',
        default='幻灯片播放器',
        help='页面标题'
    )

    args = parser.parse_args()

    # 扫描目录
    directory = os.path.abspath(args.dir)
    print(f"扫描目录: {directory}")

    if not os.path.exists(directory):
        print(f"目录不存在: {directory}")
        return 1

    data = scan_slides(directory)

    if not data['slides']:
        print("未找到幻灯片图片 (格式: 1.png, 2.png, ...)")
        return 1

    print(f"找到 {data['total']} 张幻灯片")
    for s in data['slides'][:5]:
        print(f"   - {s['filename']}")
    if data['total'] > 5:
        print(f"   ... 共 {data['total']} 张")

    if data['videos']:
        print(f"找到 {len(data['videos'])} 个视频")
        for key, path in data['videos'].items():
            print(f"   - 第{key}页: {path}")

    # 生成HTML
    output_path = os.path.join(directory, args.output)
    generate_html(data, output_path, args.title)

    print(f"\n完成！用浏览器打开 {output_path} 即可播放")
    return 0


if __name__ == "__main__":
    exit(main())
