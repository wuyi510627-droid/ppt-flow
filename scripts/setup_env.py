"""准备本技能的隔离 Python 环境，不修改 shell 或全局包。"""
import argparse
from pathlib import Path
import subprocess
import sys
import venv


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--qa', action='store_true', help='同时安装 PDF 转图和绘图依赖')
    parser.add_argument('--venv', type=Path, help='自定义隔离环境目录')
    args = parser.parse_args()
    if sys.version_info < (3, 9):
        parser.error('需要 Python 3.9 或更新版本')
    root = Path(__file__).resolve().parents[1]
    env = args.venv.expanduser().resolve() if args.venv else root / '.venv'
    if env.exists() and not (env / 'pyvenv.cfg').is_file():
        parser.error('目标目录不是虚拟环境，停止以避免改动：' + str(env))
    if not env.exists():
        venv.EnvBuilder(with_pip=True).create(env)
    python = env / ('Scripts/python.exe' if sys.platform == 'win32' else 'bin/python')
    requirements = root / ('requirements-qa.txt' if args.qa else 'requirements.txt')
    subprocess.run([str(python), '-m', 'pip', 'install', '-r', str(requirements)], check=True)
    subprocess.run([str(python), str(root / 'scripts/check_env.py')], check=True)
    print('出片解释器：' + str(python))


if __name__ == '__main__':
    main()
