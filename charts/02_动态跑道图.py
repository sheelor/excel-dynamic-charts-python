"""02 动态跑道图：各部门人数（多环嵌套 Pie + Timeline 时间轴）

Excel 原效果：数据按部门呈环形"跑道"排布，组合框切换月份。
Python 复现：每个部门一个圆环（数值段 + 灰色占位段），
            中心文字显示当月公司总人数，Timeline 切换月份。
数据：各部门月度人数（单位：人）
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import PALETTE, save_html, snapshot

from pyecharts import options as opts
from pyecharts.charts import Pie, Timeline
from pyecharts.commons.utils import JsCode

MONTHS = ["1月", "2月", "3月", "4月"]
DEPTS = ["人力部", "行政部", "财务部", "工程部", "采购部", "销售部"]
HEADCOUNT = {
    "1月": [130, 226, 238, 293, 326, 451],
    "2月": [138, 206, 228, 305, 349, 456],
    "3月": [130, 217, 255, 314, 316, 406],
    "4月": [129, 226, 226, 264, 359, 433],
}

# 只给"数值段"显示标签，占位段隐藏
LABEL_ONLY_VALUE = JsCode(
    "function(p){return p.name === '占位' ? '' : p.name + '\\n' + p.value + '人';}")


def build_chart():
    tl = Timeline(init_opts=opts.InitOpts(width="920px", height="600px"))
    for m in MONTHS:
        total = sum(HEADCOUNT[m])                    # 当月公司总人数
        pie = Pie(init_opts=opts.InitOpts(width="920px", height="600px"))
        for i, dept in enumerate(DEPTS):
            v = HEADCOUNT[m][i]
            placeholder = total / 2 - v              # 占位 = 总人数/2 − 部门人数（与 Excel 一致）
            inner, outer = 18 + i * 12, 18 + i * 12 + 10   # 每环宽度 10%、间隔 2%
            pie.add(
                dept,
                [(dept, v), ("占位", round(placeholder, 1))],
                radius=[f"{inner}%", f"{outer}%"],
                label_opts=opts.LabelOpts(formatter=LABEL_ONLY_VALUE, font_size=11),
            )
        pie.set_colors(PALETTE + ["#EBEBEB"] * 6)    # 占位段浅灰
        pie.set_global_opts(
            title_opts=opts.TitleOpts(
                title=f"{m}\n公司总人数为 {total}",
                pos_left="center", pos_top="middle",
                title_textstyle_opts=opts.TextStyleOpts(font_size=18, color="#333")),
            legend_opts=opts.LegendOpts(is_show=False),
            tooltip_opts=opts.TooltipOpts(formatter=JsCode(
                "function(p){return p.name === '占位' ? '' : p.seriesName + '：' + p.value + '人';}")),
        )
        tl.add(pie, m)
    tl.add_schema(play_interval=1800, is_auto_play=False, is_loop_play=False, pos_bottom="0%")
    return tl


if __name__ == "__main__":
    save_html(build_chart(), "02_动态跑道图")
    snapshot("02_动态跑道图", height=780)
