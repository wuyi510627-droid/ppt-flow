import copy, re, sys, os
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE)
from lib import *
from pptx import Presentation
from pptx.opc.constants import RELATIONSHIP_TYPE as RT
from pptx.util import Emu
from PIL import Image

GREEN='4F6228'; GL='E8EDDB'; CREAM='F5EBDF'; BROWN='A0622D'; BLUE='3F6680'; BL='E6EDF3'
PURPLE='7B5EA7'; PL='EEE9F5'; RED='C0392B'; RL='FBEDEA'; CARD='FAFBF6'; CB='DCE0D2'
TXT='222222'; GR='4A4A4A'; GRAY='8C8C8C'; GOLD='E8D9A8'

REF=os.environ.get('PPTFLOW_TEMPLATE') or os.path.join(HERE,'..','assets','templates','seu','template.pptx')
REF=os.path.abspath(os.path.expanduser(REF))
prs=Presentation(REF)
SRC=list(prs.slides)   # 母版里的全部原始页（作为可复制的版式页）
N_TEMPLATE=len(SRC)
ORIG=set(id(s) for s in SRC)
if N_TEMPLATE < 27:
    raise ValueError('模板需保留第 1、2、17、27 页的版式；见 assets/templates/seu/template.md')

def dup(src):
    new=prs.slides.add_slide(src.slide_layout)
    for sh in list(new.shapes): sh._element.getparent().remove(sh._element)
    for sh in src.shapes:
        el=copy.deepcopy(sh._element)
        new.shapes._spTree.append(el)
        for blip in el.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}blip'):
            rid=blip.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
            if rid:
                part=src.part.related_part(rid)
                nr=new.part.relate_to(part,RT.IMAGE)
                blip.set('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed',nr)
    ids=[int(e.get('id')) for e in new._element.iter('{http://schemas.openxmlformats.org/presentationml/2006/main}cNvPr')]
    nid[0]=max([nid[0]]+ids)
    return new

def title_of(sl,t):
    ph=[s for s in sl.shapes if s.is_placeholder][0]
    settext(ph,t)

def newslide(title,crumb=None,footer=True):
    sl=dup(SRC[16]); strip(sl)
    title_of(sl,title)
    if not footer:
        for s in list(sl.shapes):
            if s.name=='Shape 6': s._element.getparent().remove(s._element)
    if crumb: text(sl,64,77,830,18,[([R(crumb,14,GREEN,True)],0)])
    return sl

def pc(sl,prob,core,y=97,h=52,split=404):
    """问题框(奶油)+核心框(绿)"""
    shape(sl,64,y,split,h,fill=CREAM,paras=[([R('解决的问题：',14,BROWN,True),R(prob,14,TXT)],0)],anchor='ctr',ins=8,adj=10000)
    shape(sl,64+split+8,y,832-split-8,h,fill=GREEN,paras=[([R('核心：',14,GOLD,True),R(core,14,'FFFFFF')],0)],anchor='ctr',ins=8,adj=10000)

def panel(sl,x,y,w,h,label=None,color=GREEN):
    shape(sl,x,y,w,h,fill=CARD,line=CB,lw=0.5,adj=3000)
    if label: text(sl,x+10,y+4,w-20,18,[([R(label,14,color,True)],0)])

def card3(sl,x,y,w,h,title,key,desc,color=GREEN):
    shape(sl,x,y,w,h,fill=CARD,line=CB,lw=0.5,adj=4000)
    text(sl,x+10,y+6,w-20,20,[([R(title,16,color,True)],0)])
    shape(sl,x+8,y+30,w-16,46,fill='FFFFFF',line=CB,lw=0.5,paras=[([R(key,15,TXT,True)],0)],anchor='ctr',ins=6,adj=6000)
    text(sl,x+10,y+80,w-20,h-84,[([R(desc,14,GR)],0)])

def proscons(sl,pro,con,y=482):
    text(sl,32,y,440,44,[([R('优点：',14,GREEN,True),R(pro,14,GREEN,True)],0)])
    text(sl,486,y,420,44,[([R('缺点：',14,BROWN,True),R(con,14,BROWN,True)],0)])

def chip(sl,x,y,w,h,t,fill,fg='FFFFFF',sz=12,line=None,b=True):
    shape(sl,x,y,w,h,fill=fill,line=line,prst='roundRect',adj=50000,paras=[([R(t,sz,fg,b)],0)],algn='ctr',anchor='ctr')

def box(sl,x,y,w,h,paras,fill='FFFFFF',line=CB,lw=0.75,algn='ctr',anchor='ctr',ins=4,adj=8000,dash=False):
    shape(sl,x,y,w,h,fill=fill,line=line,lw=lw,paras=paras,algn=algn,anchor=anchor,ins=ins,adj=adj,dash=dash)

def banner(sl,x,y,w,h,paras,fill=GREEN,line=None,anchor='ctr',algn='l',ins=10):
    shape(sl,x,y,w,h,fill=fill,line=line,paras=paras,anchor=anchor,algn=algn,ins=ins,adj=12000)

def pic(sl,path,box_,pad=0):
    bx,by,bw,bh=box_
    w,h=Image.open(path).size
    s=min(bw/w,bh/h); W,H=w*s,h*s
    sl.shapes.add_picture(path,Emu(E(bx+(bw-W)/2)),Emu(E(by+(bh-H)/2)),Emu(E(W)),Emu(E(H)))

def table_header(sl,x,y,w,cols,h=26):
    shape(sl,x,y,w,h,fill=GREEN,adj=6000)
    for cx,cw,t in cols: text(sl,cx,y+4,cw,18,[([R(t,13,'FFFFFF',True)],0)])

def line(sl,x1,y1,x2,y2,c='6B6B6B',lw=1.5,dash=False,head=False):
    nid[0]+=1
    tail='<a:tailEnd type="triangle" w="med" len="med"/>' if head else ''
    flips=(' flipH="1"' if x2<x1 else '')+(' flipV="1"' if y2<y1 else '')
    dash_xml='<a:prstDash val="dash"/>' if dash else ''
    add(sl,f'<p:cxnSp {P}><p:nvCxnSpPr><p:cNvPr id="{nid[0]}" name="L{nid[0]}"/><p:cNvCxnSpPr/><p:nvPr/></p:nvCxnSpPr><p:spPr><a:xfrm{flips}><a:off x="{E(min(x1,x2))}" y="{E(min(y1,y2))}"/><a:ext cx="{E(abs(x2-x1))}" cy="{E(abs(y2-y1))}"/></a:xfrm><a:prstGeom prst="straightConnector1"><a:avLst/></a:prstGeom><a:ln w="{E(lw)}"><a:solidFill><a:srgbClr val="{c}"/></a:solidFill>{dash_xml}{tail}</a:ln></p:spPr></p:cxnSp>')

def circ(sl,x,y,d,t,fill,sz=12,fg='FFFFFF'):
    shape(sl,x,y,d,d,fill=fill,prst='ellipse',paras=[([R(t,sz,fg,True)],0)],algn='ctr',anchor='ctr')

def cover(title,date,presenter=None):
    sl=dup(SRC[0])
    ph=[s for s in sl.shapes if s.is_placeholder][0]
    settext(ph,title); ph.left=E(20); ph.width=E(920)
    for s in sl.shapes:
        if s.has_text_frame and '日　期' in s.text_frame.text: settext(s,'日　期：'+date)
        if s.has_text_frame and '汇报人' in s.text_frame.text:
            settext(s,'汇报人：'+(presenter if presenter is not None else os.environ.get('PPTFLOW_PRESENTER','')))
    return sl

def toc(items,active,title='目录'):
    sl=dup(SRC[1]);
    for s in list(sl.shapes):
        if s.name in ('Text 3','Text 4','Text 5','Text 7'): s._element.getparent().remove(s._element)
    title_of(sl,title)
    n=len(items); y0=92; step=(470-y0)//n
    for i,t in enumerate(items):
        a=(i==active)
        shape(sl,200,y0+i*step,560,step-14,fill='EEF1E6' if a else None,prst='rect',paras=[([R(t,32,GREEN if a else '595959',a)],0)],anchor='ctr',ins=18)
    return sl

def thanks():
    return dup(SRC[26])

def flow(sl,x,y,items,w,h,gap,col=GREEN,tsz=14,dsz=12,fills=None,arrows=True,acol=GRAY):
    xs=[]
    for i,(t,d) in enumerate(items):
        bx=x+i*(w+gap); xs.append(bx)
        c=col[i] if isinstance(col,list) else col
        box(sl,bx,y,w,h,[([R(t,tsz,c,True)],0)]+([([R(d,dsz,GR)],2)] if d else []),fill='FFFFFF',line=c,lw=1,ins=4)
        if arrows and i>0: arrow(sl,bx-gap+2,y+h/2,bx-2,y+h/2,c=acol,lw=1.75)
    return xs

PA=(40,153,430,175); PB=(482,153,438,175)
def pan(which,label,col=GREEN):
    x,y,w,h=PA if which=='a' else PB
    panel(sl_cur[0],x,y,w,h,label,col); return x,y,w,h
sl_cur=[None]
def cards_row(sl,specs,y=333,h=140):
    xs=[40,336,632]
    for x,(t,k,d,c) in zip(xs,specs): card3(sl,x,y,288,h,t,k,d,c)
