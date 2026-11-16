# 出片脚本

Python 3.9+；核心依赖见 requirements.txt。运行 setup_env.py 可创建隔离环境；--qa 额外安装 PyMuPDF 与 matplotlib。字体及 LibreOffice 是系统资源，不由 pip 安装。

## 页面片段

片段是可信的 Python 代码，由 build.py 依次执行，共享 common 模块的同一份 Presentation。不要把不明来源的代码当成论文数据直接执行。

```python
from common import *
sl = newslide('标题', '01 · 章节')
flow(sl, 80, 180, [('输入', '任务'), ('处理', '关键步骤'), ('结果', '反馈')],
     w=230, h=100, gap=55, tsz=22, dsz=18)
notes(sl, '约 1 分钟：按图从左到右解释输入、步骤和结果。')
```

```bash
python scripts/build.py outputs/deck.pptx part1.py part2.py
python scripts/build.py outputs/deck.pptx part1.py --notes-out outputs/talk.md
python scripts/check_fit.py outputs/deck.pptx
```

片段路径与输出路径按命令运行目录解析；片段内 pic() 的相对图片路径按该片段所在目录解析。可从任意工作目录调用 build.py 的绝对路径。输出文件会被覆盖，避免使用原稿文件名；模板和片段不会被输出覆盖。

## 常用函数

| 函数 | 用途 |
| --- | --- |
| cover(title, date, presenter=None)、toc(items, active)、thanks() | 封面、目录、结束页 |
| newslide(title, crumb, footer=True) | 从模板复制正文页 |
| R(text, size, color, bold) | 一段带格式文字 |
| text、box、shape、banner、chip | 文字与原生图形 |
| flow、line、arrow | 流程与连线 |
| pic(sl, path, (x,y,w,h)) | 按比例插图 |
| notes(sl, text) | 写入本页讲稿 |

坐标单位 pt；默认页面 960×540。图形边界是文本容器边界，并不保证文字一定装得下。正文一般放在 y=100–480 之间，避免遮挡标题、面包屑与页码。

build.py 会移除模板原始页，更新已有的 n/N 页码并导出讲稿。已有 PPT 的局部修改需要按原稿结构单独实现，不能把 build.py 当作通用“无损更新任意 PPT”工具。

## 渲染

有 LibreOffice 时：

```bash
soffice --headless --convert-to pdf --outdir outputs outputs/deck.pptx
python scripts/pdf_to_png.py outputs/deck.pdf outputs/preview 120
```

也可以用宿主渲染器、PowerPoint 或 WPS。check_fit.py 是粗略估算，复杂字体、表格或布局仍需看图检查。
