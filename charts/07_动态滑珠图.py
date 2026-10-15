"""07 动态滑珠图：各区域目标完成率（堆积 Bar 滑轨 + EffectScatter 滑珠 + Timeline）

Excel 原效果：条形滑轨 + 滑珠，滚动条切换月份。
Python 复现：堆积柱形作浅色滑轨（完成率 + 未完成率 = 100%），
            EffectScatter 涟漪散点作滑珠，Timeline 切换月份。
数据：各区域月度目标完成率（单位：%）
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save_html, snapshot

from pyecharts import options as opts
from pyecharts.charts import Bar, EffectScatter, Timeline
from pyecharts.commons.utils import JsCode

MONTHS = ["1月", "2月", "3月", "4月", "5月", "6月"]
REGIONS = ["华北", "华南", "东北", "西北", "西南", "华东"]
RATES = {
    "1月": [0.32, 0.49, 0.65, 0.73, 0.536, 0.32],
    "2月": [0.45, 0.36, 0.53, 0.63, 0.498, 0.49],
    "3月": [0.66, 0.54, 0.58, 0.61, 0.527, 0.65],
    "4月": [0.52, 0.39, 0.48, 0.53, 0.708, 0.73],
    "5月": [0.69, 0.415, 0.445, 0.47, 0.7035, 0.536],
    "6月": [0.771, 0.403, 0.399, 0.408, 0.758, 0.7468],
}


def build_chart():
    tl = Timeline(init_opts=opts.InitOpts(width="920px", height="540px"))
    for m in MONTHS:
        rates = [round(v, 4) for v in RATES[m]]
        bar = (
            Bar(init_opts=opts.InitOpts(width="920px", height="540px"))
            .add_xaxis(REGIONS)
            .add_yaxis("完成率", rates, stack="slider", color="#4472C4", bar_width="45%",
                       label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis("未完成率", [round(1 - r, 4) for r in rates], stack="slider",
                       color="#DCE6F1", bar_width="45%",     # 浅色滑轨
                       label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
                title_opts=opts.TitleOpts(title=f"{m}各区域目标完成率", subtitle="滑珠位置即完成率水平"),
                legend_opts=opts.LegendOpts(is_show=False),
                xaxis_opts=opts.AxisOpts(name="区域"),
                yaxis_opts=opts.AxisOpts(name="完成率", max_=1,
                                         axislabel_opts=opts.LabelOpts(formatter=JsCode(
                                             "function(v){return (v*100).toFixed(0)+'%';}"))),
                tooltip_opts=opts.TooltipOpts(trigger="axis", formatter=JsCode(
                    "function(ps){var p=ps[0];var v=Array.isArray(p.value)?p.value[1]:p.value;"
                    "return p.name+'：完成率 '+(v*100).toFixed(1)+'%';}")),
            )
        )
        bead = (
            EffectScatter()
            .add_xaxis(REGIONS)
            .add_yaxis("滑珠", rates, symbol_size=16, color="#ED7D31",
                       label_opts=opts.LabelOpts(is_show=False))
        )
        bar.overlap(bead)
        tl.add(bar, m)
    tl.add_schema(play_interval=1500, is_auto_play=False, is_loop_play=False, pos_bottom="0%")
    return tl


if __name__ == "__main__":
    save_html(build_chart(), "07_动态滑珠图")
    snapshot("07_动态滑珠图")
