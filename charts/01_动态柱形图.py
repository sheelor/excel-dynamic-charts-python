"""01 动态柱形图：各区域销售额（Bar + Timeline 时间轴）

Excel 原效果：插入滚动条控件，拖动切换月份。
Python 复现：Bar 按月份逐张生成，Timeline 时间轴串联，
            拖动时间轴即可播放 1—6 月各区域销售额。
数据：各区域月度销售额（单位与教材一致）
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import PALETTE, save_html, snapshot

from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline
from pyecharts.commons.utils import JsCode

MONTHS = ["1月", "2月", "3月", "4月", "5月", "6月"]
REGIONS = ["华北", "华南", "东北", "西北", "西南", "华东"]
SALES = {
    "1月": [259, 247, 705, 513, 463, 384],
    "2月": [235, 266, 529, 324, 579, 282],
    "3月": [330, 342, 705, 540, 492, 308],
    "4月": [282, 342, 599, 270, 492, 384],
    "5月": [282, 323, 705, 486, 405, 308],
    "6月": [965, 380, 282, 567, 463, 897],
}


def build_chart():
    tl = Timeline(init_opts=opts.InitOpts(width="920px", height="520px"))
    for m in MONTHS:
        bar = (
            Bar()
            .add_xaxis(REGIONS)
            .add_yaxis(
                "销售额", SALES[m],
                label_opts=opts.LabelOpts(position="top", font_size=13),
                itemstyle_opts=opts.ItemStyleOpts(color=JsCode(
                    "function(p){var cs=" + str(PALETTE) + ";return cs[p.dataIndex % cs.length];}")),
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title=f"{m}各区域销售额", subtitle="拖动下方时间轴切换月份"),
                yaxis_opts=opts.AxisOpts(name="销售额", max_=1000),
                legend_opts=opts.LegendOpts(is_show=False),
            )
        )
        tl.add(bar, m)
    tl.add_schema(play_interval=1500, is_auto_play=False, is_loop_play=False,
                  pos_bottom="0%", control_position="left")
    return tl


if __name__ == "__main__":
    save_html(build_chart(), "01_动态柱形图")
    snapshot("01_动态柱形图")
