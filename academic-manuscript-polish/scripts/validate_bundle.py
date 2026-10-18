"""Read-only structural checks for this portable writing guide (Python 3)."""
from collections import Counter, deque
import argparse
import ast
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

COUNTS = {
    "research-design-statistics": 36,
    "soil-microbial-ecology": 50,
    "plant-evolution-life-history": 32,
    "molecular-biology-biomedicine": 36,
    "earth-climate-chemistry": 30,
    "mathematics-physics-theoretical-cs": 32,
    "ai-language-software": 32,
    "economics-innovation-policy": 32,
    "psychology-organization-humanities": 28,
}
WRITING = [
    "a-theory", "b-mechanism", "c-causal-effects", "d-hypothesis-tests",
    "e-treatment-responses", "f-mapping-prediction", "g-method-validation",
    "h-measurement-audit", "i-process-reconstruction", "j-synthesis",
]
LINK = re.compile(r"\[[^\]\n]*\]\(([^)\n]+)\)")
HTML_ID = re.compile(r'<a\s+id="([^"]+)"\s*></a>')
MAX_FILES = 160

def check_foundation(root, docs, errors, stats):
    manifest_path = root / "bundle-manifest.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
    except (OSError, ValueError):
        errors.append("Missing or invalid bundle manifest")
        return
    domains = manifest.get("domains", [])
    if len(domains) != 52:
        errors.append("Expected 52 foundation domains")
    slugs = [d.get("slug", "") for d in domains]
    ids = [d.get("id", "") for d in domains]
    if len(set(slugs)) != len(slugs) or len(set(ids)) != len(ids):
        errors.append("Duplicate domain ID or slug")
    if {d.get("group") for d in domains} != {"通用", "自然科学", "工程与技术", "医学与健康", "农业与兽医", "社会科学", "人文与艺术"}:
        errors.append("Foundation discipline-group coverage differs")
    term_dir = root / "references" / "terms"
    if {p.stem for p in term_dir.glob("*.md")} != set(slugs):
        errors.append("Foundation file set differs from manifest")
    row_pattern = re.compile(r'^\| <a id="(t\d{2})"></a>([^|]+)\|([^|]+)\|([^|]+)\|$', re.M)
    expected_links = []
    headwords = []
    actual_count = 0
    for domain in domains:
        slug = domain.get("slug", "")
        if not re.fullmatch(r"[a-z0-9-]+", slug):
            errors.append("Unsafe or invalid domain slug")
            continue
        content = docs.get(term_dir / (slug + ".md"), "")
        rows = row_pattern.findall(content)
        anchors = [r[0] for r in rows]
        expected = [f"t{i:02d}" for i in range(1, 41)]
        if domain.get("count") != 40 or anchors != expected:
            errors.append("Foundation count/anchor mismatch: " + slug)
        heads = [r[1].strip().casefold() for r in rows]
        if len(heads) != len(set(heads)):
            errors.append("Duplicate English headword within domain: " + slug)
        if any(not value.strip() for row in rows for value in row):
            errors.append("Empty foundation term field: " + slug)
        actual_count += len(rows)
        headwords.extend(heads)
        expected_links.extend("terms/" + slug + ".md#" + anchor for anchor in expected)
    if actual_count != 2080 or manifest.get("foundation_term_records") != actual_count:
        errors.append("Expected 2080 foundation records")
    if manifest.get("unique_english_headwords") != len(set(headwords)):
        errors.append("Unique English headword count differs from manifest")
    index = docs.get(root / "references" / "foundation-index.md", "")
    actual_links = [x for x in LINK.findall(index) if x.startswith("terms/")]
    if Counter(actual_links) != Counter(expected_links):
        errors.append("Foundation index is not one-to-one")
    practice = docs.get(root / "references" / "domain-practice.md", "")
    if Counter(HTML_ID.findall(practice)) != Counter(ids):
        errors.append("Domain example coverage differs")
    journal = docs.get(root / "references" / "journal-cards.md", "")
    if re.findall(r'<a id="(j\d{2})"></a>', journal) != [f"j{i:02d}" for i in range(1, 16)]:
        errors.append("Journal card set differs")
    worked = docs.get(root / "references" / "worked-examples.md", "")
    if len(re.findall(r"^## \d+\.", worked, re.M)) != 12:
        errors.append("Expected 12 worked editing examples")
    stats.update(foundation_domains=len(domains), foundation_term_records=actual_count,
                 unique_english_headwords=len(set(headwords)), journal_cards=15,
                 domain_examples=len(HTML_ID.findall(practice)))

def check_bundle(root):
    root = Path(root).resolve()
    errors = []
    warnings = []
    stats = {}
    if not root.is_dir():
        return {"ok": False, "errors": ["Bundle folder not found"], "warnings": [], "stats": {}}
    files = sorted(p for p in root.rglob("*") if p.is_file())
    if len(files) > MAX_FILES:
        errors.append("Unexpected file count; inspect for manuscript data or build artifacts")
    allowed = {".md", ".yaml", ".py", ".json"}
    for p in files:
        if p.suffix.lower() not in allowed:
            errors.append("Unexpected distribution file: " + str(p.relative_to(root)))
        if p.is_symlink() or not p.resolve().is_relative_to(root):
            errors.append("File escapes bundle: " + str(p))
    docs = {p.resolve(): p.read_text(encoding="utf-8-sig") for p in files if p.suffix == ".md"}
    stats["files"] = len(files)
    stats["markdown_files"] = len(docs)
    stats["bytes"] = sum(p.stat().st_size for p in files)
    entry_path = root / "SKILL.md"
    if entry_path not in docs:
        errors.append("SKILL.md is missing")
    else:
        entry = docs[entry_path]
        front = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", entry, re.S)
        if not front:
            errors.append("SKILL.md frontmatter is missing")
        else:
            fields = front.group(1)
            name = re.search(r"^name:\s*(.+)$", fields, re.M)
            desc = re.search(r"^description:\s*(.+)$", fields, re.M)
            if not name or name.group(1).strip() != "academic-manuscript-polish":
                errors.append("Unexpected guide identifier")
            if not desc or len(desc.group(1).strip()) < 20:
                errors.append("Description is missing or uninformative")
    total_terms = 0
    expected_index_links = []
    glossary_dir = root / "references" / "glossary"
    actual_glossaries = {p.stem for p in glossary_dir.glob("*.md")}
    if actual_glossaries != set(COUNTS):
        errors.append("Glossary volume set differs from the release manifest")
    for key, expected in COUNTS.items():
        p = glossary_dir / (key + ".md")
        s = docs.get(p, "")
        numbers = re.findall(r"^## (\d{2}) ", s, re.M)
        anchors = re.findall(r'<a id="term-(\d{2})"></a>', s)
        target = [f"{i:02d}" for i in range(1, expected + 1)]
        if numbers != target or anchors != target:
            errors.append("Term order/count/anchors differ: " + key)
        for label in ("英文：", "- 论文用法：", "- 易混边界：", "- 依据与用例："):
            if s.count(label) != expected:
                errors.append("Missing term field " + label + " in " + key)
        total_terms += len(numbers)
        expected_index_links.extend(f"glossary/{key}.md#term-{n}" for n in target)
    stats["legacy_detailed_terms"] = total_terms
    stats["glossary_volumes"] = len(actual_glossaries)
    if total_terms != 308:
        errors.append("Expected 308 terms")
    index = docs.get(root / "references" / "glossary-index.md", "")
    actual_index_links = [x for x in LINK.findall(index) if x.startswith("glossary/")]
    if Counter(actual_index_links) != Counter(expected_index_links):
        errors.append("English index is not a one-to-one index of all terms")
    writing_dir = root / "references" / "writing"
    if {p.stem for p in writing_dir.glob("*.md")} != set(WRITING):
        errors.append("Writing archetype file set differs from the release manifest")
    for i, key in enumerate(WRITING):
        s = docs.get(writing_dir / (key + ".md"), "")
        letter = chr(65 + i)
        if not s.startswith("# " + letter + " "):
            errors.append("Archetype title missing: " + key)
        for n in range(1, 6):
            if not re.search(r"^## " + letter + str(n) + r" ", s, re.M):
                errors.append("Archetype guidance section missing: " + key + "/" + str(n))
    stats["writing_archetypes"] = len(list(writing_dir.glob("*.md")))
    check_foundation(root, docs, errors, stats)
    graph = {}
    internal_links = 0
    anchors_by_file = {p: set(HTML_ID.findall(s)) for p, s in docs.items()}
    for p, s in docs.items():
        rel = str(p.relative_to(root))
        anchors = HTML_ID.findall(s)
        if len(anchors) != len(set(anchors)):
            errors.append("Duplicate explicit anchor: " + rel)
        if "[[" in s:
            errors.append("Unconverted wikilink: " + rel)
        if re.search(r"(?i)(?:(?<![a-z])[a-z]:[\\/]|file://|obsidian://)", s):
            errors.append("Machine-specific path: " + rel)
        if re.search(r"(?i)(?:\[\[raw/|\[\[wiki/|C:/Users/)", s):
            errors.append("Private source path: " + rel)
        if re.search(r"\\[\(\)\[\]]", s):
            errors.append("Nonportable math delimiter: " + rel)
        if len(re.findall(r"(?<!\\)\$", s)) % 2:
            errors.append("Odd dollar delimiter count: " + rel)
        graph[p] = set()
        for raw_target in LINK.findall(s):
            target = raw_target.strip().strip("<>")
            parts = urlsplit(target)
            if parts.scheme in ("https", "http", "mailto"):
                continue
            if parts.scheme or target.startswith("/"):
                errors.append("Unsupported link scheme/path in " + rel + ": " + target)
                continue
            qpath, _, anchor = target.partition("#")
            dest = (p.parent / unquote(qpath)).resolve() if qpath else p
            internal_links += 1
            if not dest.is_relative_to(root):
                errors.append("Link escapes bundle in " + rel + ": " + target)
            elif not dest.is_file():
                errors.append("Missing link in " + rel + ": " + target)
            elif anchor and unquote(anchor) not in anchors_by_file.get(dest, set()):
                errors.append("Missing explicit anchor in " + rel + ": " + target)
            if dest in docs:
                graph[p].add(dest)
    stats["internal_links"] = internal_links
    reached = set()
    queue = deque([entry_path])
    while queue:
        p = queue.popleft()
        if p not in reached:
            reached.add(p)
            queue.extend(graph.get(p, set()) - reached)
    for p in docs:
        if p not in reached and p != root / "README.md":
            errors.append("Markdown resource unreachable from SKILL.md: " + str(p.relative_to(root)))
    for p in files:
        if p.suffix == ".py":
            try:
                ast.parse(p.read_text(encoding="utf-8-sig"))
            except SyntaxError as exc:
                errors.append("Python syntax error: " + str(exc))
    ui = root / "agents" / "openai.yaml"
    if not ui.exists():
        errors.append("UI metadata missing")
    else:
        ui_text = ui.read_text(encoding="utf-8-sig")
        if "$academic-manuscript-polish" not in ui_text:
            errors.append("UI default prompt does not name the guide")
        short = re.search(r'^\s+short_description:\s*"([^"]+)"', ui_text, re.M)
        if not short or not 25 <= len(short.group(1)) <= 64:
            errors.append("UI short description length must be 25 to 64 characters")
    warnings.append("Static checks do not establish scientific accuracy, editing quality, or host behavior.")
    return {"ok": not errors, "errors": errors, "warnings": warnings, "stats": stats}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    result = check_bundle(args.root)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1

if __name__ == "__main__":
    sys.exit(main())
