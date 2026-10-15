"""08 综合数据大屏：Page 可拖拽布局整合全部案例

Excel 原效果：数据大屏将多个动态图表放在同一画布展示。
Python 复现：pyecharts Page(DraggablePageLayout) 整合案例 1—7，
            浏览器打开后可自由拖拽每个图表的位置与大小。
注：pyecharts 2.x 的 Page 不能嵌套 Tab 组件，
    因此大屏中案例 5 / 案例 6 各取一张代表性图表（全部部门、近 30 天）。
"""
import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import DATA_DIR, PALETTE, save_html, snapshot

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Page, Pie
from pyecharts.commons.utils import JsCode

EDU_ORDER = ["高中", "专科", "本科", "硕士", "博士"]
SOURCES6 = ["个人主页", "搜索", "关注页面", "首页推荐"]
SHARE6_30 = [0.09, 0.24, 0.29, 0.38]

LABEL_PCT = JsCode(
    "function(p){return p.name === '占位' ? '' : p.name + '\\n' + (p.value * 100).toFixed(0) + '%';}")


def _build_bar5_all():
    """案例 5 代表性图表：全部员工各学历平均月收入。"""
    df = pd.read_csv(os.path.join(DATA_DIR, "案例5_人力资源明细.csv"))
    g = df.groupby("学历")["月收入"].mean().reindex(EDU_ORDER).round(0)
    return (
        Bar(init_opts=opts.InitOpts(width="920px", height="500px"))
        .add_xaxis(EDU_ORDER)
        .add_yaxis("平均月收入", g.tolist(), color="#4472C4",
                   label_opts=opts.LabelOpts(position="top", formatter="{c} 元"))
        .set_global_opts(
            title_opts=opts.TitleOpts(title=f"各学历平均月收入（全部，{len(df)} 人）"),
            yaxis_opts=opts.AxisOpts(name="平均月收入（元）"),
            legend_opts=opts.LegendOpts(is_show=False))
    )


def _build_pie6_30():
    """案例 6 代表性图表：近 30 天流量来源玉玦图。"""
    pie = Pie(init_opts=opts.InitOpts(width="920px", height="560px"))
    for i, (s, v) in enumerate(zip(SOURCES6, SHARE6_30)):
        inner, outer = 15 + i * 14, 15 + i * 14 + 11
        pie.add(s, [(s, v), ("占位", round(0.5 - v, 4))],
                radius=[f"{inner}%", f"{outer}%"],
                label_opts=opts.LabelOpts(formatter=LABEL_PCT, font_size=12))
    pie.set_colors(["#ED7D31", "#A5A5A5", "#FFC000", "#4472C4"] + ["#EBEBEB"] * 4)
    pie.set_global_opts(
        title_opts=opts.TitleOpts(title="流量来源玉玦图（近30天）", pos_top="2%"),
        legend_opts=opts.LegendOpts(is_show=False))
    return pie


def build_chart():
    tl1 = importlib.import_module("01_动态柱形图").build_chart()
    tl2 = importlib.import_module("02_动态跑道图").build_chart()
    tl3 = importlib.import_module("03_动态南丁格尔圆环图").build_chart()
    combo4 = importlib.import_module("04_动态组合图").build_chart()
    tl7 = importlib.import_module("07_动态滑珠图").build_chart()

    page = Page(page_title="第三章 动态图表 · Python 数据大屏",
                layout=Page.DraggablePageLayout)
    page.add(tl1, tl2, tl3, combo4, _build_bar5_all(), _build_pie6_30(), tl7)
    return page


if __name__ == "__main__":
    save_html(build_chart(), "08_综合数据大屏")
    print("提示：浏览器打开 output/08_综合数据大屏.html 后可自由拖拽布局")
    snapshot("08_综合数据大屏", height=1000, wait=4000)
