# ppt-flow

中文学术组会 / 讨论班 PPT 技能：用问题组织材料，用文字和图形共同解释机制，生成可编辑幻灯片，同步逐页讲稿与备注。支持 Codex 与 Claude Code。

组会模式默认服务于共同补知识和建立 Agent 研究框架。一次汇报约 40 分钟，可以选择 Problem statement 或 Technical family。确认主题后，先学习综述和代表工作，再共同确定技术路线与正式目录。前者梳理一个问题下的主要技术路线，后者梳理一类相关技术的联系、区别和适用场景。两种形式都需要解释可复用的实验范式，而不是只介绍一篇论文或逐公式讲解。

论文材料必须和大纲建立对应关系。每篇主讲论文要说明补充哪一章、哪条技术路线或哪种实验范式，并在全文阅读后核对方法、实验、结果、局限和图表。摘要只用于初筛。

约 40 分钟的专题可从正文 8–10 篇有明确用途的论文起步。选 4–6 篇讲透方法，其余用于补路线、横向比较或设实验基线，随主题调整。

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

新做组会先确认已有主题还是需要推荐。选择推荐时，根据研究方向图谱提供四个完整候选，用户确认后再进入领域学习。先看综述、一起读代表工作，再确认正式目录、逐页内容和样稿。节点确认后，可按用户要求逐页或批量制作。宿主支持点击选项时优先使用，组会默认 40 分钟，需要时可选 30 或 50 分钟。细节见 [协作流程](references/process.md)。

代表论文页用问题和核心做法开头，中间以机制图和案例讲方法，下方拆步骤并分别框出优点和局限。优先选能展示推理关系或验证依据的图，按最终画面写讲稿，交付前逐页渲染检查。版式见 [样式说明](references/style.md)。

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

此私有仓库已包含[研究方向图谱](assets/research/LLM%20Agent研究方向.pdf)和[个人资料](assets/personal-data/)。克隆后可按选题规则直接使用。需要另外建立本地资料目录时运行下列命令。

```bash
python3 scripts/init_data.py --data-dir /你的资料目录/ppt-flow-data
```

将 PPTFLOW_DATA 环境变量指向该目录，或在请求中说明资料位置。初始化模板提供空白档案和选题池。读取顺序见 [流程说明](references/process.md#研究资料和个人偏好)。

- PPTFLOW_TEMPLATE：替换模板 PPTX；版式索引要求见 [模板说明](assets/templates/seu/template.md)。
- PPTFLOW_FONT：替换 Noto Sans SC 字体；换字体后重新检查排版。
- PPTFLOW_PRESENTER：封面汇报人；也可直接传入 cover() 的 presenter 参数。

以所选东南大学模板为基准，使用协调的语义配色，机制图优先可编辑。

## 更新与验证

```bash
git pull --ff-only
python3 scripts/check_env.py
# 使用已配置依赖的解释器
.venv/bin/python -m unittest discover -s tests -v
```

原包 33 页 Agent Memory 演示保留在 [历史示例](examples/legacy-agent-memory/README.md)，用于兼容性验证，论文内容需要另行核实。当前制作推荐 quickstart.py 和最新规则。

见 [变更记录](references/changelog.md)。仓库不包含运行凭据，不通过脚本发布 PPT 或发送消息。
