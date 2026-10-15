"""06 VBA 动态玉玦图：流量来源占比（多环 Pie + Tab 选项卡替代 VBA 按钮）

Excel 原效果：VBA 按钮切换"近7天 / 近30天"，玉玦（缺角圆环）逐级展开。
Python 复现：每个来源一个缺角圆环（数值段 + 占位段，占位 = 0.5 − 占比），
            Tab 选项卡等价于两个 VBA 按钮。
数据：各流量来源占比（单位：%）
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save_html, snapshot

from pyecharts import options as opts
from pyecharts.charts import Pie, Tab
from pyecharts.commons.utils import JsCode

SOURCES = ["个人主页", "搜索", "关注页面", "首页推荐"]
SHARE = {
    "近7天": [0.13, 0.19, 0.32, 0.36],
    "近30天": [0.09, 0.24, 0.29, 0.38],
}

LABEL_PCT = JsCode(
    "function(p){return p.name === '占位' ? '' : p.name + '\\n' + (p.value * 100).toFixed(0) + '%';}")


def build_chart():
    tab = Tab()
    for period, values in SHARE.items():
        pie = Pie(init_opts=opts.InitOpts(width="920px", height="560px"))
        for i, (s, v) in enumerate(zip(SOURCES, values)):
            v = round(v, 4)
            inner, outer = 15 + i * 14, 15 + i * 14 + 11
            pie.add(
                s,
                [(s, v), ("占位", round(0.5 - v, 4))],   # 占位 = 0.5 − 占比（与 Excel 一致）
                radius=[f"{inner}%", f"{outer}%"],
                label_opts=opts.LabelOpts(formatter=LABEL_PCT, font_size=12),
            )
        pie.set_colors(["#ED7D31", "#A5A5A5", "#FFC000", "#4472C4"] + ["#EBEBEB"] * 4)
        pie.set_global_opts(
            title_opts=opts.TitleOpts(title=f"流量来源玉玦图（{period}）", pos_top="2%"),
            legend_opts=opts.LegendOpts(is_show=False),
            tooltip_opts=opts.TooltipOpts(formatter=JsCode(
                "function(p){return p.name === '占位' ? '' : p.seriesName + '：' + (p.value * 100).toFixed(0) + '%';}")),
        )
        tab.add(pie, period)   # 两个选项卡 ≈ 两个 VBA 按钮
    return tab


if __name__ == "__main__":
    save_html(build_chart(), "06_VBA动态玉玦图")
    snapshot("06_VBA动态玉玦图")
