import re
from pptx import Presentation
from lxml import etree
NS={'a':'http://schemas.openxmlformats.org/drawingml/2006/main','p':'http://schemas.openxmlformats.org/presentationml/2006/main'}
E=lambda v:int(round(v*12700))
import os
FN=os.environ.get('PPTFLOW_FONT','Noto Sans SC')
FONT=f'<a:latin typeface="{FN}" pitchFamily="34" charset="0"/><a:ea typeface="{FN}" pitchFamily="34" charset="-122"/><a:cs typeface="{FN}" pitchFamily="34" charset="-120"/>'
P='xmlns:p="%s" xmlns:a="%s"'%(NS['p'],NS['a'])
nid=[2000]
def esc(t): return t.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def paras_xml(paras,algn):
    ps=''
    for runs,sb in paras:
        rs=''.join(f'<a:r><a:rPr lang="zh-CN" sz="{int(sz*100)}" b="{1 if b else 0}" dirty="0"><a:solidFill><a:srgbClr val="{c}"/></a:solidFill>{FONT}</a:rPr><a:t>{esc(t)}</a:t></a:r>' for t,sz,c,b in runs)
        ps+=f'<a:p><a:pPr marL="0" indent="0" algn="{algn}"><a:lnSpc><a:spcPct val="115000"/></a:lnSpc><a:spcBef><a:spcPts val="{int(sb*100)}"/></a:spcBef><a:buNone/></a:pPr>{rs}</a:p>'
    return ps
def add(sl,x): sl.shapes._spTree.append(etree.fromstring(x))
def shape(sl,x,y,w,h,fill=None,line=None,lw=0.75,prst='roundRect',paras=None,algn='l',anchor='t',ins=0,adj=8000,dash=False):
    nid[0]+=1
    f=f'<a:solidFill><a:srgbClr val="{fill}"/></a:solidFill>' if fill else '<a:noFill/>'
    dash_xml='<a:prstDash val="dash"/>' if dash else ''
    l=f'<a:ln w="{E(lw)}"><a:solidFill><a:srgbClr val="{line}"/></a:solidFill>{dash_xml}</a:ln>' if line else '<a:ln><a:noFill/></a:ln>'
    av=f'<a:gd name="adj" fmla="val {adj}"/>' if prst=='roundRect' else ''
    tb=f'<p:txBody><a:bodyPr wrap="square" lIns="{E(ins)}" tIns="{E(ins*0.6)}" rIns="{E(ins)}" bIns="{E(ins*0.6)}" anchor="{anchor}"><a:noAutofit/></a:bodyPr><a:lstStyle/>{paras_xml(paras,algn)}</p:txBody>' if paras else ''
    tx=' txBox="1"' if (paras and not fill and not line) else ''
    add(sl,f'<p:sp {P}><p:nvSpPr><p:cNvPr id="{nid[0]}" name="S{nid[0]}"/><p:cNvSpPr{tx}/><p:nvPr/></p:nvSpPr><p:spPr><a:xfrm><a:off x="{E(x)}" y="{E(y)}"/><a:ext cx="{E(w)}" cy="{E(h)}"/></a:xfrm><a:prstGeom prst="{prst}"><a:avLst>{av}</a:avLst></a:prstGeom>{f}{l}</p:spPr>{tb}</p:sp>')
def text(sl,x,y,w,h,paras,algn='l',anchor='t'): shape(sl,x,y,w,h,paras=paras,algn=algn,anchor=anchor)
def arrow(sl,x1,y1,x2,y2,c='6B6B6B',lw=1.5,dash=False):
    nid[0]+=1
    flips=(' flipH="1"' if x2<x1 else '')+(' flipV="1"' if y2<y1 else '')
    dash_xml='<a:prstDash val="dash"/>' if dash else ''
    add(sl,f'<p:cxnSp {P}><p:nvCxnSpPr><p:cNvPr id="{nid[0]}" name="A{nid[0]}"/><p:cNvCxnSpPr/><p:nvPr/></p:nvCxnSpPr><p:spPr><a:xfrm{flips}><a:off x="{E(min(x1,x2))}" y="{E(min(y1,y2))}"/><a:ext cx="{E(abs(x2-x1))}" cy="{E(abs(y2-y1))}"/></a:xfrm><a:prstGeom prst="straightConnector1"><a:avLst/></a:prstGeom><a:ln w="{E(lw)}"><a:solidFill><a:srgbClr val="{c}"/></a:solidFill>{dash_xml}<a:tailEnd type="triangle" w="med" len="med"/></a:ln></p:spPr></p:cxnSp>')
def R(t,sz=11,c='4A4A4A',b=False): return (t,sz,c,b)
def settext(sh,new):
    rs=sh._element.findall('.//a:r',NS)
    rs[0].find('a:t',NS).text=new
    for r in rs[1:]: r.getparent().remove(r)
def find(sl,sub): return [sh for sh in sl.shapes if sh.has_text_frame and sub in sh.text_frame.text]
def strip(sl):
    for sh in list(sl.shapes):
        if sh.is_placeholder: continue
        t=sh.top/12700
        if t<75 or t>=498: continue
        sh._element.getparent().remove(sh._element)
def notes(sl,t): sl.notes_slide.notes_text_frame.text=t
