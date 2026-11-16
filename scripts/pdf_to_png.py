"""把 PDF（如 WPS 导出的）逐页转成 PNG，供逐页检查。
用法：python pdf_to_png.py deck.pdf [输出目录] [dpi，默认 80]"""
import sys, os
import fitz  # pip install pymupdf
pdf = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(pdf)[0] + "_png"
dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 80
os.makedirs(out, exist_ok=True)
doc = fitz.open(pdf)
for i, page in enumerate(doc, 1):
    page.get_pixmap(dpi=dpi).save(os.path.join(out, f"p-{i:02d}.png"))
print(f"{len(doc)} 页 → {out}")
