from common import *

# ---- 1 封面 / 2 目录
cover('Agent Memory：存什么、怎么存、怎么用','2026.11.12')
CH=['一、研究背景','二、记忆的分类','三、各环节的代表工作','四、评测与实验范式','五、开放问题与总结']
toc(CH,0)

# ---- 3 例子引入
sl=newslide('研究背景：从编程 agent 的「失忆」说起','01 · 研究背景 · 一个例子',footer=False)
banner(sl,64,100,832,30,[([R('周一用户告诉编程 agent「本项目用 pnpm，别用 npm」；周五再来说：',14,TXT),R('「再帮我加一个依赖」',14,RED,True)],0)],fill=CREAM)
def lane(x,col,light,name,tag,s1,s2,mid,res):
    shape(sl,x,138,412,222,fill=CARD,line=col,lw=1.5,adj=3000)
    shape(sl,x,138,412,26,fill=col,paras=[([R(name,15,'FFFFFF',True)],0)],anchor='ctr',ins=10,adj=12000)
    for k,(bx,t1,t2) in enumerate([(x+10,'周一 · 会话 1',s1),(x+214,'周五 · 会话 2',s2)]):
        box(sl,bx,172,188,114,[([R(t1,12,GRAY,True)],0)]+[([R(a,14,b2,bb)],3) for a,b2,bb in t2],algn='l',anchor='t',ins=8,line=CB)
    arrow(sl,x+200,228,x+212,228,c=col,lw=2)
    box(sl,x+10,290,392,26,[([R(mid,14,col,True)],0)],fill=light,line=col,lw=0.75,adj=20000)
    box(sl,x+10,320,392,34,[([R(res,14,TXT,True)],0)],fill='FFFFFF',line=col,lw=0.75,algn='l',ins=8)
lane(64,RED,RL,'没有记忆','',
     [('用户：「用 pnpm，别用 npm」',TXT,False),('→ 用 pnpm 装好 ✓',GREEN,True)],
     [('不知道约定，默认 npm install ✗',RED,True),('用户只好再说一遍',TXT,False)],
     '会话结束，上下文清空 ✗','结果：每次从零开始，约定反复重说，还会弄乱项目')
lane(484,GREEN,GL,'有记忆','',
     [('用户：「用 pnpm，别用 npm」',TXT,False),('→ 用 pnpm 装好 ✓',GREEN,True),('结束前写下一条笔记',BROWN,True)],
     [('开头读到笔记：用 pnpm',BROWN,True),('→ 直接 pnpm add ✓',GREEN,True)],
     '笔记：「用 pnpm，禁用 npm」→ 跨会话保留','结果：第二次直接做对，不用再交代')
# 三个问题
for i,(c,t,d) in enumerate([(BLUE,'记下什么？','项目约定值得记；一次性的报错输出不必记'),(PURPLE,'怎么存？','一条短笔记？向量库？图？存多久、错了怎么改'),(BROWN,'怎么用？','新会话开头读到，还是需要时再去检索')]):
    x=64+i*280
    shape(sl,x,368,272,76,fill='FFFFFF',line=c,lw=1.25,adj=6000)
    text(sl,x+10,372,252,20,[([R(['存什么','怎么存','怎么用'][i]+' · '+t,15,c,True)],0)])
    text(sl,x+10,396,252,48,[([R(d,14,GR)],0)])
banner(sl,64,452,832,40,[([R('同一个 agent、同一个用户，差别只在「上一次的经验有没有留下来」——这就是 agent memory 要解决的问题',14,'FFFFFF',True)],0)])

# ---- 4 定义
sl=newslide('研究背景：什么是 Agent Memory','01 · 研究背景 · 概念界定',footer=False)
banner(sl,64,100,832,48,[([R('定义（Anthropic）：',14,GOLD,True),R('agent 从经验（用户交互、被分配的任务）中获得，并在会话之间保留、以后可以读取的上下文',14,'FFFFFF')],0)])
cols=[(70,150,'概念'),(226,110,'保存多久'),(342,150,'谁来写'),(498,390,'与 agent memory 的关系')]
table_header(sl,64,156,832,cols)
rows=[('上下文窗口','单次会话内','随对话自然累积','含上下文学习；会话结束就没了，Anthropic 不算',GRAY),
      ('压缩 compaction','同一任务内','模型把旧轮次写成摘要','只为腾出窗口，不跨会话；Anthropic 不算',GRAY),
      ('参数更新（改权重）','永久','训练','Anthropic 不算；综述 2512.13564 归为「参数化记忆」',GRAY),
      ('检索增强 RAG','跨会话','多由人准备资料','外部知识库；记忆是 agent 自己从经验里写出来的（概括）',BLUE),
      ('agent memory','跨会话','agent 自己','经验 → 写入 → 以后读取：前三类都不是它',GREEN)]
for i,(a,b,c,d,col) in enumerate(rows):
    y=184+i*37; last=(i==4)
    shape(sl,64,y,832,35,fill=GL if last else ('FFFFFF' if i%2==0 else CARD),line=CB,lw=0.5,adj=6000)
    text(sl,70,y+4,150,28,[([R(a,14,col if last else TXT,True)],0)],anchor='ctr')
    text(sl,226,y+4,110,28,[([R(b,14,GR)],0)],anchor='ctr')
    text(sl,342,y+4,150,28,[([R(c,14,GR)],0)],anchor='ctr')
    text(sl,498,y+4,394,28,[([R(d,14,GR if not last else GREEN,last)],0)],anchor='ctr')
# 图：三次会话 + 记忆条
text(sl,64,376,400,18,[([R('示意：窗口只管一次会话，记忆跨会话保留',14,GREEN,True)],0)])
for i in range(3):
    x=64+i*214
    box(sl,x,398,196,40,[([R(f'会话 {i+1}',14,TXT,True),R('  上下文窗口',12,GRAY)],0)],fill='FFFFFF',line=GRAY,dash=True)
shape(sl,64,458,832,30,fill=GL,line=GREEN,lw=1.25,paras=[([R('记忆：跨会话保留，下一次会话开头可以读取',14,GREEN,True)],0)],algn='ctr',anchor='ctr',adj=20000)
arrow(sl,162,438,162,456,c=BROWN,lw=2); text(sl,168,440,60,16,[([R('写入',12,BROWN,True)],0)])
arrow(sl,590,456,590,438,c=GREEN,lw=2); text(sl,596,440,60,16,[([R('读取',12,GREEN,True)],0)])

# ---- 5 为什么难
sl=newslide('研究背景：为什么难——写的时候不知道以后什么重要','01 · 研究背景 · 核心难点',footer=False)
banner(sl,64,100,832,36,[([R('核心难点（Anthropic）：',14,BROWN,True),R('写记忆的时刻，模型并不知道后面几轮会发生什么，也就不知道哪条信息以后有用',14,TXT)],0)],fill=CREAM)
cards=[(RED,RL,'写入','不确定','现场就得判断「什么值得记」，但此时没有后续信息；记多了是噪声，记少了会漏掉关键事实','形成'),
       (BLUE,BL,'错误','笔记可能一开始就错','错误的预测或规则一旦存下，之后会被当作事实信任，并反复误导决策','巩固 · 校对'),
       (PURPLE,PL,'漂移','记忆会过期','用户偏好、项目状态、环境都会变；旧笔记不更新就会和现实脱节','更新与遗忘'),
       (BROWN,'F8EFE6','成本','注意力与算力','现场记笔记会分散主任务的注意力；事后整理要额外算力，不可能时刻检查全部记忆','权衡')]
for i,(c,l,tag,head,desc,pill) in enumerate(cards):
    x=64+(i%2)*424; y=146+(i//2)*150
    shape(sl,x,y,408,142,fill=l,line=c,lw=1.25,adj=4000)
    shape(sl,x+12,y+10,56,24,fill=c,paras=[([R(tag,13,'FFFFFF',True)],0)],algn='ctr',anchor='ctr',adj=20000)
    text(sl,x+78,y+10,320,24,[([R(head,17,c,True)],0)],anchor='ctr')
    text(sl,x+12,y+42,384,64,[([R(desc,14,TXT)],0)])
    chip(sl,x+260,y+112,136,22,'对应：'+pill,c,sz=12)
banner(sl,64,452,832,42,[([R('例：玩《Pokémon Red》时，一条错记精灵中心位置的笔记，让 agent 在月见山反复掉下悬崖',14,'FFFFFF',True)],0)])

# ---- 6 全文地图
sl=newslide('本讲地图：存什么、怎么存、怎么用','01 · 研究背景 · 记忆的生命周期',footer=False)
for i,(c,t) in enumerate([(BLUE,'存什么'),(PURPLE,'怎么存'),(BROWN,'怎么用')]):
    chip(sl,64+i*112,98,100,22,t,c,sz=13)
text(sl,400,99,500,20,[([R('六个环节 ↔ 三个问题；每个环节都有「它要回答的问题」',13,GRAY)],0)])
def stage(x,y,w,h,c,name,q):
    shape(sl,x,y,w,h,fill=CARD,line=c,lw=1.5,adj=5000)
    shape(sl,x,y,w,28,fill=c,paras=[([R(name,16,'FFFFFF',True)],0)],algn='ctr',anchor='ctr',adj=14000)
    text(sl,x+8,y+34,w-16,h-38,[([R(q,14,TXT)],0)])
stage(64,134,190,96,BLUE,'形成','哪些经历值得记？什么时候写？')
stage(278,134,290,96,PURPLE,'表示（记忆库）','以什么形式存：文本、结构化、图、技能、分层？')
stage(592,134,140,96,BROWN,'检索','相似不等于有用，怎么取到真正有用的？')
stage(756,134,140,96,BROWN,'利用','取到了，怎么真正改善决策？')
for x1,x2 in [(254,278),(568,592),(732,756)]: arrow(sl,x1,182,x2,182,c=GRAY,lw=2)
stage(278,262,140,100,PURPLE,'巩固','零散经历怎么变成可复用知识？')
stage(428,262,140,100,PURPLE,'更新与遗忘','过期、错误、矛盾的记忆怎么办？')
arrow(sl,348,262,348,232,c=PURPLE,lw=2); arrow(sl,498,262,498,232,c=PURPLE,lw=2)
text(sl,282,366,290,16,[([R('维护记忆库（离线或在线）',12,GRAY)],0)],algn='ctr')
# 回流
line(sl,826,230,826,250,c=GRAY,lw=1.5); line(sl,826,250,159,250,c=GRAY,lw=1.5,dash=True); arrow(sl,159,250,159,232,c=GRAY,lw=1.5,dash=True)
text(sl,596,252,230,16,[([R('新经验回流',12,GRAY,True)],0)],algn='r')
# 章节对应
box(sl,596,268,300,94,[([R('章节对应',14,GREEN,True)],0),([R('第二章  记忆的分类',13,GR)],3),([R('第三章  六个环节的代表工作',13,GR)],2),([R('第四章  评测    第五章  开放问题',13,GR)],2)],fill='FFFFFF',line=CB,algn='l',anchor='t',ins=10)
banner(sl,64,388,832,48,[([R('贯穿线：',14,GOLD,True),R('写入、管理、检索这些决策，能不能不靠手写规则，而是被训练出来？（学习式控制，第 23 页）',14,'FFFFFF')],0)])
banner(sl,64,446,832,44,[([R('口径：',14,BROWN,True),R('Anthropic 只把「可读取的上下文」算作记忆；综述把参数化、潜在也算进来。本讲主要讲前者，第 9 页会再对比',14,TXT)],0)],fill=CREAM)

# ---- 7 目录 二
toc(CH,1)

# ---- 8 综述怎么分
sl=newslide('记忆的分类：综述怎么切','02 · 记忆的分类 · 三个主要视角',footer=False)
def surv(x,w,col,tag,title,rows):
    shape(sl,x,100,w,262,fill=CARD,line=CB,lw=0.5,adj=3000)
    shape(sl,x,100,w,50,fill=col,adj=8000)
    text(sl,x+10,103,w-20,18,[([R(tag,12,GOLD,True)],0)])
    text(sl,x+10,121,w-20,24,[([R(title,13 if len(title)>30 else 15,'FFFFFF',True)],0)])
    y=156
    for lab,items in rows:
        text(sl,x+10,y,w-20,18,[([R(lab,13,col,True)],0)])
        cx=x+10; cy=y+20
        for it in items:
            tw=len(it)*13+16
            if cx+tw>x+w-6: cx=x+10; cy+=24
            chip(sl,cx,cy,tw,20,it,'FFFFFF',fg=col,sz=12,line=col)
            cx+=tw+6
        y=cy+30
surv(64,270,BLUE,'2512.13564','Memory in the Age of AI Agents',[('形式：记忆存在哪',['token 级','参数化','潜在']),('功能：为什么要记',['事实','经验','工作记忆']),('动态：怎么运转',['形成','演化','检索'])])
surv(346,270,PURPLE,'2603.07670','Memory for Autonomous LLM Agents',[('时间范围',['工作','情景','语义','程序']),('载体',['上下文文本','向量库','结构化存储','可执行库','混合']),('控制策略',['启发式','提示自控','学习式'])])
surv(628,268,BROWN,'2602.19320','Anatomy of Agentic Memory',[('四种结构',['轻量语义','实体中心','情景·反思','结构化·分层'])])
text(sl,638,236,250,80,[([R('按「记忆在系统里怎么组织」来切，再逐类分析基准与系统的局限',14,GR)],0),([R('→ 下一页展开这四类',14,BROWN,True)],6)])
for i,(tag,t,d) in enumerate([('2505.00675','Rethinking Memory in LLM based Agents','按载体（参数化 / 上下文）切；6 种操作：巩固、更新、索引、遗忘、检索、压缩'),('2504.15965','From Human Memory to AI Memory','类比人类记忆：对象 × 形式 × 时间，共 8 个象限')]):
    x=64+i*424
    box(sl,x,368,408,66,[([R(tag+'  ',12,GREEN,True),R(t,13,TXT,True)],0),([R(d,13,GR)],2)],algn='l',anchor='ctr',ins=10,line=CB)
for x,w_,t in [(74,250,'另有资源与框架、前沿讨论两章'),(356,250,'另有评测、工程现实、开放挑战'),]:
    text(sl,x,336,w_,16,[([R(t,12,GRAY)],0)])
banner(sl,64,442,832,50,[([R('怎么切取决于看哪个轴：',14,GOLD,True),R('存在哪（形式）、记来干什么（功能）、怎么组织（结构）、怎么管（控制）。本讲按生命周期组织，方便对应「存什么、怎么存、怎么用」',14,'FFFFFF')],0)])
