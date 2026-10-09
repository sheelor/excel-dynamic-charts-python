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

## 补充上传二进制附件（GitHub / Gitee 均适用）

以下文件为运行产物或二进制文件，未包含在 git 提交中，可在仓库网页端手动补充：

- `docs/images/` 下的 8 张图表截图（README 中的预览图引用它们）
- `docs/实验报告.docx`（课程实验报告）
- `output/` 下的 8 个交互式 HTML（运行 Notebook 后可重新生成）

操作路径：仓库主页 →「Add file / 上传文件」→ 将上述文件拖入对应目录 → 提交。
上传后 README 中的截图预览即可正常显示。

## 开源检查清单

- [ ] 仓库设为公开（Public / 开源）
- [ ] LICENSE（MIT）已随仓库导入
- [ ] README 首页正常渲染（截图上传后图片可见）
- [ ] Notebook 可在仓库内直接预览源码
