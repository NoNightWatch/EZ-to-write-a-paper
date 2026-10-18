"""Offline usage lookup and journal-card regression tests; no manuscript input."""
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import runpy
import subprocess
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
API = runpy.run_path(str(ROOT / "scripts" / "search_usage.py"))
READ, SEARCH = API["read_records"], API["search"]
ROWS = READ(ROOT)
CHECK = runpy.run_path(str(ROOT / "scripts" / "validate_bundle.py"))["check_bundle"]
REAL_READ = Path.read_text


class UsageTests(unittest.TestCase):
    def cli(self, *args, env=None):
        return subprocess.run([sys.executable, "-B", str(ROOT / "scripts" / "search_usage.py"), *args],
                              capture_output=True, env=env)

    def changed(self, name, transform, action):
        def reader(path, *args, **kwargs):
            text = REAL_READ(path, *args, **kwargs)
            return transform(text) if path.resolve() == (ROOT / name).resolve() else text
        with patch.object(Path, "read_text", reader):
            return action()

    def test_01_coverage(self):
        self.assertEqual(len(ROWS), 208)
        counts = Counter(r["domain_id"] for r in ROWS)
        self.assertEqual(len(counts), 52)
        self.assertEqual(set(counts.values()), {4})

    def test_02_rebuild_software(self):
        rows = SEARCH(ROWS, "rebuild", "n10", True)
        self.assertEqual(len(rows), 1)
        self.assertIn("refactor", rows[0]["candidates"])
        self.assertEqual(rows[0]["evidence"], "S02")

    def test_03_rebuild_fisheries(self):
        rows = SEARCH(ROWS, "rebuild", "fisheries-aquaculture", True)
        self.assertEqual(rows[0]["evidence"], "S01")
        self.assertIn("stock", rows[0]["collocations"])

    def test_04_restructure_organization(self):
        rows = SEARCH(ROWS, "restructure", "s03", True)
        self.assertEqual(len(rows), 1)
        self.assertIn("organization", rows[0]["collocations"])

    def test_05_cross_field_senses(self):
        domains = {r["domain_id"] for r in SEARCH(ROWS, "rebuild", exact=True)}
        self.assertTrue({"n10", "s03", "a04"}.issubset(domains))

    def test_06_chinese_intent(self):
        self.assertTrue(SEARCH(ROWS, "重建", exact=True))

    def test_07_normalized_english(self):
        self.assertEqual(SEARCH(ROWS, " ＲＥＢＵＩＬＤ ", exact=True), SEARCH(ROWS, "rebuild", exact=True))

    def test_08_exact_excludes_substrings(self):
        self.assertFalse(SEARCH(ROWS, "rebu", exact=True))
        self.assertTrue(SEARCH(ROWS, "rebu"))

    def test_09_empty_query(self):
        with self.assertRaises(ValueError):
            SEARCH(ROWS, "\u3000  ")

    def test_10_unknown_domain(self):
        with self.assertRaisesRegex(ValueError, "Unknown domain"):
            SEARCH(ROWS, "rebuild", "../private")

    def test_11_deterministic_no_mutation(self):
        before = json.dumps(ROWS, ensure_ascii=False)
        self.assertEqual(SEARCH(ROWS, "rebuild"), SEARCH(list(reversed(ROWS)), "rebuild"))
        self.assertEqual(json.dumps(ROWS, ensure_ascii=False), before)

    def test_12_complete_fields(self):
        for row in ROWS:
            self.assertTrue(all(row[f].strip() for f in API["FIELDS"]))
            for code in row["evidence"].split(";"):
                self.assertIn(code.strip(), API["EVIDENCE"])

    def test_13_missing_boundary_rejected(self):
        def blank(text):
            lines = text.splitlines()
            i = next(i for i, line in enumerate(lines) if 'id="u-g01-01"' in line)
            cells = lines[i].split("|")
            cells[-3] = " "
            lines[i] = "|".join(cells)
            return "\n".join(lines)
        with self.assertRaisesRegex(ValueError, "nonempty"):
            self.changed("references/usage/general.md", blank, lambda: READ(ROOT))

    def test_14_missing_domain_row_rejected(self):
        with self.assertRaisesRegex(ValueError, "coverage"):
            self.changed("references/usage/general.md",
                         lambda s: re.sub(r'^.*id="u-g01-01".*\n', "", s, flags=re.M), lambda: READ(ROOT))

    def test_15_unknown_evidence_rejected(self):
        with self.assertRaisesRegex(ValueError, "evidence"):
            self.changed("references/usage/general.md", lambda s: s.replace("| E |", "| X99 |", 1), lambda: READ(ROOT))

    def test_16_cli_text_and_json(self):
        data = self.cli("rebuild", "--exact", "--limit", "1")
        plain = self.cli("rebuild", "--exact", "--limit", "1", "--format", "text")
        self.assertEqual(data.returncode, 0, data.stderr)
        self.assertEqual(plain.returncode, 0, plain.stderr)
        result = json.loads(data.stdout)
        self.assertGreater(result["total_matches"], 1)
        self.assertEqual(result["shown"], 1)
        for field in ("boundary", "evidence", "path"):
            self.assertIn(result["results"][0][field], plain.stdout.decode("utf-8"))

    def test_17_cli_domains(self):
        proc = self.cli("--list-domains")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(len(json.loads(proc.stdout)["domains"]), 52)

    def test_18_cli_bad_arguments(self):
        for args in (("a", "--domain", "bad"), ("a", "--limit", "0"), ("a", "--format", "html"), ()):
            self.assertEqual(self.cli(*args).returncode, 2)

    def test_19_cli_no_match(self):
        proc = self.cli("zz-not-a-usage-zz", "--format", "text")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("No match.", proc.stdout.decode("utf-8"))

    def test_20_cli_utf8(self):
        proc = self.cli("重建", env=dict(os.environ, PYTHONIOENCODING="ascii"))
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertTrue(json.loads(proc.stdout.decode("utf-8"))["results"])

    def test_21_read_only(self):
        def snapshot():
            return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in ROOT.rglob("*") if p.is_file()}
        before = snapshot()
        self.assertEqual(self.cli("rebuild", "--exact").returncode, 0)
        self.assertEqual(snapshot(), before)

    def test_22_forty_journals(self):
        report = CHECK(ROOT)
        self.assertTrue(report["ok"], report["errors"])
        self.assertEqual(report["stats"]["journal_cards"], 40)
        self.assertEqual(report["stats"]["usage_records"], 208)

    def test_23_missing_journal_rejected(self):
        report = self.changed("references/journal-cards.md", lambda s: s.replace('<a id="j40"></a>', ""), lambda: CHECK(ROOT))
        self.assertFalse(report["ok"])
        self.assertIn("Journal card set differs", report["errors"])

    def test_24_missing_scope_rejected(self):
        report = self.changed("references/journal-cards.md", lambda s: s.replace("- 核验范围：", "- 范围：", 1), lambda: CHECK(ROOT))
        self.assertFalse(report["ok"])
        self.assertTrue(any("missing - 核验范围" in e for e in report["errors"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
