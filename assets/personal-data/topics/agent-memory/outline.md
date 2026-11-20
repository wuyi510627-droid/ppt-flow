# Agent Memory 研究大纲(更新版)

暂定标题:**Agent Memory——存什么、怎么存、怎么用**
时长:约 40 分钟
主线:记忆是 agent 的一连串决策(写什么、怎么整理、何时取),这些决策能否被学出来、效果怎么评。与信用分配方向相连。

```
Anthropic 的分层(由底到顶):
  转录日志 transcripts   完整事件记录,可检索
  记忆笔记 notes         对「值得记」的预测
  记忆表示 wiki 等       链接成网的结构化页面
  注入上下文             每次会话开头加载,必须很小
        ↑↓
  dreaming:离线反思,修正笔记、生成表示、上下搬运

生命周期:
  写入 → 表示 → 检索 → 利用(影响决策)
   ↑       ↓                  │
   └── 巩固 / 更新 / 遗忘 ←───┘        外圈:评测、安全
```

---

## 一、研究背景(5 分钟)

- 例子引出:agent 跨会话忘了用户偏好,或重复踩同一个坑。
- 什么是 agent memory:Anthropic 的定义是「从经验中获得、跨会话保存、以后可读取的上下文」。它明确排除三样东西:改权重、单次对话内的上下文学习、压缩(compaction)。
- 对照:综述 2512.13564 把参数化记忆也算进来。两种口径的差别可作为讨论点。
- 为什么难:写的时候不知道以后什么重要(Anthropic 的核心命题)。
- 与长程任务的上下文管理相关(PDF 3.5)。

## 二、记忆的分类(8 分钟)

**综述的视角**
- 2512.13564(Memory in the Age of AI Agents):
  - 形式:token 级(平面 1D / 2D / 层级 3D)、参数化(内部 / 外部)、潜在(generate / reuse / transform)
  - 功能:事实、经验、工作记忆
  - 动态:形成、演化、检索
- 2603.07670(Memory for Autonomous LLM Agents):
  - 时间范围:工作、情景、语义、程序
  - 载体:上下文内文本、向量库、结构化存储、可执行库、混合
  - 控制策略:启发式、提示自控、学习式
  - 五类机制:上下文压缩、检索增强、反思自改进、分层虚拟上下文、策略学习式管理
- 2602.19320(Anatomy of Agentic Memory),四种结构:轻量语义、实体中心/个性化、情景/反思、结构化/分层
- 2505.00675(Rethinking Memory):参数化 / 上下文两个维度,6 种原子操作(巩固、更新、索引、遗忘、检索、压缩)
- 2504.15965(From Human Memory to AI Memory):对象 × 形式 × 时间,8 个象限,类比人类记忆

**一页「分类并不统一」**:同一个方法在不同综述里归类不同,例如 A-MEM 在 2512.13564 是平面 token 记忆,在 2602.19320 是实体中心记忆。

**表示方式**(PDF 4.2):文本/向量、结构化槽位、图、情景、程序/技能、分层。

## 三、记忆的生命周期(16 分钟,主体)

每节沿用叙事:解决的问题 → 核心 → 方法 → 优缺点。

| 环节 | 要回答的问题 | 来源与代表 |
|---|---|---|
| 形成 | 写什么、何时写 | PDF 4.1;Generative Agents(2304.03442)、Reflexion(2303.11366);Anthropic:现场写 vs 事后 dreaming,让强模型自己判断显著性,别用「只记失败」这类固定规则 |
| 表示 | 以什么形式存 | PDF 4.2;Voyager 技能库(2305.16291)、MemGPT 分层(2310.08560)、Zep 时间知识图谱(2501.13956) |
| 检索 | 相似不等于有用 | PDF 4.3;Mem0(2504.19413)的检索流水线 |
| 巩固 | 零散经历变成知识 | PDF 4.4;A-MEM(2502.12110);Anthropic 的 dreaming,源头是 sleep-time compute(2504.13171) |
| 更新与遗忘 | 过期、矛盾的记忆 | PDF 4.5;Zep 的时间维度;Anthropic:错误笔记会反复误导 agent |
| 利用 | 取到了,决策真变好吗 | PDF 4.6 |

**代表方法(摘要核对)**
- Generative Agents:记录经历、反思成高层结论、动态检索;25 个智能体的沙盒小镇。
- Reflexion:每次尝试后写文字反思存入情景记忆,不改权重;HumanEval pass@1 91%。
- Voyager:可执行代码的技能库,可组合复用,跨世界迁移。
- MemGPT:仿操作系统的虚拟上下文管理,分层存储。
- Zep:时间感知知识图谱(Graphiti);DMR 94.8% 对 MemGPT 93.4%;LongMemEval 最高提升 18.5%、延迟降 90%(作者报告)。
- A-MEM:Zettelkasten 式笔记互相链接,新记忆会更新旧记忆。
- Mem0:提取、巩固、检索的流水线,另有图变体;LOCOMO 上对 OpenAI 记忆基线相对提升 26%,p95 延迟降 91%(作者报告)。

**Anthropic 案例(数字待对原文)**
- Pokémon Red:一条关于地点的错误笔记导致反复失败,dreaming 修正后才通过该段。
- 维基实验:语料约 35 万文件,128 次 dreaming 后,仅用 wiki 的准确率从 13% 升到 48%;wiki 加检索 61%,单用检索 53%。
- 反例:有的任务里 wiki 涨到语料的 1.77 倍,收益不明确。
- 共享表格被多个 agent 覆盖写会丢事实(57 条中剩 41 条);每份合同一页后恢复完整。

**贯穿线:学习式控制**(2603.07670 的第三个维度)
- PDF 里的对应:Learned Memory Writing Policy(4.1)、Learned Retrieval Policy(4.3)、Memory-Conditioned Policy Learning(4.6)。
- 综述点名的 RL 相关工作:Memory-R1、MemRL、AgeMem(待核实)。

## 四、评测(5 分钟)

- PDF 4.7 的五种做法:召回、任务收益、跨会话、消融、鲁棒性/过期。
- 核心观点:「记得住」不等于「用得好」。
- 基准:
  - LoCoMo(2402.17753):平均约 300 轮、9K token、最多 35 个会话;任务含问答、事件摘要、多模态对话。
  - LongMemEval(2410.10813,ICLR 2025):500 个问题,5 种能力(信息抽取、多会话推理、时间推理、知识更新、拒答);商用助手和长上下文模型准确率下降约 30%。
  - MemBench、MemoryAgentBench、MemoryArena(2603.07670 分析,未打开)。
- Anthropic:CL-Bench 1.0 数据库任务,带记忆后 Sonnet 5.5 从 0.644 升到 0.833,Opus 5.5 从 0.655 升到 0.838。
- 2602.19320 的批评:基准过小或饱和、指标与语义有用性不一致、对评审模型敏感、依赖骨干模型、系统开销被忽视。

## 五、开放问题与延伸(5 分钟)

- Anthropic 的四个问题:何时创建(现场 vs 事后)、如何保鲜、转录日志是否该做底层、随模型变强怎么演化。
- 综述的方向:记忆自动化、与 RL 结合、多模态、多智能体、可信性(2512.13564)。
- 安全:2604.16548 按 6 个阶段(写入、存储、检索、执行、共享传播、遗忘回滚)梳理攻击与防御。
- 与信用分配的联系:写笔记是一次「预测它以后有用」的决策,怎么给它做信用分配,还没有被系统回答(这是我的观察,不是任何一篇文章的结论)。

## 六、总结(1 分钟)

---

## 仍待核实

- RL 学记忆管理的工作:Memory-R1、MemRL、AgeMem,没打开原文。
- Anthropic 文章里的数字来自网页摘要,上 PPT 前要对原文。
- 2512.13564(资源与框架)、2603.07670(开放问题章节)后半部分没读。
- MemBench、MemoryAgentBench、MemoryArena 未打开。

## 参考

- Anthropic, The components of agent memory (2026-11-06): https://www.anthropic.com/research/components-of-agent-memory
- 2512.13564 Memory in the Age of AI Agents
- 2603.07670 Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers
- 2602.19320 Anatomy of Agentic Memory
- 2505.00675 Rethinking Memory in LLM based Agents
- 2504.15965 From Human Memory to AI Memory
- 2604.16548 A Survey on Long-Term Memory Security in LLM Agents
- 2504.13171 Sleep-time Compute
- 方法与基准:2304.03442、2303.11366、2305.16291、2310.08560、2501.13956、2502.12110、2504.19413、2402.17753、2410.10813
