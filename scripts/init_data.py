"""初始化个人资料；只创建缺失文件，永不覆盖已有记录。"""
import argparse
import os
from pathlib import Path


def default_dir():
    if os.environ.get('PPTFLOW_DATA'):
        return Path(os.environ['PPTFLOW_DATA']).expanduser().resolve()
    root = Path(__file__).resolve().parents[1]
    cwd = Path.cwd().resolve()
    if cwd == root or root in cwd.parents:
        return root.parent / 'ppt-flow-data'
    return cwd / 'ppt-flow-data'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-dir', type=Path)
    args = parser.parse_args()
    dest = args.data_dir.expanduser().resolve() if args.data_dir else default_dir()
    source = Path(__file__).resolve().parents[1] / 'assets/data-template'
    for item in sorted(source.rglob('*.md')):
        output = dest / item.relative_to(source)
        output.parent.mkdir(parents=True, exist_ok=True)
        try:
            with output.open('x', encoding='utf-8') as stream:
                stream.write(item.read_text(encoding='utf-8'))
            print('created: ' + str(output))
        except FileExistsError:
            print('kept: ' + str(output))
    print('个人资料目录：' + str(dest))


if __name__ == '__main__':
    main()
