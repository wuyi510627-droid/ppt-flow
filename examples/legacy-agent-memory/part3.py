from common import *
import math
# ---- 25 目录 四
toc(CH,3)

# ---- 26 评测范式
sl=newslide('评测范式：固定其他一切，只换记忆模块','04 · 评测与实验范式 · 范式',footer=False)
items=[('多会话历史 + 问题','输入',GREEN,False),('记忆系统','写 · 管 · 读',BROWN,True),('回答模型','基座 LLM',GREEN,False),('打分','答案 / 任务结果',GREEN,False)]
for i,(t,d,c,var) in enumerate(items):
    x=64+i*208; w=180
    if var:
        shape(sl,x-5,104,w+10,76,line=BROWN,lw=1.25,dash=True,adj=6000)
        chip(sl,x+50,96,80,17,'唯一变量','FFFFFF',fg=BROWN,sz=11,line=BROWN)
        box(sl,x,112,w,60,[([R(t,15,'FFFFFF',True)],0),([R(d,12,'FFFFFF')],2)],fill=BROWN,line=None)
    else:
        chip(sl,x+68,98,44,16,'固定',GL,fg=GREEN,sz=11,line=GREEN)
        box(sl,x,116,w,56,[([R(t,15,TXT,True)],0),([R(d,12,GR)],2)],fill=CARD,line=CB)
    if i>0: arrow(sl,x-26,142,x-2,142,c=BROWN if i in (1,2) else GRAY,lw=2)
# 三块
def pnl(x,col,title):
    shape(sl,x,190,270,262,fill='FFFFFF',line=CB,lw=0.75,adj=3000)
    shape(sl,x,190,270,28,fill=col,paras=[([R(title,15,'FFFFFF',True)],0)],anchor='ctr',ins=10,adj=0,prst='rect')
pnl(64,GREEN,'① 在哪测：基准数据'); pnl(345,BROWN,'② 和谁比：对比阶梯'); pnl(626,BLUE,'③ 测什么：五类指标')
for i,(c,t,d) in enumerate([(BLUE,'LoCoMo','超长多会话对话，问答等三类任务'),(PURPLE,'LongMemEval','500 题，5 种长期记忆能力'),(BROWN,'CL-Bench','跨会话学习，仅记忆目录留存'),(GREEN,'MemBench 等三个','MemoryAgentBench · MemoryArena')]):
    box(sl,74,224+i*56,250,50,[([R(t,14,c,True)],0),([R(d,12,GR)],2)],fill=CARD,line=c,lw=1)
bars=[('无记忆',36,'C9C9C9'),('全上下文',56,'B9C49C'),('检索',76,'8FA36A'),('记忆系统',96,GREEN),('学习式',116,BROWN)]
for i,(t,h,c) in enumerate(bars):
    x=356+i*50
    shape(sl,x,372-h,42,h,fill=c,prst='rect')
    text(sl,x-5,372-h-30,52,28,[([R(t,11,TXT,True)],0)],algn='ctr',anchor='b')
shape(sl,354,372,246,1,fill=GRAY,prst='rect')
text(sl,354,375,250,16,[([R('越往右：越多机制 → 增益该归因给谁？',11,GRAY)],0)],algn='ctr')
box(sl,355,398,250,46,[([R('消融：去掉记忆模块，增益还在吗？',14,BROWN,True)],0)],fill=CREAM,line=BROWN)
M5=[(GREEN,'召回','历史事实问答、事件排序',None),(BLUE,'任务收益','有无记忆的成功率、成本、错误','核心'),(BLUE,'跨会话','信息散在不同会话，再使用',None),(BLUE,'记忆消融','去掉某类记忆看边际作用',None),(RED,'鲁棒与过期','故意加入陈旧、冲突、错误记忆','最易忽略')]
for i,(c,t,d,tag) in enumerate(M5):
    y=224+i*44
    box(sl,636,y,250,38,[([R(t,14,c,True),R('  '+d,11,GR)],0)],fill=RL if c==RED else (BL if c==BLUE else GL),line=c,lw=1.25 if tag else 0.75,algn='l',ins=8)
    if tag: chip(sl,820,y-6,60,15,tag,c,sz=10)
banner(sl,64,458,832,34,[([R('「记得住」≠「用得好」：',14,GOLD,True),R('高召回率不直接代表决策受益；好的实验固定其他一切，只替换记忆模块',14,'FFFFFF')],0)])

# ---- 27 基准
sl=newslide('常用基准：输入、任务与指标','04 · 评测与实验范式 · 基准',footer=False)
table_header(sl,40,98,880,[(48,120,'基准'),(172,200,'输入（数据）'),(376,240,'任务 / 测什么'),(620,296,'规模与发现')])
BM=[(BLUE,'LoCoMo','arXiv:2402.17753','超长多会话对话：平均约 300 轮、9K token，最多 35 个会话；人设与事件图生成，人工校对','问答、事件摘要、多模态对话生成','LLM 在长对话与时间、因果关系上吃力；长上下文与 RAG 有帮助，但仍远不及人'),
    (PURPLE,'LongMemEval','arXiv:2410.10813（ICLR 2025）','嵌入长度可扩展的用户-助手对话历史','5 种能力：信息抽取、多会话推理、时间推理、知识更新、拒答','500 题；商用助手与长上下文 LLM 的准确率约下降 30%；另提出索引-检索-阅读三阶段框架'),
    (BROWN,'CL-Bench 1.0 数据库任务','Anthropic 文章','每道题一个新会话，只有记忆目录跨会话保存','连续回答问题；答完被告知正确解，并可写记忆','指标：平均奖励；比较同一模型有无记忆（见下页）'),
    (GREEN,'其他三个基准','2603.07670 分析','MemBench · MemoryAgentBench · MemoryArena','—','该综述把它们与 LoCoMo 一起作为评测分析对象；本讲未逐一核对')]
for i,(c,n,src,inp,task,note) in enumerate(BM):
    y=126+i*80
    shape(sl,40,y,880,76,fill='FFFFFF' if i%2==0 else CARD,line=CB,lw=0.5,adj=4000)
    shape(sl,40,y,6,76,fill=c,prst='rect')
    text(sl,52,y+6,118,64,[([R(n,13,c,True)],0),([R(src,10,GRAY)],3)])
    text(sl,172,y+6,200,66,[([R(inp,12,TXT)],0)])
    text(sl,376,y+6,240,66,[([R(task,12,TXT)],0)])
    text(sl,620,y+6,292,66,[([R(note,12,GR)],0)])
banner(sl,40,452,880,40,[([R('怎么选：',14,GOLD,True),R('关心「记得住」看 LoCoMo、LongMemEval；关心「用得好」看任务收益与跨会话表现（如 CL-Bench）',14,'FFFFFF')],0)])

# ---- 28 结果与局限
sl=newslide('评测结果与基准自身的局限','04 · 评测与实验范式 · 结果',footer=False)
panel(sl,40,100,520,300,None)
pic(sl,'chart_clbench.png',(46,106,508,288))
shape(sl,572,100,348,146,fill=CARD,line=GREEN,lw=1.25,adj=4000)
text(sl,582,106,328,20,[([R('数字说明什么（Anthropic）',15,GREEN,True)],0)])
text(sl,582,130,328,112,[([R('• 五款模型有记忆后提升 0.18–0.32',13,TXT)],0),([R('• Sonnet 4.6 只提升 0.034（0.330→0.364）；加上调整过的提示后到 0.641',13,TXT)],3),([R('• Opus 5.5、Sonnet 5.5 有记忆时与 Opus 5 接近，但无记忆基线略高',13,TXT)],3)])
shape(sl,572,254,348,146,fill=CARD,line=BROWN,lw=1.25,adj=4000)
text(sl,582,260,328,20,[([R('基准自身的问题（2602.19320）',15,BROWN,True)],0)])
text(sl,582,284,328,112,[([R('• 基准过小或已饱和',13,TXT)],0),([R('• 指标与语义上的「有用」不一致',13,TXT)],3),([R('• 对评审模型敏感、依赖骨干模型',13,TXT)],3),([R('• 系统开销常被忽略',13,TXT)],3)])
banner(sl,40,410,880,40,[([R('讨论：',14,GOLD,True),R('同样给了记忆目录，增益差别很大——评测要把「有没有记忆」和「模型会不会用记忆」分开看',14,'FFFFFF')],0)])
banner(sl,40,458,880,34,[([R('注：数字来自 Anthropic 文章；其余模型的提示与设置请以原文为准',13,BROWN,True)],0)],fill=CREAM)

# ---- 29 目录 五
toc(CH,4)

# ---- 30 开放问题
sl=newslide('开放问题','05 · 开放问题与总结',footer=False)
OP=[(BROWN,'① 何时写','现场写，还是事后 dreaming？各有利弊（Anthropic）'),
    (BLUE,'② 如何保鲜','重点整理易变的信息？按访问频率调节 dreaming 的频率？'),
    (PURPLE,'③ 转录日志做底层吗','把转录日志检索当作记忆的基础，是否更合理？'),
    (GREEN,'④ 表示不积累错误','wiki 等表示如何避免累积错误与幻觉？需要持续算力'),
    (RED,'⑤ 写入的信用分配','写入、更新的回报延迟而稀疏；奖励要兼顾容量、成本与错误写入'),
    ('3F6680','⑥ 评测与安全','基准不统一、易饱和；记忆投毒等威胁贯穿写入到遗忘回滚六个阶段')]
for i,(c,t,d) in enumerate(OP):
    left=(i<3); x=40 if left else 580; y=100+(i%3)*108
    shape(sl,x,y,340,98,fill=CARD,line=c,lw=1.25,adj=5000)
    circ(sl,x+10,y+10,26,str(i+1),c,13)
    text(sl,x+44,y+10,288,22,[([R(t[2:],16,c,True)],0)])
    text(sl,x+12,y+42,316,52,[([R(d,13,TXT)],0)])
cx,cy=480,254
shape(sl,cx-82,cy-82,164,164,fill=GREEN,prst='ellipse',paras=[([R('Agent Memory',15,'FFFFFF',True)],0),([R('仍待解决',15,'FFFFFF',True)],2),([R('的问题',13,GOLD)],2)],algn='ctr',anchor='ctr')
for i in range(6):
    left=(i<3); y=149+(i%3)*108
    px,py=(380,y) if left else (580,y)
    ex=(cx-72 if left else cx+72); ey=cy+(y-254)*0.45
    line(sl,px,py,ex,ey,c='9AAF6A',lw=1.25,dash=True)
banner(sl,40,430,880,52,[([R('综述提到的延伸方向：',14,BROWN,True),R('记忆自动化、与 RL 结合、多模态、多智能体、可信性（2512.13564）；以及与自进化 agent 的关系——经验蒸馏、技能获取（PDF 第 5 章）',14,TXT)],0)],fill=CREAM)

# ---- 31 总结
sl=newslide('总结：存什么、怎么存、怎么用','05 · 总结',footer=False)
COL=[(BLUE,'① 存什么 · 形成','写的时候不知道以后什么重要',['现场写：信息鲜活，但看不到结局','事后写（dreaming）：知道结局，要算力'],['Generative Agents','Reflexion']),
     (PURPLE,'② 怎么存 · 表示 / 巩固 / 更新','表示决定能否检索与复用',['技能、分层、图、链接笔记','用转录日志检验笔记；带时间更新，不直接覆盖'],['Voyager','MemGPT','Zep','A-MEM','dreaming']),
     (BROWN,'③ 怎么用 · 检索 / 利用','相似不等于有用',['取到之后还要真正改善决策','评估看任务收益，而不只是召回'],['Mem0','Reflexion','Voyager'])]
for i,(c,t,k,ds,ms) in enumerate(COL):
    x=40+i*300; w=280
    shape(sl,x,100,w,246,fill=CARD,line=c,lw=1.25,adj=3000)
    shape(sl,x,100,w,30,fill=c,paras=[([R(t,14,'FFFFFF',True)],0)],algn='ctr',anchor='ctr',adj=0,prst='rect')
    text(sl,x+12,138,w-24,40,[([R(k,15,c,True)],0)])
    text(sl,x+12,174,w-24,120,[([R('• '+d,13,TXT)],3) for d in ds])
    cx_=x+12; cy_=290
    for m in ms:
        tw=len(m)*8+22
        if cx_+tw>x+w-8: cx_=x+12; cy_+=26
        chip(sl,cx_,cy_,tw,22,m,'FFFFFF',fg=c,sz=11,line=c); cx_+=tw+6
    if i<2: arrow(sl,x+w+2,232,x+w+18,232,c=GRAY,lw=2)
shape(sl,40,354,880,104,fill=CREAM,line=BROWN,lw=1,adj=5000)
text(sl,54,360,852,96,[([R('三个要点',14,BROWN,True)],0),
   ([R('① 难在写的时候不知道以后什么重要，所以要事后用日志检验（dreaming）',13,TXT)],3),
   ([R('② 不同综述的切法不同：先看它按什么轴切，再对比方法',13,TXT)],2),
   ([R('③ 评测看任务收益而非召回；学习式管理让写入、更新、检索可训练，也带来延迟奖励的归因问题',13,TXT)],2)])
banner(sl,40,466,880,32,[([R('一句话：记忆不是「存下来」就完事，而是「存什么、怎么整理、怎么用」一整条链路',14,'FFFFFF',True)],0)],anchor='ctr')

# ---- 32 参考文献
sl=newslide('参考文献','附录')
def est(t,w):
    u=sum(14 if ord(ch)>255 else 7.6 for ch in t); return max(1,math.ceil(u/w))
L=['Anthropic (Lance Martin). The components of agent memory. 2026-11-06.',
   'Memory in the Age of AI Agents（综述）. arXiv:2512.13564.',
   'Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers（综述）. arXiv:2603.07670.',
   'Anatomy of Agentic Memory: Taxonomy and Empirical Analysis of Evaluation and System Limitations. arXiv:2602.19320.',
   'Rethinking Memory in LLM based Agents. arXiv:2505.00675.',
   'From Human Memory to AI Memory. arXiv:2504.15965.',
   'A Survey on Long-Term Memory Security in LLM Agents. arXiv:2604.16548.',
   'Lin et al. Sleep-time Compute. arXiv:2504.13171.']
Rr=['Park et al. Generative Agents. arXiv:2304.03442.   Shinn et al. Reflexion. arXiv:2303.11366.',
    'Wang et al. Voyager. arXiv:2305.16291.   Packer et al. MemGPT. arXiv:2310.08560.',
    'Rasmussen et al. Zep. arXiv:2501.13956.   Xu et al. A-MEM. arXiv:2502.12110.',
    'Chhikara et al. Mem0. arXiv:2504.19413.',
    'Yan et al. Memory-R1. arXiv:2508.19828.   Yu et al. AgeMem. arXiv:2601.01885.   Zhang et al. MemRL. arXiv:2601.03192.',
    'Maharana et al. LoCoMo. arXiv:2402.17753.   Wu et al. LongMemEval. arXiv:2410.10813（ICLR 2025）.',
    'LLM Agent 技术路线整理（第 4 章 Agent Memory，4.1–4.7）.']
for col,lst in [(64,L),(490,Rr)]:
    y=102
    for t in lst:
        n=est(t,400); h=n*19+2
        text(sl,col,y,406,h,[([R(t,13,TXT)],0)]); y+=h+4
# ---- 33 谢谢
thanks()
