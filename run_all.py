"""一键运行全部图表脚本。

用法：
    python run_all.py
"""
import os
import subprocess
import sys

CHARTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "charts")


def main():
    scripts = sorted(
        f for f in os.listdir(CHARTS)
        if f.endswith(".py") and f[:2].isdigit()
    )
    print(f"共 {len(scripts)} 个图表脚本：\n")

    failures = []
    for s in scripts:
        print(f"===== {s} =====")
        r = subprocess.run(
            [sys.executable, os.path.join(CHARTS, s)],
            capture_output=True, text=True,
        )
        sys.stdout.write(r.stdout)
        if r.returncode != 0:
            failures.append(s)
            sys.stderr.write(r.stderr)
            print(f"[失败] {s}")
        print()

    print("=" * 40)
    if failures:
        print(f"{len(failures)} 个脚本运行失败：")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)
    print("全部脚本运行成功。HTML 见 output/，截图见 images/。")


if __name__ == "__main__":
    main()
