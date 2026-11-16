from common import *

# ---- 9 按形式
sl=newslide('按「形式」分：记忆存在哪','02 · 记忆的分类 · 综述 2512.13564',footer=False)
def fcard(x,w,col,title,drawfn,subs,feat):
    shape(sl,x,100,w,336,fill=CARD,line=CB,lw=0.5,adj=3000)
    shape(sl,x,100,w,28,fill=col,paras=[([R(title,15,'FFFFFF',True)],0)],algn='ctr',anchor='ctr',adj=10000)
    drawfn(x,w)
    ps=[]
    for a,b in subs: ps.append(([R(a,13,col,True),R(b,13,TXT)],3))
    text(sl,x+10,226,w-20,110,ps)
    shape(sl,x+8,342,w-16,86,fill=GL if col==BLUE else (PL if col==PURPLE else 'F8EFE6'),paras=[([R('特点（概括）',12,col,True)],0),([R(feat,13,TXT)],2)],ins=8,adj=6000)
def d1(x,w):
    box(sl,x+16,142,78,62,[([R('LLM',16,'FFFFFF',True)],0)],fill=BLUE,line=None)
    arrow(sl,x+130,174,x+98,174,c=BLUE,lw=2)
    for k,t in enumerate(['笔记 / 日志','向量库 / 图']):
        box(sl,x+134,138+k*36,w-150,30,[([R(t,13,BLUE,True)],0)],fill='FFFFFF',line=BLUE)
    text(sl,x+16,206,w-32,16,[([R('记忆是外部的、可读的文本',12,GRAY)],0)],algn='ctr')
def d2(x,w):
    box(sl,x+30,138,w-60,66,[([R('LLM',14,'FFFFFF',True)],0)],fill=PURPLE,line=None,anchor='t',ins=6)
    for k in range(3): shape(sl,x+46,168+k*10,w-92,6,fill='D9CCEB',prst='rect')
    text(sl,x+16,206,w-32,16,[([R('记忆写进权重（内部或外挂适配器）',12,GRAY)],0)],algn='ctr')
def d3(x,w):
    box(sl,x+16,138,w-100,66,[([R('LLM',14,'FFFFFF',True)],0),([R('KV / 隐状态',12,'FFFFFF',False)],2)],fill=BROWN,line=None)
    box(sl,x+w-76,150,60,40,[([R('编码器',12,BROWN,True)],0)],fill='FFFFFF',line=BROWN)
    arrow(sl,x+w-78,170,x+w-82,170,c=BROWN,lw=2)
    text(sl,x+16,206,w-32,16,[([R('记忆是模型内部的向量表示',12,GRAY)],0)],algn='ctr')
fcard(64,270,BLUE,'token 级（可读文本）',d1,
      [('1D 平面：','Reflexion · MemGPT · Mem0 · Voyager'),('2D 平面（树/图）：','A-Mem · MemTree · M3-Agent'),('3D 层级：','Zep · GraphRAG · HippoRAG')],
      '可读、可编辑、可追溯；但要占用上下文，规模大了检索成本高')
fcard(346,270,PURPLE,'参数化（写进权重）',d2,
      [('内部：','训练各阶段写入（Character-LM · MEND）'),('外部：','适配器（K-Adapter · WISE · MemLoRA）或辅助 LM（MAC）')],
      '不占上下文；但写入代价高，难以精确修改某一条')
fcard(628,268,BROWN,'潜在（隐状态）',d3,
      [('生成：','辅助模型产生嵌入，影响前向计算'),('复用：','把 KV 缓存等中间状态向后传'),('转换：','对内部状态压缩、合并、投影'),('代表：','MemoryLLM · M+ · MemGen')],
      '紧凑、贴近模型内部；但人读不懂，难审计、难纠错')
banner(sl,64,444,832,48,[([R('口径差别：',14,GOLD,True),R('Anthropic 只把可读取的上下文（对应 token 级）算作记忆，排除改权重；综述把三种形式都纳入。本讲主要讲 token 级',14,'FFFFFF')],0)])

# ---- 10 按结构
sl=newslide('按「结构」分：四种常见形态，以及分类为何不统一','02 · 记忆的分类 · 综述 2602.19320',footer=False)
S4=[(BLUE,'轻量语义记忆','独立文本单元存入向量空间，按 top-k 相似度检索；多为只追加，无显式关系','MemAgent · MemSearcher · ACON · TokMem'),
    (PURPLE,'实体中心 / 个性化记忆','围绕用户、任务、偏好等显式实体，按预定义模式存成结构化记录或属性-值对','A-MEM · Memory-R1 · PAMU · MemOrb'),
    (BROWN,'情景 / 反思记忆','交互按「情节」或高层摘要组织，定期通过摘要或反思来巩固','MemR3 · MemP · LEGOMem · TiMem · MemRL'),
    (GREEN,'结构化 / 分层记忆','显式分层（短期 / 长期）存储，或用关系图连接记忆单元','MAGMA · Zep · MemGPT · MemoryOS · EverMemOS')]
for i,(c,n,d,ex) in enumerate(S4):
    y=100+i*84
    shape(sl,64,y,520,78,fill=CARD,line=c,lw=1.25,adj=5000)
    circ(sl,74,y+8,26,str(i+1),c,13)
    text(sl,108,y+6,470,20,[([R(n,16,c,True)],0)])
    text(sl,108,y+26,470,36,[([R(d,13,TXT)],0)])
    text(sl,108,y+61,470,16,[([R('例：'+ex,12,GRAY)],0)])
shape(sl,600,100,296,330,fill='FFFFFF',line=RED,lw=1.5,adj=3000)
shape(sl,600,100,296,28,fill=RED,paras=[([R('同一个方法，不同的归类',15,'FFFFFF',True)],0)],algn='ctr',anchor='ctr',adj=10000)
yy=136
for n,a,b in [('A-MEM','2512.13564：平面（2D）token 记忆','2602.19320：实体中心记忆'),('MemGPT','2512.13564：1D 平面记忆','2602.19320：结构化 / 分层记忆')]:
    text(sl,612,yy,274,18,[([R(n,15,RED,True)],0)])
    box(sl,612,yy+22,274,26,[([R(a,12,TXT)],0)],fill=BL,line=BLUE,algn='l',ins=6)
    arrow(sl,749,yy+50,749,yy+62,c=GRAY,lw=1.5)
    box(sl,612,yy+64,274,26,[([R(b,12,TXT)],0)],fill='F8EFE6',line=BROWN,algn='l',ins=6)
    yy+=104
text(sl,612,yy-2,274,80,[([R('原因：',13,RED,True),R('切的轴不一样——一个按载体与拓扑，一个按组织方式。',13,TXT)],0),([R('综述里的「类别」不是方法的固有属性',13,TXT)],4)])
banner(sl,64,442,832,50,[([R('读综述的第一步：',14,GOLD,True),R('先看它「按什么轴切」；同一个方法在不同综述里的位置可以不同，不要把某一篇的分类当成定论',14,'FFFFFF')],0)])

# ---- 11 Anthropic 四层
sl=newslide('Anthropic 的四层结构：从日志到注入上下文','02 · 记忆的分类 · Anthropic：The components of agent memory',footer=False)
L=[(GREEN,'FFFFFF','注入上下文','每次新会话开头加载，必须小',250),
   ('6F8444','FFFFFF','记忆表示（如 wiki）','Claude 写的页面，汇总主题并链接相关笔记',320),
   ('8FA36A','FFFFFF','记忆笔记','会话中写下的显著观察，存成文件或标在日志里',400),
   ('B9C49C',TXT,'转录日志','可检索的事件日志，记录 agent 做过的一切',460)]
for i,(c,fg,n,d,w) in enumerate(L):
    y=104+i*74; x=64+(460-w)/2
    box(sl,x,y,w,66,[([R(n,15,fg,True)],0),([R(d,13,fg)],2)],fill=c,line=None,ins=8)
line(sl,548,404,548,112,c=BROWN,lw=4,head=True)
text(sl,486,408,110,34,[([R('dreaming',13,BROWN,True)],0),([R('自下而上',12,BROWN)],0)],algn='ctr')
text(sl,66,408,200,34,[([R('越往上：越小、越贵、越精',13,GREEN,True)],0)])
for i,(c,t,d) in enumerate([(BROWN,'dreaming（离线）','读转录日志，对照检验笔记；生成表示；把少量要点提升到注入层，细节下沉'),
                            (PURPLE,'现场写入','会话进行中，把显著观察直接写成笔记'),
                            (BLUE,'读取','注入层每次自动带上；其余层需要时再读取或搜索')]):
    y=100+i*108
    shape(sl,576,y,320,100,fill=CARD,line=c,lw=1.25,adj=5000)
    shape(sl,576,y,320,26,fill=c,paras=[([R(t,14,'FFFFFF',True)],0)],anchor='ctr',ins=10,adj=14000)
    text(sl,586,y+32,300,64,[([R(d,14,TXT)],0)])
banner(sl,64,448,832,44,[([R('为什么分层：',14,GOLD,True),R('注入的每个 token 都有成本，指令越长遵循度越低，所以上层必须小；底层完整但大，需要时再取',14,'FFFFFF')],0)])

# ---- 12 目录 三
toc(CH,2)
