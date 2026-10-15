"""第三章 动态图表复现 · 公共配置与工具函数。

- PALETTE：与 Excel 默认主题接近的商务配色
- save_html：渲染 pyecharts 图表为可交互 HTML（输出到仓库根目录 output/）
- snapshot：用 Playwright 把 HTML 截取为 PNG（输出到仓库根目录 images/），
  未安装 Playwright 时自动跳过，不影响 HTML 生成
"""
import os

# 与 Excel 默认主题接近的商务配色
PALETTE = ["#4472C4", "#ED7D31", "#A5A5A5", "#FFC000", "#5B9BD5", "#70AD47"]

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(REPO_ROOT, "data")
OUTPUT_DIR = os.path.join(REPO_ROOT, "output")
IMAGES_DIR = os.path.join(REPO_ROOT, "images")


def save_html(chart, name):
    """渲染 pyecharts 图表为可交互的 HTML 文件，返回输出路径。"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, f"{name}.html")
    chart.render(path)
    print(f"[HTML] {path}")
    return path


def snapshot(name, width=1100, height=760, wait=2000):
    """用 Playwright 把 output/{name}.html 截取为 images/{name}.png。

    HTML 中的图表依赖在线 JS 资源（assets.pyecharts.org），截图需要联网。
    未安装 Playwright 时打印提示并跳过，不视为错误。
    """
    html_path = os.path.join(OUTPUT_DIR, f"{name}.html")
    png_path = os.path.join(IMAGES_DIR, f"{name}.png")
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print(f"[跳过截图] 未安装 playwright：{png_path} 未生成（HTML 不受影响）")
        return None
    os.makedirs(IMAGES_DIR, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="/usr/bin/chromium" if os.path.exists("/usr/bin/chromium") else None,
            args=["--no-sandbox", "--disable-gpu"],
        )
        page = browser.new_page(viewport={"width": width, "height": height})
        page.goto("file://" + html_path)
        page.wait_for_timeout(wait)
        page.screenshot(path=png_path, full_page=True)
        browser.close()
    print(f"[PNG ] {png_path}")
    return png_path
