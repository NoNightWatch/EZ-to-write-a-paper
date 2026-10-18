"""Run offline structural and search regression tests without changing bundle files."""
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
validator = runpy.run_path(str(ROOT / "scripts" / "validate_bundle.py"))
searcher = runpy.run_path(str(ROOT / "scripts" / "search_terms.py"))
CHECK = validator["check_bundle"]
RECORDS = searcher["read_records"](ROOT)
SEARCH = searcher["search"]
REAL_READ = Path.read_text

class BundleTests(unittest.TestCase):
    def modified(self, changes):
        normalized = {str((ROOT / k).resolve()): v for k, v in changes.items()}
        def read(path, *args, **kwargs):
            content = REAL_READ(path, *args, **kwargs)
            fn = normalized.get(str(path.resolve()))
            return fn(content) if fn else content
        with patch.object(Path, "read_text", read):
            return CHECK(ROOT)

    def require_failure(self, changes, contains):
        result = self.modified(changes)
        self.assertFalse(result["ok"])
        self.assertTrue(any(contains in e for e in result["errors"]), result["errors"])

    def test_01_baseline(self):
        result = CHECK(ROOT)
        self.assertTrue(result["ok"], result["errors"])

    def test_02_layer_counts(self):
        self.assertEqual(sum(r["layer"] == "foundation" for r in RECORDS), 2080)
        self.assertEqual(sum(r["layer"] == "detailed" for r in RECORDS), 308)

    def test_03_unique_heads(self):
        self.assertEqual(len({r["english"].casefold() for r in RECORDS if r["layer"] == "foundation"}), 2043)

    def test_04_validity_senses(self):
        rows = SEARCH(RECORDS, "validity", exact=True)
        self.assertEqual({r["domain_id"] for r in rows}, {"s05", "h02"})

    def test_05_soc_senses(self):
        self.assertEqual({r["domain_id"] for r in SEARCH(RECORDS, "SOC", exact=True)}, {"e07", "a02"})

    def test_06_domain_filter(self):
        rows = SEARCH(RECORDS, "SOC", domain="e07", exact=True)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["english"], "state of charge")

    def test_07_npv_senses(self):
        heads = {r["english"] for r in SEARCH(RECORDS, "NPV", exact=True)}
        self.assertIn("net present value", heads)
        self.assertIn("negative predictive value", heads)

    def test_08_chinese_search(self):
        self.assertTrue(SEARCH(RECORDS, "反身性", exact=True))

    def test_09_legacy_search(self):
        self.assertTrue(any(r["layer"] == "detailed" for r in SEARCH(RECORDS, "qSIP")))

    def test_10_empty_query(self):
        with self.assertRaises(ValueError):
            SEARCH(RECORDS, "  ")

    def test_11_no_match(self):
        self.assertEqual(SEARCH(RECORDS, "zz-unlisted-term-zz", exact=True), [])

    def test_12_missing_link(self):
        self.require_failure({"SKILL.md": lambda s: s + "\n[missing](references/missing.md)\n"}, "Missing link")

    def test_13_missing_anchor(self):
        self.require_failure({"SKILL.md": lambda s: s + "\n[anchor](references/beginner-guide.md#absent)\n"}, "Missing explicit anchor")

    def test_14_private_path(self):
        self.require_failure({"SKILL.md": lambda s: s + "\nQ:/private-example/secret.txt\n"}, "Machine-specific path")

    def test_15_escaping_link(self):
        self.require_failure({"SKILL.md": lambda s: s + "\n[escape](../../outside.md)\n"}, "Link escapes bundle")

    def test_16_missing_term(self):
        self.require_failure({"references/terms/mathematics.md":
                              lambda s: re.sub(r'^\| <a id="t01"></a>.*\n', "", s, flags=re.M)},
                             "Foundation count/anchor mismatch")

    def test_17_duplicate_headword(self):
        self.require_failure({"references/terms/mathematics.md": lambda s: s.replace("</a>element |", "</a>set |")},
                             "Duplicate English headword")

    def test_18_index_repeat(self):
        self.require_failure({"references/foundation-index.md":
                              lambda s: s + "\n[set](terms/mathematics.md#t01)\n"},
                             "Foundation index is not one-to-one")

    def test_19_invalid_manifest(self):
        self.require_failure({"bundle-manifest.json": lambda s: "not-json"},
                             "Missing or invalid bundle manifest")

    def test_20_manifest_count(self):
        self.require_failure({"bundle-manifest.json": lambda s: s.replace('"foundation_term_records": 2080',
                                                                               '"foundation_term_records": 2081')},
                             "Expected 2080")

    def test_21_domain_id_collision(self):
        self.require_failure({"bundle-manifest.json": lambda s: s.replace('"id": "g02"', '"id": "g01"')},
                             "Duplicate domain ID")

    def test_22_legacy_index_repeat(self):
        self.require_failure({"references/glossary-index.md":
                              lambda s: s + "\n[term](glossary/research-design-statistics.md#term-01)\n"},
                             "English index is not a one-to-one")

    def test_23_cli_list(self):
        proc = subprocess.run([sys.executable, "-X", "utf8", str(ROOT / "scripts" / "search_terms.py"),
                               "--list-domains"], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(len(json.loads(proc.stdout)["domains"]), 61)

    def test_24_cli_unknown_domain(self):
        proc = subprocess.run([sys.executable, "-X", "utf8", str(ROOT / "scripts" / "search_terms.py"),
                               "test", "--domain", "../../not-a-domain"],
                              capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(proc.returncode, 2)
        self.assertIn("Unknown domain", proc.stderr)

    def test_25_missing_root(self):
        self.assertFalse(CHECK(ROOT / "nonexistent-bundle")["ok"])

    def test_26_cli_limit(self):
        proc = subprocess.run([sys.executable, "-X", "utf8", str(ROOT / "scripts" / "search_terms.py"),
                               "state", "--limit", "0"], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(proc.returncode, 2)

    def test_27_fullwidth_abbreviation(self):
        self.assertEqual(SEARCH(RECORDS, "ＳＯＣ", exact=True), SEARCH(RECORDS, "SOC", exact=True))
        self.assertEqual(len(SEARCH(RECORDS, "ＳＯＣ", exact=True)), 2)

    def test_28_unicode_hyphens(self):
        expected = SEARCH(RECORDS, "life-cycle assessment", exact=True)
        self.assertTrue(expected)
        for query in ("life\u2010cycle assessment", "life\u2011cycle assessment", "ＬＣＡ"):
            self.assertEqual(SEARCH(RECORDS, query, exact=True), expected)

    @staticmethod
    def term(english, path="test.md#one", meaning="", domain="test"):
        return {"english": english, "chinese": "", "meaning": meaning,
                "path": path, "slug": domain, "domain_id": domain}

    def test_29_canonical_accent(self):
        rows = [self.term("caf\u00e9")]
        self.assertEqual(SEARCH(rows, "cafe\u0301", exact=True), rows)

    def test_30_preserve_scientific_symbols(self):
        for marked, plain in (("R²", "R2"), ("CO₂", "CO2"), ("x−y", "x-y")):
            rows = [self.term(marked, "a.md"), self.term(plain, "b.md")]
            self.assertEqual(SEARCH(rows, marked, exact=True), [rows[0]])
            self.assertEqual(SEARCH(rows, plain, exact=True), [rows[1]])

    def test_31_headword_before_meaning_match(self):
        incidental = self.term("unrelated", "a.md", "This mentions target.")
        headword = self.term("target", "z.md")
        self.assertEqual(SEARCH([incidental, headword], "target"), [headword, incidental])
        self.assertEqual(SEARCH([incidental, headword], "target", exact=True), [headword])

    def test_32_literal_query(self):
        rows = [self.term("a+b"), self.term("ab", "b.md")]
        self.assertEqual(SEARCH(rows, "a+b", exact=True), [rows[0]])

    def test_33_cli_limit_preserves_total(self):
        proc = subprocess.run([sys.executable, "-B", "-X", "utf8", str(ROOT / "scripts" / "search_terms.py"),
                               "SOC", "--exact", "--limit", "1"],
                              capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        result = json.loads(proc.stdout)
        self.assertEqual((result["total_matches"], result["shown"], len(result["results"])), (2, 1, 1))

    def test_34_cli_utf8_with_ascii_environment(self):
        env = dict(os.environ, PYTHONIOENCODING="ascii")
        proc = subprocess.run([sys.executable, "-B", str(ROOT / "scripts" / "search_terms.py"),
                               "SOC", "--exact"], capture_output=True, env=env)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        result = json.loads(proc.stdout.decode("utf-8"))
        self.assertEqual(result["total_matches"], 2)
        self.assertTrue(any(r["chinese"] for r in result["results"]))

    def test_35_unicode_blank_query(self):
        with self.assertRaises(ValueError):
            SEARCH(RECORDS, "\u3000\u00a0\t")

    def test_36_missing_search_root(self):
        with self.assertRaises(OSError):
            searcher["read_records"](ROOT / "nonexistent-bundle")

    def test_37_deterministic_tie_order(self):
        rows = [self.term("target", "b.md"), self.term("target", "a.md")]
        self.assertEqual(SEARCH(rows, "target"), SEARCH(list(reversed(rows)), "target"))
        self.assertEqual([r["path"] for r in SEARCH(rows, "target")], ["a.md", "b.md"])

    def test_38_search_does_not_mutate_records(self):
        before = json.dumps(RECORDS, ensure_ascii=False, sort_keys=True)
        for query in ("ＳＯＣ", "life\u2011cycle assessment", "反身性"):
            SEARCH(RECORDS, query)
        self.assertEqual(json.dumps(RECORDS, ensure_ascii=False, sort_keys=True), before)

if __name__ == "__main__":
    unittest.main(verbosity=2)
