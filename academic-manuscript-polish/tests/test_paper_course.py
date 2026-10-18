"""Read-only checks of fictional evidence, calculations and bilingual exercises.

These tests do not evaluate a model's tutoring decisions or learning outcomes.
"""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "assets/paper-course-data.json").read_text(encoding="utf-8"))


def read(name):
    return (ROOT / "references" / name).read_text(encoding="utf-8")


def source_records(text):
    blocks = re.findall(r'<a id="(C\d{2}-[AB])"></a>(.*?)(?=<a id=|## L1|\Z)', text, re.S)
    rows = {}
    for key, block in blocks:
        numbers = [int(n) for n in re.findall(r"^(\d+)\. ", block, re.M)]
        if numbers != list(range(1, len(numbers) + 1)) or not numbers:
            raise ValueError("Invalid item sequence: " + key)
        if key in rows:
            raise ValueError("Duplicate source: " + key)
        rows[key] = (len(numbers), int(bool(re.search(r"^Contact: ", block, re.M))))
    return rows


def table_records(text, prefix):
    rows = {}
    for line in text.splitlines():
        cells = [s.strip() for s in line.strip().strip("|").split("|")]
        if re.fullmatch(prefix + r"\d{2}", cells[0]):
            if cells[0] in rows:
                raise ValueError("Duplicate table row")
            rows[cells[0]] = tuple(int(x) for x in cells[1:])
    return rows


def expected(pairs, change=False):
    result = {}
    for p in pairs:
        values = tuple(p[k] for k in ("earlier_items", "later_items", "earlier_contact", "later_contact"))
        result[p["id"]] = values + ((values[1] - values[0],) if change else ())
    return result


class PaperCourseTests(unittest.TestCase):
    def test_01_fictional_data_schema(self):
        self.assertIs(DATA["fictional"], True)
        self.assertIs(DATA["transfer"]["fictional"], True)
        for pairs in (DATA["pairs"], DATA["transfer"]["pairs"]):
            self.assertEqual(len({p["id"] for p in pairs}), len(pairs))
            for p in pairs:
                for version in ("earlier", "later"):
                    self.assertGreater(p[version + "_items"], 0)
                    self.assertIn(p[version + "_contact"], (0, 1))

    def test_02_complete_source_inventory(self):
        rows = source_records(read("paper-case-materials.md"))
        self.assertEqual(set(rows), {p["id"] + "-" + v for p in DATA["pairs"] for v in "AB"})
        self.assertEqual(len(rows), 12)

    def test_03_source_item_counts_match_records(self):
        rows = source_records(read("paper-case-materials.md"))
        for p in DATA["pairs"]:
            for letter, version in (("A", "earlier"), ("B", "later")):
                self.assertEqual(rows[p["id"] + "-" + letter][0], p[version + "_items"])

    def test_04_source_contacts_match_records(self):
        rows = source_records(read("paper-case-materials.md"))
        for p in DATA["pairs"]:
            for letter, version in (("A", "earlier"), ("B", "later")):
                self.assertEqual(rows[p["id"] + "-" + letter][1], p[version + "_contact"])

    def test_05_main_table_matches_data_and_changes(self):
        self.assertEqual(table_records(read("paper-case-manuscript.md"), "C"), expected(DATA["pairs"], True))

    def test_06_answer_tables_match_both_datasets(self):
        text = read("paper-answer-key.md")
        self.assertEqual(table_records(text, "C"), expected(DATA["pairs"], True))
        self.assertEqual(table_records(text, "N"), expected(DATA["transfer"]["pairs"], True))

    def test_07_bilingual_transfer_records_match(self):
        for locale in ("zh-CN", "en"):
            self.assertEqual(table_records(read("paper-workbook." + locale + ".md"), "N"),
                             expected(DATA["transfer"]["pairs"]))

    def test_08_main_totals_means_and_relative_change(self):
        rows = source_records(read("paper-case-materials.md"))
        a = sum(v[0] for k, v in rows.items() if k.endswith("A"))
        b = sum(v[0] for k, v in rows.items() if k.endswith("B"))
        self.assertEqual((a, b, a / 6, b / 6, (a - b) / a), (30, 21, 5.0, 3.5, .3))
        text = read("paper-case-manuscript.md")
        abstract = text.split("## Abstract", 1)[1].split("## 1.", 1)[0]
        results = text.split("## 3. Results", 1)[1].split("## 4.", 1)[0]
        for section in (abstract, results):
            self.assertRegex(section, rf"from {a} .*?to {b}")
            self.assertIn(f"{(a-b)/a:.0%}", section)
            self.assertRegex(section, rf"{a/6:.1f} (?:and|to) {b/6:.1f}")

    def test_09_contact_percentage_points(self):
        a = sum(p["earlier_contact"] for p in DATA["pairs"])
        b = sum(p["later_contact"] for p in DATA["pairs"])
        self.assertEqual((a, b), (2, 5))
        self.assertEqual(100 * (b - a) / len(DATA["pairs"]), 50)
        self.assertEqual(100 * (b - a) / a, 150)
        self.assertIn("50 percentage points", read("paper-case-manuscript.md"))

    def test_10_transfer_requires_a_different_conclusion(self):
        pairs = DATA["transfer"]["pairs"]
        changes = [p["later_items"] - p["earlier_items"] for p in pairs]
        self.assertEqual((sum(x < 0 for x in changes), sum(x > 0 for x in changes), changes.count(0)), (2, 1, 1))
        self.assertLess(sum(p["later_contact"] - p["earlier_contact"] for p in pairs), 0)
        self.assertTrue(set(p["id"] for p in pairs).isdisjoint(p["id"] for p in DATA["pairs"]))

    def test_11_transfer_arithmetic(self):
        pairs = DATA["transfer"]["pairs"]
        a = sum(p["earlier_items"] for p in pairs)
        b = sum(p["later_items"] for p in pairs)
        self.assertEqual((a, b, a / 4, b / 4), (14, 12, 3.5, 3.0))
        self.assertEqual(round(100 * (a - b) / a, 1), 14.3)
        answer = read("paper-answer-key.md").split("## T01", 1)[1]
        self.assertIn(f"from {a} to {b}", answer)
        self.assertIn(f"{100 * (a-b)/a:.1f}%", answer)

    def test_12_bilingual_task_inventory(self):
        for locale in ("zh-CN", "en"):
            ids = re.findall(r'<a id="([ET]\d{2})"></a>', read("paper-workbook." + locale + ".md"))
            self.assertEqual(ids, DATA["exercises"])

    def test_13_learner_count_tables_are_unfilled(self):
        for locale in ("zh-CN", "en"):
            lines = re.findall(r"^\| (C\d{2}) \|(.*)$", read("paper-workbook." + locale + ".md"), re.M)
            self.assertEqual({key for key, _ in lines}, {p["id"] for p in DATA["pairs"]})
            self.assertTrue(all(not cells.replace("|", "").strip() for _, cells in lines))

    def test_14_citations_resolve_to_supplied_readings(self):
        text = read("paper-case-manuscript.md")
        keys = set(re.findall(r"\[(L\d+)\]", text))
        self.assertEqual(keys, set(DATA["reading_cards"]))
        packet = read("paper-case-materials.md")
        for key in keys:
            self.assertEqual(packet.count(f'<a id="{key}"></a>'), 1)
        self.assertEqual(set(re.findall(r"\bC\d{2}\b", text)), {p["id"] for p in DATA["pairs"]})

    def test_15_invalid_or_changed_source_is_detectable(self):
        text = read("paper-case-materials.md")
        with self.assertRaises(ValueError):
            source_records(text.replace("2. Choose an available room.", "3. Choose an available room.", 1))
        changed = source_records(text.replace("4. Submit the booking form.\n", "", 1))
        self.assertNotEqual(changed["C01-A"][0], DATA["pairs"][0]["earlier_items"])

    def test_16_table_change_and_duplicate_are_detectable(self):
        text = read("paper-case-manuscript.md")
        altered = text.replace("| C01 | 4 | 3 |", "| C01 | 4 | 4 |", 1)
        self.assertNotEqual(table_records(altered, "C"), expected(DATA["pairs"], True))
        with self.assertRaises(ValueError):
            table_records(text + "\n| C01 | 4 | 3 | 0 | 1 | -1 |\n", "C")


if __name__ == "__main__":
    unittest.main(verbosity=2)
