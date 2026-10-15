"""05 数据透视表 + 切片器：各部门各学历平均月收入（pandas 透视 + Tab 选项卡）

Excel 原效果：数据透视表 + 部门切片器，点击部门即切换统计范围。
Python 复现：pandas pivot_table 复现透视计算，
            pyecharts Tab 选项卡等价于切片器，点击部门标签即切换图表。
数据：data/案例5_人力资源明细.csv（1470 名员工明细）
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import DATA_DIR, save_html, snapshot

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Tab

EDU_ORDER = ["高中", "专科", "本科", "硕士", "博士"]
CSV_PATH = os.path.join(DATA_DIR, "案例5_人力资源明细.csv")


def build_chart():
    df = pd.read_csv(CSV_PATH)
    tab = Tab()
    dept_list = ["全部"] + sorted(df["部门"].unique().tolist())

    for dept in dept_list:
        sub = df if dept == "全部" else df[df["部门"] == dept]
        g = sub.groupby("学历")["月收入"].mean().reindex(EDU_ORDER).round(0)
        bar = (
            Bar(init_opts=opts.InitOpts(width="920px", height="500px"))
            .add_xaxis(EDU_ORDER)
            .add_yaxis("平均月收入", g.tolist(), color="#4472C4",
                       label_opts=opts.LabelOpts(position="top", formatter="{c} 元"))
            .set_global_opts(
                title_opts=opts.TitleOpts(title=f"各学历平均月收入（{dept}，{len(sub)} 人）"),
                yaxis_opts=opts.AxisOpts(name="平均月收入（元）"),
                legend_opts=opts.LegendOpts(is_show=False),
            )
        )
        tab.add(bar, dept)   # 每个选项卡 ≈ 切片器的一个选项
    return tab


if __name__ == "__main__":
    save_html(build_chart(), "05_数据透视表切片器")
    snapshot("05_数据透视表切片器")
