"""Read-only offline lookup of discipline-sensitive wording and collocations."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import runpy
import sys

normalize = runpy.run_path(str(Path(__file__).with_name("search_terms.py")))["normalize"]
FILES = {"general", "natural-sciences", "engineering", "health", "agriculture",
         "social-sciences", "humanities"}
FIELDS = ("candidates", "intent", "collocations", "condition", "example", "boundary", "evidence")
EVIDENCE = {"E"} | {f"S{i:02d}" for i in range(1, 9)}


def read_records(root):
    root = Path(root)
    manifest = json.loads((root / "bundle-manifest.json").read_text(encoding="utf-8-sig"))
    domains = {d["id"]: d for d in manifest["domains"]}
    folder = root / "references" / "usage"
    paths = sorted(folder.glob("*.md"))
    if {p.stem for p in paths} != FILES:
        raise ValueError("Usage volume set differs")
    records = []
    seen = set()
    for path in paths:
        domain_id = None
        for line in path.read_text(encoding="utf-8-sig").splitlines():
            heading = re.fullmatch(r'## ([a-z]\d{2}) (.+)', line)
            if heading:
                domain_id = heading[1]
                if domain_id not in domains or heading[2] != domains[domain_id]["zh"]:
                    raise ValueError("Unknown or mismatched usage domain: " + domain_id)
            if '<a id="u-' not in line:
                continue
            cells = [x.strip() for x in line.strip().strip("|").split("|")]
            if len(cells) != 7 or any(not x for x in cells):
                raise ValueError("Usage row must contain seven nonempty fields: " + path.name)
            anchor = re.fullmatch(r'<a id="(u-([a-z]\d{2})-\d{2})"></a>(.+)', cells[0])
            if not anchor or anchor[2] != domain_id or anchor[1] in seen:
                raise ValueError("Invalid or duplicate usage anchor: " + path.name)
            seen.add(anchor[1])
            cells[0] = anchor[3].strip()
            candidates = [x.strip() for x in cells[0].split(" / ")]
            if len(candidates) < 2 or any(not x for x in candidates):
                raise ValueError("Usage row needs at least two candidates: " + anchor[1])
            if any(code.strip() not in EVIDENCE for code in cells[-1].split(";")):
                raise ValueError("Unknown usage evidence code: " + cells[-1])
            domain = domains[domain_id]
            row = dict(zip(FIELDS, cells))
            row.update(domain_id=domain_id, domain=domain["zh"], slug=domain["slug"],
                       path="references/usage/" + path.name + "#" + anchor[1])
            records.append(row)
    counts = Counter(row["domain_id"] for row in records)
    if set(counts) != set(domains) or any(n != 4 for n in counts.values()):
        raise ValueError("Usage domain coverage must contain four rows per domain")
    if len(records) != manifest.get("usage_records") or len(counts) != manifest.get("usage_domains"):
        raise ValueError("Usage counts differ from manifest")
    return records


def search(records, query, domain=None, exact=False):
    key = normalize(query)
    if not key:
        raise ValueError("Query must not be blank")
    if domain and domain not in {r[k] for r in records for k in ("domain_id", "slug")}:
        raise ValueError("Unknown domain; use --list-domains")
    found = []
    for row in records:
        if domain and domain not in {row["domain_id"], row["slug"]}:
            continue
        heads = [normalize(c) for c in row["candidates"].split(" / ")]
        heads += [normalize(c) for c in row["intent"].split("、")]
        direct = key in heads
        if direct or (not exact and key in normalize(" ".join(row[f] for f in FIELDS[:-1]))):
            found.append((0 if direct else 1, row))
    return [row for _, row in sorted(found, key=lambda x: (x[0], x[1]["path"]))]


def render_text(result):
    if "domains" in result:
        return "\n".join([f"Domains: {len(result['domains'])}"] +
                         [" | ".join(d) for d in result["domains"]])
    lines = [f"Query: {result['query']}",
             f"Matches: {result['total_matches']} | Shown: {result['shown']}"]
    if not result["results"]:
        lines.append("No match. Try another wording or consult author-supplied sources.")
    for i, row in enumerate(result["results"], 1):
        lines += ["", f"{i}. {row['candidates']} | {row['intent']}",
                  f"Domain: {row['domain']} ({row['domain_id']}, {row['slug']})"]
        lines += [f"{field}: {row[field]}" for field in FIELDS[2:]]
        lines += [f"Source: {row['path']}"]
    return "\n".join(lines + ["", result["note"]])


def main():
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="?", default="")
    parser.add_argument("--domain", help="Domain ID or slug")
    parser.add_argument("--exact", action="store_true", help="Match a whole candidate or Chinese intent")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--list-domains", action="store_true")
    parser.add_argument("--format", choices=("json", "text"), default="json")
    args = parser.parse_args()
    if not 1 <= args.limit <= 200:
        parser.error("--limit must be between 1 and 200")
    try:
        records = read_records(Path(__file__).resolve().parents[1])
        if args.domain and args.domain not in {r[k] for r in records for k in ("domain_id", "slug")}:
            raise ValueError("Unknown domain; use --list-domains")
        if args.list_domains:
            result = {"domains": sorted({(r["domain_id"], r["slug"], r["domain"]) for r in records})}
        else:
            found = search(records, args.query, args.domain, args.exact)
            result = {"query": args.query, "total_matches": len(found), "shown": min(len(found), args.limit),
                      "results": found[:args.limit],
                      "note": "Editorial usage aids and original examples, not frequency claims. "
                              "Check the evidence ledger and author sources before changing meaning."}
        print(render_text(result) if args.format == "text" else json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
