"""验证克隆后最关键的使用行为，不依赖本机字体或外部渲染器。"""
from pathlib import Path
import os
import re
import subprocess
import sys
import tempfile
import unittest
from zipfile import ZipFile

from lxml import etree
from PIL import Image
from pptx import Presentation

ROOT = Path(__file__).resolve().parents[1]
NS = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
      'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}


class WorkflowTests(unittest.TestCase):
    def run_script(self, script, *args, cwd, check=True):
        env = os.environ.copy()
        env.pop('PPTFLOW_TEMPLATE', None)
        env.pop('PPTFLOW_DATA', None)
        env.pop('PPTFLOW_FONT', None)
        env['PYTHONIOENCODING'] = 'utf-8'
        return subprocess.run([sys.executable, str(ROOT / 'scripts' / script), *map(str, args)],
                              cwd=cwd, env=env, capture_output=True, text=True, encoding='utf-8', check=check)

    def test_quickstart_from_another_directory(self):
        with tempfile.TemporaryDirectory(prefix='ppt flow ') as tmp:
            output = Path(tmp) / 'nested output' / '示例.pptx'
            self.run_script('build.py', output, ROOT / 'examples/quickstart.py', cwd=tmp)
            deck = Presentation(output)
            self.assertEqual(len(deck.slides), 4)
            self.assertEqual((deck.slide_width, deck.slide_height), (12192000, 6858000))
            for index, slide in enumerate(deck.slides, 1):
                self.assertTrue(slide.notes_slide.notes_text_frame.text.strip())
                for shape in slide.shapes:
                    if shape.has_text_frame and re.fullmatch(r'\d+/\d+', shape.text.strip()):
                        self.assertEqual(shape.text.strip(), f'{index}/4')
            self.assertGreater(len(deck.slides[1].shapes), 8)
            notes = output.with_name('示例_讲稿.md').read_text(encoding='utf-8')
            for index, slide in enumerate(deck.slides, 1):
                self.assertIn(f'## 第 {index} 页', notes)
                self.assertIn(slide.notes_slide.notes_text_frame.text.strip(), notes)
            with ZipFile(output) as archive:
                self.assertIsNone(archive.testzip())
                for name in archive.namelist():
                    if re.fullmatch(r'ppt/slides/slide\d+\.xml', name):
                        xml = etree.fromstring(archive.read(name))
                        ids = xml.xpath('.//p:cNvPr/@id', namespaces=NS)
                        self.assertEqual(len(ids), len(set(ids)), name)

    def test_fragment_assets_resolve_beside_the_fragment(self):
        with tempfile.TemporaryDirectory(prefix='ppt assets ') as tmp:
            base = Path(tmp)
            parts = base / 'parts with spaces'
            parts.mkdir()
            Image.new('RGB', (20, 10), 'blue').save(parts / 'sample.png')
            fragment = parts / 'page.py'
            fragment.write_text("from common import *\nsl=newslide('图片路径测试')\npic(sl,'sample.png',(100,150,200,100))\nnotes(sl,'图片相对页面片段解析。')\n", encoding='utf-8')
            output = base / 'result.pptx'
            self.run_script('build.py', output, fragment, cwd=base)
            deck = Presentation(output)
            images = [shape for shape in deck.slides[0].shapes if hasattr(shape, 'image')]
            self.assertTrue(any(shape.image.blob == (parts / 'sample.png').read_bytes() for shape in images))

    def test_personal_data_init_preserves_existing_notes(self):
        with tempfile.TemporaryDirectory(prefix='ppt data ') as tmp:
            data = Path(tmp) / 'personal'
            self.run_script('init_data.py', '--data-dir', data, cwd=tmp)
            profile = data / 'profile.md'
            self.assertTrue(profile.is_file())
            profile.write_text('我的自定义内容\n', encoding='utf-8')
            self.run_script('init_data.py', '--data-dir', data, cwd=tmp)
            self.assertEqual(profile.read_text(encoding='utf-8'), '我的自定义内容\n')
            self.assertTrue((data / 'topics/_pool.md').is_file())

    def test_bad_input_does_not_create_output(self):
        with tempfile.TemporaryDirectory(prefix='ppt invalid ') as tmp:
            output = Path(tmp) / 'result.pptx'
            result = self.run_script('build.py', output, Path(tmp) / 'missing.py', cwd=tmp, check=False)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(output.exists())


if __name__ == '__main__':
    unittest.main()
