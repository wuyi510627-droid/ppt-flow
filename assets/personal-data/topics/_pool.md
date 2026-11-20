# 选题池（_pool.md）

来源：LLM / Agent 研究问题与技术路线图谱（12 个领域、83 个小节）。
状态：未讲 / 已讲 / 候选（新增）。「相关度」是初判，待数据校准；数据列由刷新流程填写并标日期，空白表示还没查。

| 编号 | 小节 | 关键难点（图谱原文摘录） | 状态 | 相关度（初判） | 近一年论文量 | 最近有无综述 | 数据日期 |
|---|---|---|---|---|---|---|---|
| 1.1 | Agentic RL / Credit Assignment | 例如一段 40 次工具调用最终测试失败，不能直接断言所有动作都错了：模型需要识别真正造成失败的关键决策。 | 已讲（信用分配） | — | | | |
| 1.2 | Agentic RL / Exploration | 难点在于有意义的探索往往很贵；随机尝试太多会浪费环境调用，探索太少又只能复现既有能力。 | 未讲 | 高 | | | |
| 1.3 | Agentic RL / Reward Design | 好的奖励既要和真实任务目标一致，也要能自动大规模计算；奖励设错会导致 Agent 学会“刷分”而不是完成任务。 | 未讲 | 高 | | | |
| 1.4 | Agentic RL / Sample Efficiency | 一次代码修复或网页任务可能需要几十次真实执行，因此学习效率常受环境成本而非参数计算成本限制。 | 未讲 | 高 | | | |
| 1.5 | Agentic RL / Long-Horizon Optimization | 最终成功信号距离早期动作很远，且执行历史可能超过上下文窗口；训练还要保持各阶段策略的一致性。 | 未讲 | 高 | | | |
| 1.6 | Agentic RL / Generalization | 在训练网站成功的点击套路不等于理解新网站；需要区分真正可迁移的决策能力与对环境细节的记忆。 | 未讲 | 高 | | | |
| 1.7 | Agentic RL / Training Stability | Agent 训练常伴随稀疏奖励、长序列与行为分布变化，更新过激可能让原本有效的工具调用能力突然退化。 | 未讲 | 高 | | | |
| 2.1 | Test-Time Scaling / Reasoning / Compute Allocation | 简单问题无需反复思考，难题却可能需要验证和多轮搜索；核心是把有限推理预算花在最可能提高正确率的地方。 | 未讲 | — | | | |
| 2.2 | Test-Time Scaling / Reasoning / Reasoning Search | 单次生成容易过早走入错误分支；搜索路线会比较多种推理假设，但也会增加计算和选择难度。 | 未讲 | — | | | |
| 2.3 | Test-Time Scaling / Reasoning / Verification & Selection | 生成更多答案并不保证更准确；如果评分器偏好表面流畅而非真实正确，搜索可能反而放大错误。 | 未讲 | 高 | | | |
| 2.4 | Test-Time Scaling / Reasoning / Reasoning Efficiency | 推理越长不一定越好：重复分析与无效分支可能消耗大量 Token，却没有带来相应收益。 | 未讲 | — | | | |
| 2.5 | Test-Time Scaling / Reasoning / Error Correction | 关键不只是发现答案错了，还要找出错误起点，避免把整条推理重新生成一遍。 | 未讲 | 高 | | | |
| 2.6 | Test-Time Scaling / Reasoning / Reasoning Generalization | 模型在熟悉的数学题上有效的推理套路，可能在新领域或新组合问题中失效，因此要研究迁移边界。 | 未讲 | — | | | |
| 3.1 | Long-Horizon Agents / Task Decomposition | 例如“交付一个可运行网站”包含需求、接口、实现和测试；拆得太粗难执行，拆得太细会带来协调开销。 | 未讲 | — | | | |
| 3.2 | Long-Horizon Agents / State Tracking | 长期任务的上下文会逐步过期：已修改的文件、正在运行的流程和未完成的依赖都需要被准确跟踪。 | 未讲 | — | | | |
| 3.3 | Long-Horizon Agents / Error Propagation | 若第一阶段误读需求，后续生成代码与测试都会沿错误方向推进；因此需要尽早识别上游错误。 | 未讲 | 高 | | | |
| 3.4 | Long-Horizon Agents / Failure Recovery | 网页超时、工具失败或测试不通过不应意味着整项任务重来；应尽量只重做受影响部分。 | 未讲 | — | | | |
| 3.5 | Long-Horizon Agents / Context Management | 长任务积累的日志与观察会挤占模型上下文，需要在“信息完整性”和“可处理成本”之间权衡。 | 未讲 | 高 | | | |
| 3.6 | Long-Horizon Agents / Goal Consistency | Agent 可能在局部子目标上表现很好，却忘记最初的安全约束、验收标准或用户优先级。 | 未讲 | — | | | |
| 3.7 | Long-Horizon Agents / Execution Efficiency | 复杂任务中大量时间会花在重复搜索、重复验证或不必要的步骤上，需要优化执行路径而不只是提高单步能力。 | 未讲 | — | | | |
| 4.1 | Agent Memory / Memory Formation | 并非每句对话都应该永久记住；应优先保存未来可能影响行动的事实、偏好与经过验证的经验。 | 已讲（Agent Memory） | — | | | |
| 4.2 | Agent Memory / Memory Representation | 同一段经验可以存为原始日志、结构化事实或可执行技能；不同表示决定了能否高效检索和复用。 | 已讲（Agent Memory） | — | | | |
| 4.3 | Agent Memory / Memory Retrieval | “相似”不等于“有用”：当前任务也许更需要某次失败的原因，而不是语义最接近的一条历史记录。 | 已讲（Agent Memory） | — | | | |
| 4.4 | Agent Memory / Memory Consolidation | 长期交互会积累大量重复甚至矛盾的记录，需要从案例层逐渐形成更抽象、更省空间的知识。 | 已讲（Agent Memory） | — | | | |
| 4.5 | Agent Memory / Memory Updating & Forgetting | 用户偏好、项目状态、API 版本都可能改变；错误记忆若不更新，可能持续误导未来决策。 | 已讲（Agent Memory） | — | | | |
| 4.6 | Agent Memory / Memory Utilization | 检索到了正确记忆不代表决策一定改善，关键是如何把回忆转成规划约束、具体行动和工具选择。 | 已讲（Agent Memory） | — | | | |
| 4.7 | Agent Memory / Memory Evaluation | 单纯问模型“记不记得”不足以评价记忆系统；更关键的是它能否减少错误、缩短任务时间。 | 已讲（Agent Memory） | — | | | |
| 5.1 | Self-Evolving Agents / Experience Distillation | 一次成功执行只是具体案例；研究目标是提炼出在类似但不完全相同的任务里仍有用的策略。 | 未讲 | 高 | | | |
| 5.2 | Self-Evolving Agents / Skill Acquisition | 熟练技能应包含触发条件、执行步骤和终止条件，否则简单保存一段脚本很难安全泛化。 | 未讲 | 高 | | | |
| 5.3 | Self-Evolving Agents / Workflow Optimization | Agent 的 Prompt、工具顺序、验证节点都可以被自动搜索；问题在于怎样防止对少量训练任务过拟合。 | 未讲 | — | | | |
| 5.4 | Self-Evolving Agents / Self-Generated Learning Data | 人类标注与真实交互昂贵，因此尝试由 Agent 自动生成训练任务，但必须控制数据质量和难度。 | 未讲 | — | | | |
| 5.5 | Self-Evolving Agents / Continual Adaptation | 不断适应新任务容易损害旧能力；研究需要衡量新知识吸收速度与遗忘程度之间的权衡。 | 未讲 | 高 | | | |
| 5.6 | Self-Evolving Agents / Improvement Verification | 自我改进很容易出现“在自己设计的评测上越来越好”的假象，需要独立验证和回归测试。 | 未讲 | 高 | | | |
| 6.1 | Agentic Coding / Repository Understanding | 修一个 Bug 往往要理解接口、调用链和历史约定，单看报错附近的几行代码容易误判。 | 未讲 | — | | | |
| 6.2 | Agentic Coding / Code Localization | 定位错误位置与生成修复方案是不同问题；在大型仓库中找错文件往往会让后续生成全部失效。 | 未讲 | — | | | |
| 6.3 | Agentic Coding / Multi-File Editing | 改动一个函数可能破坏多个调用点；跨文件编辑需要同时维护接口、类型、测试和项目规范。 | 未讲 | — | | | |
| 6.4 | Agentic Coding / Automated Debugging | 测试失败只是症状，真正根因可能在另一层模块；因此调试需要提出假设并反复验证。 | 未讲 | — | | | |
| 6.5 | Agentic Coding / Code Verification | “编译通过”并不代表需求正确实现；还需检查边界条件、回归影响和潜在的隐藏测试。 | 未讲 | — | | | |
| 6.6 | Agentic Coding / Development Workflow Planning | 真实开发任务具有依赖：未明确接口就开始并行开发，可能造成大量返工和冲突。 | 未讲 | — | | | |
| 6.7 | Agentic Coding / Repository Generalization | 新仓库的语言、构建命令和约定都不同；好的 Agent 应先理解环境，再迁移一般性的开发技能。 | 未讲 | — | | | |
| 7.1 | Computer Use / GUI Agents / UI Perception | 截图既有文字也有布局和状态；若连当前页面包含什么都判断错误，后续点击将无从谈起。 | 未讲 | — | | | |
| 7.2 | Computer Use / GUI Agents / Visual Grounding | “点击提交按钮”需要精确对应真实元素；页面中可能存在多个同名按钮或动态移动的控件。 | 未讲 | — | | | |
| 7.3 | Computer Use / GUI Agents / Action Generation | 模型需要输出软件真正能执行的动作参数，并掌握操作顺序，例如先选中字段再输入。 | 未讲 | — | | | |
| 7.4 | Computer Use / GUI Agents / Partial Observability | 界面只展示部分环境状态，例如菜单未展开、任务还在后台加载，需要主动获得更多观察。 | 未讲 | — | | | |
| 7.5 | Computer Use / GUI Agents / Interaction Robustness | 视觉布局、弹窗和加载时间常常变化，固定坐标的开放环操作很容易失效。 | 未讲 | — | | | |
| 7.6 | Computer Use / GUI Agents / GUI Learning Efficiency | 录制高质量 GUI 操作数据非常昂贵，且真实网页具有随机性与副作用，训练需要更高效的数据来源。 | 未讲 | — | | | |
| 7.7 | Computer Use / GUI Agents / Cross-Application Generalization | 不同应用的“搜索、筛选、提交”外观不同，但具有共享的功能结构；泛化依赖这种抽象。 | 未讲 | — | | | |
| 8.1 | Multimodal / Embodied Agents / Multimodal Representation | 视觉、语言和动作的时间尺度与数据形态不同，必须学会在一个模型中对齐“看到了什么”和“该做什么”。 | 未讲 | — | | | |
| 8.2 | Multimodal / Embodied Agents / World Modeling | 行动前需要预测后果，例如机器人推动杯子后的位置；错误的预测可能直接造成任务失败。 | 未讲 | — | | | |
| 8.3 | Multimodal / Embodied Agents / Action Grounding | “把杯子放进盒子”是高层语言目标，实际执行需要连续的关节控制、抓取和放置动作。 | 未讲 | — | | | |
| 8.4 | Multimodal / Embodied Agents / Spatial & Temporal Reasoning | 物理操作依赖距离、相对位置、遮挡和时间变化，纯文本推理无法完整表达这些约束。 | 未讲 | — | | | |
| 8.5 | Multimodal / Embodied Agents / Embodied Planning | 任务顺序与运动可达性必须同时满足，例如抓取前要先移动到合适位置。 | 未讲 | — | | | |
| 8.6 | Multimodal / Embodied Agents / Sim-to-Real Generalization | 仿真中的摩擦、光照、传感器噪声与真实世界不同，直接迁移经常失败。 | 未讲 | — | | | |
| 8.7 | Multimodal / Embodied Agents / Data Efficiency | 真实机器人采样速度慢、成本高，如何从少量演示与无标签数据中学习十分关键。 | 未讲 | — | | | |
| 9.1 | Multi-Agent Systems / Task Allocation | 不同 Agent 能力、成本和工具权限不同；合理分工能提效，但错误分工会增加沟通与返工。 | 未讲 | — | | | |
| 9.2 | Multi-Agent Systems / Coordination | 多个 Agent 可能同时修改同一文件、重复执行任务或相互等待，需要明确协调机制。 | 未讲 | — | | | |
| 9.3 | Multi-Agent Systems / Communication Efficiency | 多 Agent 系统中的消息常比实际执行还昂贵；研究如何仅传递对下游决策有用的信息。 | 未讲 | — | | | |
| 9.4 | Multi-Agent Systems / Collective Decision-Making | 多个 Agent 同意某个答案不一定代表正确，尤其当它们共享同一模型偏差时。 | 未讲 | — | | | |
| 9.5 | Multi-Agent Systems / Multi-Agent Credit Assignment | 团队成功后如何奖励贡献大的 Agent，尤其在多个成员互相依赖时，是协作学习中的难题。 | 未讲 | 高 | | | |
| 9.6 | Multi-Agent Systems / Scalability | Agent 越多并不一定越快，通信量与协调冲突可能随规模迅速增长。 | 未讲 | — | | | |
| 9.7 | Multi-Agent Systems / Cooperation Robustness | 一个执行者给出错误中间结果，可能使下游多个 Agent 全部偏离目标，因此需要隔离和恢复机制。 | 未讲 | — | | | |
| 9.8 | Multi-Agent Systems / Collaboration Benefit | 多 Agent 带来额外 Token、延迟与管理成本；只有协作收益高于额外开销才值得使用。 | 未讲 | — | | | |
| 10.1 | Agent Infrastructure / MCP / A2A / Tool Discovery | 当工具数量从几个增加到几百个时，全部塞进 Prompt 不现实，Agent 需要先发现有用工具。 | 未讲 | — | | | |
| 10.2 | Agent Infrastructure / MCP / A2A / Tool Selection & Routing | 找到多个可用工具后，还需要权衡权限、可靠性、成本和任务约束，选错会导致失败或浪费。 | 未讲 | — | | | |
| 10.3 | Agent Infrastructure / MCP / A2A / Interface Interoperability | 不同工具接口格式不一致，跨平台调用容易出错；标准协议改善连接方式，但不自动保证任务成功。 | 未讲 | — | | | |
| 10.4 | Agent Infrastructure / MCP / A2A / Workflow Orchestration | 一个工作流可能需要审批、等待网页事件和并行执行，不能仅靠顺序调用串起来。 | 未讲 | — | | | |
| 10.5 | Agent Infrastructure / MCP / A2A / State & Session Management | 任务可能跨会话、跨机器运行；如果没有可靠状态，重启之后 Agent 就无法知道已经做过什么。 | 未讲 | — | | | |
| 10.6 | Agent Infrastructure / MCP / A2A / Fault Tolerance | 第三方服务超时或只执行了一半会留下副作用，恢复逻辑需要避免重复付款、重复发信等问题。 | 未讲 | — | | | |
| 10.7 | Agent Infrastructure / MCP / A2A / Cost & Latency Optimization | 每一次模型和工具调用都会产生实际成本，因此需要把成功率、延迟和费用一起优化。 | 未讲 | — | | | |
| 11.1 | Agent Evaluation / Task Success Measurement | Agent 的自然语言自述不能作为成功证据；例如“邮件已发送”必须与真实系统状态相核对。 | 未讲 | — | | | |
| 11.2 | Agent Evaluation / Process Evaluation | 两个 Agent 最终都成功，却可能采用完全不同的风险、成本和步骤；过程评测能识别这种差异。 | 未讲 | 高 | | | |
| 11.3 | Agent Evaluation / Benchmark Realism | 过于理想化的静态题目会高估真实能力；真实场景往往包含动态页面、歧义与失败恢复。 | 未讲 | — | | | |
| 11.4 | Agent Evaluation / Evaluation Reliability | 环境随机性和 Judge 偏差会使同一系统在不同评测轮次得到不同结果，需要统计稳健性。 | 未讲 | — | | | |
| 11.5 | Agent Evaluation / Generalization Evaluation | 只在训练环境成功并不代表可部署，评测应使用未见过的工具、任务组合和环境扰动。 | 未讲 | — | | | |
| 11.6 | Agent Evaluation / Long-Horizon Evaluation | 长任务的失败概率会随着步骤增加而累积，需要考察成功率随任务长度的变化及恢复能力。 | 未讲 | — | | | |
| 11.7 | Agent Evaluation / Efficiency Evaluation | 只比较成功率容易让高成本系统占优；评价真实可用性时必须把时间与费用纳入。 | 未讲 | — | | | |
| 12.1 | Agent Safety / Security / Prompt Injection Robustness | 网页或文档中的文字只是待处理数据，不能自动升级为高权限命令，这是防范指令注入的核心。 | 未讲 | — | | | |
| 12.2 | Agent Safety / Security / Permission & Access Control | Agent 获得邮箱、文件和支付权限后，权限边界必须比普通问答系统更明确。 | 未讲 | — | | | |
| 12.3 | Agent Safety / Security / Action Safety | 错误回答可以修改，删除数据或付款则可能不可逆，因此安全校验需要发生在行动之前。 | 未讲 | — | | | |
| 12.4 | Agent Safety / Security / Trustworthy Tool Use | 工具返回既可能有错误，也可能包含恶意内容；还需防止敏感信息被发送到不可信服务。 | 未讲 | — | | | |
| 12.5 | Agent Safety / Security / Runtime Monitoring | 仅靠事前规则不足以发现复杂任务中的新风险，需要沿执行轨迹持续监控。 | 未讲 | — | | | |
| 12.6 | Agent Safety / Security / Adversarial Robustness | 攻击者会改变措辞、界面和工具反馈，因此安全评估不能只看少量固定攻击样例。 | 未讲 | — | | | |
| 12.7 | Agent Safety / Security / Controllability & Oversight | 即使 Agent 能自主执行，也必须允许人类随时检查、纠正、暂停，并能追溯关键决策。 | 未讲 | — | | | |

## 候选（图谱之外的新方向）

| 方向 | 为什么值得关注 | 来源 | 加入日期 |
|---|---|---|---|
| （由刷新流程填写） | | | |