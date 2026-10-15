# Gitee 上传步骤说明

本项目已在 GitHub 发布：https://github.com/sheelor/excel-dynamic-charts-python
以下任一方式可将实验内容同步到 Gitee 个人开源账号。

## 方式一：从 GitHub 一键导入（推荐）

1. 登录 Gitee，点击右上角「+」→「从 GitHub/GitLab 导入仓库」。
2. 绑定 GitHub 账号后，在列表中选择 `excel-dynamic-charts-python`，或直接填写仓库地址：
   `https://github.com/sheelor/excel-dynamic-charts-python.git`
3. 点击「导入」，等待完成即可。仓库默认公开（可在「管理 → 仓库设置」中确认开源属性与许可证）。

## 方式二：本地 git 命令行推送

```bash
# 在项目目录下（已包含全部文本文件的克隆或本地副本）
git clone https://github.com/sheelor/excel-dynamic-charts-python.git
cd excel-dynamic-charts-python

# 在 Gitee 网页端先新建一个同名空仓库（不要勾选初始化 README），然后：
git remote add gitee https://gitee.com/<你的用户名>/excel-dynamic-charts-python.git
git push gitee main
```

## 关于图片截图

README 引用的图表截图位于 `images/` 目录，由仓库自带的
`.github/workflows/render.yml` 在每次推送后**自动运行 `run_all.py` 生成并提交**，
无需手动上传。若想在本地生成，执行：

```bash
pip install playwright && playwright install chromium
python run_all.py
```

> 如果暂不配置 CI，也可以直接把本地 `images/` 下的 8 张 PNG
> 通过网页端「Add file → Upload files」上传到仓库。

## 可选：补充上传实验报告

`docs/实验报告.docx` 为课程实验报告（Word 二进制文件，未包含在 git 提交中）。
如需随仓库公开，可在仓库网页端「Add file / 上传文件」拖入 `docs/` 目录。

## 开源检查清单

- [ ] 仓库设为公开（Public / 开源）
- [ ] LICENSE（MIT）已随仓库导入
- [ ] README 首页正常渲染（推送后等待 CI 完成，截图即可见）
- [ ] Notebook 与 `第三章动态图表复现-全部代码汇总.md` 可在线预览
