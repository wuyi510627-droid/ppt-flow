# ppt-flow

中文学术组会 / 讨论班 PPT 技能：用问题组织材料，用文字和图形共同解释机制，生成可编辑幻灯片，同步逐页讲稿与备注。支持 Codex 与 Claude Code。

仓库根目录就是完整技能，包含 SKILL.md、references/、scripts/、assets/ 和 examples/。

## 克隆即安装

本仓库为私有仓库，需使用有访问权限的 GitHub 账号。先完成自己的 HTTPS 或 SSH 认证，再选择一种安装方式。

**Codex：**

```bash
git clone https://github.com/wuyi510627-droid/ppt-flow.git ~/.agents/skills/ppt-flow
```

**Claude Code：**

```bash
git clone https://github.com/wuyi510627-droid/ppt-flow.git ~/.claude/skills/ppt-flow
```

也可克隆到项目的 .agents/skills/ppt-flow 或 .claude/skills/ppt-flow。克隆后技能即可被发现；如没有出现，重启应用。不要将整个仓库再套进另一层 ppt-flow/。

## 使用

> 使用 ppt-flow，帮我准备一次 30 分钟的组会汇报。结合附件确定论证主线，设计图文协同、画面有层次的页面，最后给我 PPT 和逐页讲稿。

修改旧稿：

> 使用 ppt-flow 修改这个 PPT。沿用现有模板和收货地址例子，取消独立分类章节，减少文字、多画机制图，目录、页码和讲稿一起同步。已确认内容不重复询问。

仅修改局部：

> 使用 ppt-flow，把第 13 页改成三种经验表示的对比图，只修改这一页和对应讲稿。

按任务选择阶段，不强制从选题重走。支持技能点名的 Codex 界面可使用 $ppt-flow；Claude Code 可使用 /ppt-flow。

## 推荐制作节奏

复杂汇报按四轮推进。先确定目录和逐页结论，再补论文证据与案例，之后设计机制图，最后统一排版并渲染检查。用户反馈“内容不够饱满”时，优先回到内容轮检查每页是否缺少机制、例子、实验信息或过渡语。

当前默认样式参考用户确认的《Agent Memory.pptx》和《Agent长程任务中的信用分配.pptx》。它们强调绿色页眉、章节面包屑、绿蓝紫橙语义配色、多内容区布局，以及每页完整的结论—图示—例子/实验—过渡结构。参考的是组织方式，具体页面仍需按当前主题重新设计。

完整制作默认采用协作式流程。选题、大纲、材料清单、论文阅读、逐页内容、出 PPT、复盘分别产出可查看结果。每一步都保留用户修改和确认的入口，用户可以在任何阶段调整主题、例子、论文范围、页面密度和图示方式。

组会汇报默认按约 40 分钟规划。需要调整时，优先选择 30、40 或 50 分钟，并同步调整论文数量、页面数量和讲解深度。

需要用户做阶段选择时，Codex 若提供点击选项控件会优先使用控件。当前会话没有控件时，技能会沿用已有上下文继续推进，减少重复输入。

## 首次出片环境

读规则、选题与写讲稿不需要安装 Python 包。附带出片脚本需要 Python 3.9+，推荐当前受支持的版本。助手可以复用宿主已有环境，也可以在仓库内准备隔离环境。

从仓库根目录执行：

```bash
python3 scripts/check_env.py
# 仅缺依赖时运行；不改系统 Python
python3 scripts/setup_env.py
.venv/bin/python scripts/check_env.py
.venv/bin/python scripts/build.py outputs/quickstart.pptx examples/quickstart.py
.venv/bin/python scripts/check_fit.py outputs/quickstart.pptx
```

Windows 解释器为 .venv\Scripts\python.exe。需要 PDF 转图或数据绘图时用 python3 scripts/setup_env.py --qa 安装额外依赖。安装过程会从 Python 包源下载依赖。

快速示例应生成 4 页 PPT 和 outputs/quickstart_讲稿.md。图片路径按片段所在目录解析，可从任意工作目录调用脚本。更多用法见 [脚本说明](references/scripting.md)。

宿主提供专用制作或渲染工具时，也可以沿用本技能规则，使用宿主工具出片。

## 个人资料与模板

个人资料不随技能提交：

```bash
python3 scripts/init_data.py --data-dir /你的资料目录/ppt-flow-data
```

将 PPTFLOW_DATA 环境变量指向该目录，或在请求中说明资料位置。模板只包含空白档案和选题池。默认位置见 [流程说明](references/process.md)。

- PPTFLOW_TEMPLATE：替换模板 PPTX；版式索引要求见 [模板说明](assets/templates/seu/template.md)。
- PPTFLOW_FONT：替换 Noto Sans SC 字体；换字体后重新检查排版。
- PPTFLOW_PRESENTER：封面汇报人；也可直接传入 cover() 的 presenter 参数。

保留原包的东南大学模板和绿、蓝、紫、橙配色，机制图优先可编辑。

## 更新与验证

```bash
git pull --ff-only
python3 scripts/check_env.py
# 使用已配置依赖的解释器
.venv/bin/python -m unittest discover -s tests -v
```

原包 33 页 Agent Memory 演示保留在 [历史示例](examples/legacy-agent-memory/README.md)，用于兼容性验证，论文内容需要另行核实。当前制作推荐 quickstart.py 和最新规则。

见 [变更记录](references/changelog.md)。仓库不包含运行凭据，不通过脚本发布 PPT 或发送消息。
