"""文字适配估算：不渲染，直接按字号和框尺寸估计每个文本框会不会溢出。
用法：python check_fit.py deck.pptx [余量，默认 1.0]
估算规则（保守）：汉字宽=字号，字母/数字宽=0.55×字号，行高=1.2×字号，不计上下内边距。
提示：这是估算，会有误报和漏报；以渲染后的实际页面为准。"""
import sys, math
from pptx import Presentation
from pptx.util import Emu

def cw(ch, sz):
    return sz if ord(ch) > 0x2E80 else sz * 0.55

def para_lines(text, sz, width):
    if not text: return 1
    lines, cur = 1, 0.0
    for ch in text:
        w = cw(ch, sz)
        if cur + w > width: lines += 1; cur = w
        else: cur += w
    return lines

prs = Presentation(sys.argv[1]); slack = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
flag = 0
for n, sl in enumerate(prs.slides, 1):
    for sh in sl.shapes:
        if not sh.has_text_frame or not sh.text_frame.text.strip(): continue
        tf = sh.text_frame
        W = Emu(sh.width).pt; H = Emu(sh.height).pt
        li = Emu(tf.margin_left).pt; ri = Emu(tf.margin_right).pt
        ti = Emu(tf.margin_top).pt; bi = Emu(tf.margin_bottom).pt
        avail = W - li - ri
        if avail < 8 or H < 8: continue
        need = 0.0
        for p in tf.paragraphs:
            sizes = [r.font.size.pt for r in p.runs if r.font.size]
            sz = max(sizes) if sizes else 12
            txt = "".join(r.text for r in p.runs)
            need += para_lines(txt, sz, avail) * sz * 1.2
            if p.space_before: need += p.space_before.pt
        if need > H * slack + 0:
            flag += 1
            print(f"第 {n} 页  需要约 {need:.0f}pt > 框高 {H:.0f}pt  「{tf.text.strip()[:24]}」")
print(f"共 {flag} 处可能溢出" if flag else "未发现可能溢出的文本框")
