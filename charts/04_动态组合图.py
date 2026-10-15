"""04 动态组合图：销售额 / 利润 / 利润率（Bar + Line 双轴，图例控制显隐）

Excel 原效果：柱形图 + 折线图双轴呈现，复选框控制系列显隐。
Python 复现：Bar（销售额、利润）+ extend_axis 扩展第二 Y 轴 +
            Line（利润率，yaxis_index=1），点击图例即可显示/隐藏系列。
数据：2022 年化妆品销售情况
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save_html, snapshot

from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from pyecharts.commons.utils import JsCode

CATEGORIES = ["口红", "面膜", "隔离", "粉底液"]
SALES = [2800, 2564, 2282, 2353]
PROFIT = [1896, 1563, 986, 1324]
MARGIN = [0.6771, 0.6096, 0.4321, 0.5627]


def build_chart():
    bar = (
        Bar(init_opts=opts.InitOpts(width="920px", height="540px"))
        .add_xaxis(CATEGORIES)
        .add_yaxis("销售额", SALES, color="#4472C4",
                   label_opts=opts.LabelOpts(position="top"))
        .add_yaxis("利润", PROFIT, color="#ED7D31",
                   label_opts=opts.LabelOpts(position="top"))
        .extend_axis(
            yaxis=opts.AxisOpts(
                name="利润率", min_=0, max_=1,
                axislabel_opts=opts.LabelOpts(formatter=JsCode(
                    "function(v){return (v * 100).toFixed(0) + '%';}")),
                splitline_opts=opts.SplitLineOpts(is_show=False),
            )
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2022年化妆品销售情况",
                                      subtitle="点击图例可显示/隐藏对应系列（等价于 Excel 复选框）"),
            yaxis_opts=opts.AxisOpts(name="金额（元）"),
            legend_opts=opts.LegendOpts(pos_top="12%"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="shadow"),
        )
    )
    line = (
        Line()
        .add_xaxis(CATEGORIES)
        .add_yaxis("利润率", MARGIN, yaxis_index=1,
                   color="#70AD47", symbol_size=12, is_smooth=True,
                   label_opts=opts.LabelOpts(formatter=JsCode(
                       "function(p){var v = Array.isArray(p.value) ? p.value[1] : p.value;"
                       "return (v * 100).toFixed(1) + '%';}"),
                       position="right", distance=10, color="#70AD47", font_weight="bold"))
    )
    return bar.overlap(line)


if __name__ == "__main__":
    save_html(build_chart(), "04_动态组合图")
    snapshot("04_动态组合图")
