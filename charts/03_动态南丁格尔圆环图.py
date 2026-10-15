"""03 动态南丁格尔圆环图：流量来源占比（Pie 玫瑰图 + Timeline 时间轴）

Excel 原效果：圆环图 + 选项按钮切换"近7天 / 近30天"。
Python 复现：rosetype="radius" 玫瑰图按占比映射半径，
            内半径 20% 形成圆环，Timeline 切换统计周期。
数据：各流量来源占比（单位：%）
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import PALETTE, save_html, snapshot

from pyecharts import options as opts
from pyecharts.charts import Pie, Timeline

SOURCES = ["首页推荐", "关注页面", "搜索", "个人主页", "其他来源"]
SHARE = {
    "近7天": [0.44, 0.17, 0.15, 0.08, 0.16],
    "近30天": [0.38, 0.21, 0.15, 0.09, 0.17],
}


def build_chart():
    tl = Timeline(init_opts=opts.InitOpts(width="920px", height="560px"))
    for period, values in SHARE.items():
        data = [(s, round(v, 4)) for s, v in zip(SOURCES, values)]
        rose = (
            Pie(init_opts=opts.InitOpts(width="920px", height="560px"))
            .add(
                period, data,
                radius=["20%", "70%"],            # 内半径形成圆环
                center=["50%", "52%"],
                rosetype="radius",                # 南丁格尔玫瑰图：半径映射数值
                label_opts=opts.LabelOpts(formatter="{b}\n{d}%", font_size=13),
            )
            .set_colors(PALETTE)
            .set_global_opts(
                title_opts=opts.TitleOpts(title=f"流量来源占比（{period}）"),
                legend_opts=opts.LegendOpts(orient="vertical", pos_left="right", pos_top="middle"),
                tooltip_opts=opts.TooltipOpts(formatter="{b}: {c} ({d}%)"),
            )
        )
        tl.add(rose, period)
    tl.add_schema(play_interval=2000, is_auto_play=False, is_loop_play=False, pos_bottom="0%")
    return tl


if __name__ == "__main__":
    save_html(build_chart(), "03_动态南丁格尔圆环图")
    snapshot("03_动态南丁格尔圆环图")
