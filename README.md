# Excel 动态图表的 Python 迁移实现

> 《大数据分析及数据可视化》课程实验 —— 将《Excel 数据可视化——从图表到数据大屏》第三章「动态图表」的 7 个案例从 Excel（控件 + 公式 + VBA）迁移为 Python（pandas + pyecharts）实现，并整合为可拖拽的数据大屏。

## 项目简介

原 Excel 工作簿《第三章 动态图表.xlsm》通过 **表单控件、INDEX/VLOOKUP 公式、数据透视表切片器、VBA 宏** 实现图表动态交互。本项目用 Python 完整复现全部 7 个案例：

| # | 案例 | Excel 动态机制 | Python 实现 |
|---|---|---|---|
| 1 | 动态柱形图 | 控件单元格 + INDEX/VLOOKUP 取数 | `Bar + Timeline` |
| 2 | 动态跑道图 | 圆环图 + 占位（总人数/2−数值） | 多环嵌套 `Pie + Timeline` |
| 3 | 动态南丁格尔圆环图 | 控件输入切换统计周期 | `Pie(rosetype="radius") + Timeline` |
| 4 | 动态组合图 | 复选框 + IF 控制系列显隐 | `Bar + Line` 双轴 + 图例开关 |
| 5 | 数据透视表 + 切片器 | 透视表按学历统计平均月收入 | `pandas.pivot_table + Tab` |
| 6 | VBA 动态玉玦图 | VBA 宏按钮切换周期 | 多环 `Pie + Tab`（选项卡替代宏按钮） |
| 7 | 动态滑珠图 | 组合框 + 选项按钮 + 辅助列 | 堆积 `Bar + EffectScatter + Timeline` |
| ★ | 综合数据大屏 | —— | `Page` 可拖拽布局整合全部案例 |

## 在线预览

- **Notebook 源码与讲解**：[在 nbviewer 中查看](https://nbviewer.org/github/sheelor/excel-dynamic-charts-python/blob/main/第三章_动态图表_Python实现.ipynb)
- 运行 Notebook 后会在 `output/` 生成 8 个交互式 HTML（7 个案例 + 数据大屏），浏览器打开即可交互操作

## 效果预览（截图位于 docs/images/）

| 动态柱形图 | 动态跑道图 | 南丁格尔圆环图 |
|---|---|---|
| ![案例1](docs/images/案例1_动态柱形图.png) | ![案例2](docs/images/案例2_动态跑道图.png) | ![案例3](docs/images/案例3_动态南丁格尔圆环图.png) |

| 动态组合图 | 透视表切片器 | 动态滑珠图 |
|---|---|---|
| ![案例4](docs/images/案例4_动态组合图.png) | ![案例5](docs/images/案例5_透视表切片器.png) | ![案例7](docs/images/案例7_动态滑珠图.png) |

## 项目结构

```
├── 第三章_动态图表_Python实现.ipynb   # 主实验 Notebook（可直接运行，含全部代码与讲解）
├── data/                            # 案例数据（从 Excel 1:1 提取的 CSV）
│   ├── 案例1_区域月度销售额.csv
│   ├── 案例2_部门月度人数.csv
│   ├── 案例3_流量来源占比.csv
│   ├── 案例4_化妆品销售.csv
│   ├── 案例5_人力资源明细.csv        # 1470 条员工明细
│   ├── 案例6_玉玦图流量来源.csv
│   └── 案例7_区域月度完成率.csv
├── output/                          # 运行 Notebook 后生成的交互式 HTML 图表（未入库）
├── docs/
│   ├── images/                      # 图表截图（README/报告用，未入库）
│   └── 实验报告.docx                 # 课程实验报告（未入库）
└── requirements.txt
```

> `output/` 与 `docs/` 为运行产物与二进制附件，可通过仓库网页端「Add file → Upload files」拖入对应文件夹补充上传。

## 快速开始

```bash
# 1. 安装依赖（建议 Python 3.10+）
pip install -r requirements.txt

# 2. 启动 Jupyter 并打开主 Notebook
jupyter notebook 第三章_动态图表_Python实现.ipynb
```

逐单元格运行即可在 Notebook 中查看交互式图表；同时会在 `output/` 目录生成 8 个独立的 HTML 文件，双击即可在浏览器中打开（支持时间轴拖动、选项卡切换、图例开关、大屏拖拽布局）。

> 提示：图表 JS 依赖默认从 CDN（assets.pyecharts.org）加载，打开 HTML 时需要联网。

## Excel → Python 机制对照

| Excel | Python |
|---|---|
| 控件单元格 + INDEX/VLOOKUP | `Timeline` 时间轴组件 |
| 复选框 + IF 隐藏系列 | 图例 `Legend` 点击开关 |
| 数据透视表 | `pandas.pivot_table` / `groupby` |
| 切片器 | `Tab` 选项卡 |
| VBA 宏按钮 | `Tab` 选项卡（无需宏，无安全性限制） |
| 多个工作表分散展示 | `Page` 整合为数据大屏，可直接部署为 Web 页面 |

## 环境

- Python 3.12
- pandas 2.3 / pyecharts 2.1（底层 Apache ECharts 6）
- Jupyter Notebook

## License

MIT
