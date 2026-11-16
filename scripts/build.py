"""从可信的 Python 页面片段生成 PPTX，并导出逐页备注。"""
import argparse
import os
from pathlib import Path
import re


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    parser.add_argument('parts', nargs='+', type=Path)
    parser.add_argument('--notes-out', type=Path, help='默认：输出名_讲稿.md')
    args = parser.parse_args()
    output = args.output.expanduser().resolve()
    parts = [p.expanduser().resolve() for p in args.parts]
    if output.suffix.lower() != '.pptx':
        parser.error('输出文件应使用 .pptx 扩展名')
    for part in parts:
        if not part.is_file():
            parser.error('找不到页面片段：' + str(part))
    notes_path = (args.notes_out.expanduser().resolve() if args.notes_out
                  else output.with_name(output.stem + '_讲稿.md'))
    if notes_path == output or notes_path in parts or output in parts:
        parser.error('输出路径不能覆盖页面片段，PPT 与讲稿也不能使用同一路径')

    # 延后导入：--help 在未安装出片依赖时仍能使用。
    import common
    if output == Path(common.REF) or notes_path == Path(common.REF):
        parser.error('输出不能覆盖模板')
    scope = dict(vars(common))
    cwd = Path.cwd()
    try:
        for part in parts:
            os.chdir(part.parent)
            scope['__file__'] = str(part)
            scope['__name__'] = '__main__'
            exec(compile(part.read_text(encoding='utf-8'), str(part), 'exec'), scope)
    finally:
        os.chdir(cwd)

    prs = common.prs
    if len(prs.slides) <= common.N_TEMPLATE:
        parser.error('页面片段没有创建新幻灯片')
    for entry in list(prs.slides._sldIdLst)[:common.N_TEMPLATE]:
        prs.part.drop_rel(entry.rId)
        prs.slides._sldIdLst.remove(entry)
    count = len(prs.slides)
    manuscript = ['# ' + output.stem + ' · 逐页讲稿', '']
    for index, slide in enumerate(prs.slides, 1):
        for shape in slide.shapes:
            if shape.has_text_frame and re.fullmatch(r'\s*\d+/\d+\s*', shape.text_frame.text):
                common.settext(shape, f'{index}/{count}')
        title = slide.shapes.title
        title_text = title.text.strip() if title is not None else ''
        manuscript += [f'## 第 {index} 页' + (' · ' + title_text if title_text else ''), '']
        frame = slide.notes_slide.notes_text_frame
        note = frame.text.strip() if frame is not None else ''
        manuscript += [note or '（本页暂无讲稿）', '']
    output.parent.mkdir(parents=True, exist_ok=True)
    notes_path.parent.mkdir(parents=True, exist_ok=True)
    prs.save(output)
    notes_path.write_text('\n'.join(manuscript), encoding='utf-8')
    print(f'saved {count}: {output}')
    print(f'notes: {notes_path}')


if __name__ == '__main__':
    main()
