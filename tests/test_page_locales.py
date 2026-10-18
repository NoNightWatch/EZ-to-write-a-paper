"""Check the language-specific artwork and navigation on the public pages.

Run from any directory: python -B tests/test_page_locales.py
English manuscript examples, product names, commands, and language switches
are intentionally retained on the Chinese pages.
"""
from html.parser import HTMLParser
from pathlib import Path
import re
import struct
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PAGES = {
    'zh-CN': ('README.md', 'docs/guide.zh-CN.md'),
    'en': ('README.en.md', 'docs/guide.en.md'),
}
SECTIONS = ('first-quest', 'quests', 'start-here', 'library', 'controls', 'workflow', 'faq')
SVG_NS = '{http://www.w3.org/2000/svg}'


class Page(HTMLParser):
    def __init__(self, content):
        super().__init__()
        self.images = []
        self.links = []
        self.feed(content)
        self.links.extend(re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)\s]+)\)', content))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'img':
            self.images.append(attrs)
        if tag == 'a' and 'href' in attrs:
            self.links.append(attrs['href'])


def locale_errors(content, locale):
    errors = []
    for image in Page(content).images:
        src = image.get('src', '')
        if 'assets/guild/' in src:
            localized = '/guild/zh-CN/' in src
            if localized != (locale == 'zh-CN'):
                errors.append(src)
        elif 'assets/writing-guild' in src:
            if src.endswith('.zh-CN.png') != (locale == 'zh-CN'):
                errors.append(src)
        else:
            errors.append(f'Artwork has no declared locale: {src}')
    return errors


class PageLocaleTests(unittest.TestCase):
    def test_all_public_pages_use_their_own_artwork(self):
        for locale, pages in PAGES.items():
            for path in pages:
                with self.subTest(page=path):
                    self.assertEqual(locale_errors((ROOT/path).read_text(encoding='utf-8'), locale), [])

    def test_wrong_language_references_are_rejected(self):
        for src, locale in [
            ('assets/guild/first-quest.svg', 'zh-CN'),
            ('assets/guild/zh-CN/first-quest.svg', 'en'),
            ('assets/writing-guild.png', 'zh-CN'),
            ('assets/writing-guild.zh-CN.png', 'en'),
        ]:
            with self.subTest(src=src):
                self.assertTrue(locale_errors(f'<img src="{src}" alt="test" />', locale))

    def test_image_pairs_exist_and_have_accessible_labels(self):
        for locale, pages in PAGES.items():
            for path in pages:
                page = ROOT/path
                images = Page(page.read_text(encoding='utf-8')).images
                self.assertEqual(len(images), 14 if path.startswith('README') else 2)
                for image in images:
                    self.assertTrue((page.parent/image['src']).is_file(), image['src'])
                    self.assertTrue(image.get('alt', '').strip())
                    if locale == 'zh-CN':
                        self.assertRegex(image['alt'], r'[\u4e00-\u9fff]')

    def test_every_svg_has_a_complete_chinese_counterpart(self):
        originals = sorted((ROOT/'assets/guild').glob('*.svg'))
        translated = sorted((ROOT/'assets/guild/zh-CN').glob('*.svg'))
        self.assertEqual({p.name for p in originals}, {p.name for p in translated})
        self.assertEqual(len(originals), 17)
        for original in originals:
            source = ET.parse(original).getroot()
            target = ET.parse(ROOT/'assets/guild/zh-CN'/original.name).getroot()
            with self.subTest(asset=original.name):
                self.assertEqual(source.get('viewBox'), target.get('viewBox'))
                self.assertEqual(target.get('{http://www.w3.org/XML/1998/namespace}lang'), 'zh-CN')
                self.assertRegex(target.findtext(SVG_NS+'title'), r'[\u4e00-\u9fff]')
                self.assertEqual(target.get('aria-label'), target.findtext(SVG_NS+'title'))
                self.assertTrue(target.findall('.//'+SVG_NS+'path'))
                self.assertFalse(target.findall('.//'+SVG_NS+'text'))
                self.assertFalse(target.findall('.//'+SVG_NS+'image'))

    def test_numbered_sections_match_in_both_languages(self):
        for locale, paths in PAGES.items():
            images = Page((ROOT/paths[0]).read_text(encoding='utf-8')).images
            sections = [Path(i['src']).stem for i in images if Path(i['src']).stem in SECTIONS]
            self.assertEqual(tuple(sections), SECTIONS, locale)
        for i, name in enumerate(SECTIONS, 1):
            svg = ET.parse(ROOT/f'assets/guild/zh-CN/{name}.svg').getroot()
            self.assertTrue(svg.findtext(SVG_NS+'title').startswith(f'{i:02d} · '))

    def test_home_and_guide_navigation_stays_in_locale(self):
        for locale, paths in PAGES.items():
            home, guide = paths
            home_links = Page((ROOT/home).read_text(encoding='utf-8')).links
            guide_links = Page((ROOT/guide).read_text(encoding='utf-8')).links
            self.assertIn(guide, home_links)
            self.assertIn('../'+home, guide_links)
            for anchor in ('try-without-install', 'install', 'field-style', 'reviewer-response', 'update'):
                self.assertIn(f'{guide}#{anchor}', home_links)

    def test_language_switches_remain_available(self):
        for locale, other in [('zh-CN', 'en'), ('en', 'zh-CN')]:
            home, guide = PAGES[locale]
            other_home, other_guide = PAGES[other]
            self.assertIn(other_home, Page((ROOT/home).read_text(encoding='utf-8')).links)
            self.assertIn(Path(other_guide).name, Page((ROOT/guide).read_text(encoding='utf-8')).links)

    def test_hero_images_keep_matching_aspect_ratio(self):
        dimensions = []
        for name in ('writing-guild.png', 'writing-guild.zh-CN.png'):
            with (ROOT/'assets'/name).open('rb') as handle:
                header = handle.read(24)
            self.assertEqual(header[:8], b'\x89PNG\r\n\x1a\n')
            width, height = struct.unpack('>II', header[16:24])
            dimensions.append((width,height))
        self.assertEqual(dimensions[0][0]*dimensions[1][1], dimensions[1][0]*dimensions[0][1])


if __name__ == '__main__':
    unittest.main(verbosity=2)
