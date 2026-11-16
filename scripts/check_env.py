"""检查独立出片依赖；不会自动安装或修改配置。"""
import importlib
import os
from pathlib import Path
import platform
import shutil
import sys


def main():
    print('Python', sys.version.split()[0], platform.system())
    print('解释器：', sys.executable)
    bad = sys.version_info < (3, 9)
    if bad:
        print('需要 Python 3.9 或更新版本')
    for module, package, required in [
        ('pptx', 'python-pptx', True), ('PIL', 'Pillow', True), ('lxml', 'lxml', True),
        ('fitz', 'PyMuPDF（PDF 转图）', False), ('matplotlib', 'matplotlib（数据图）', False),
    ]:
        try:
            importlib.import_module(module)
            print('OK   ' + package)
        except ImportError:
            print(('缺失 ' if required else '可选 ') + package)
            bad |= required
    root = Path(__file__).resolve().parents[1]
    template = Path(os.environ.get('PPTFLOW_TEMPLATE', root / 'assets/templates/seu/template.pptx')).expanduser()
    if not template.is_file():
        print('缺失模板：' + str(template))
        bad = True
    else:
        print('模板：' + str(template))
    office = shutil.which('soffice') or shutil.which('libreoffice')
    print('可选渲染器：' + (office or '未找到 LibreOffice，可使用宿主、PowerPoint 或 WPS 渲染'))
    print('字体：' + os.environ.get('PPTFLOW_FONT', 'Noto Sans SC') + '；请确认本机已安装，换字体后重新检查布局。')
    if bad:
        print('可使用已满足依赖的解释器，或运行 scripts/setup_env.py 创建隔离环境。')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
