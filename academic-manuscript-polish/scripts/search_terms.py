"""Read-only offline search across the bundle's foundation and detailed terms."""
import argparse
import json
from pathlib import Path
import re
import sys
import unicodedata

ROW = re.compile(r'^\| <a id="(t\d{2})"></a>([^|]+)\|([^|]+)\|([^|]+)\|$', re.M)
ALIASES = {
    "cdna": ["complementary dna"],
    "mrna": ["messenger rna"],
    "rrna": ["ribosomal rna"],
    "trna": ["transfer rna"],
    "soc": ["soil organic carbon", "state of charge"],
    "som": ["soil organic matter"],
    "pom": ["particulate organic matter"],
    "maom": ["mineral-associated organic matter"],
    "doc": ["dissolved organic carbon"],
    "mbc": ["microbial biomass carbon"],
    "cue": ["carbon use efficiency"],
    "cec": ["cation exchange capacity"],
    "lai": ["leaf area index"],
    "dbh": ["diameter at breast height"],
    "cpue": ["catch per unit effort"],
    "msy": ["maximum sustainable yield"],
    "fcr": ["feed conversion ratio"],
    "gis": ["geographic information system"],
    "snr": ["signal-to-noise ratio"],
    "ber": ["bit error rate"],
    "mpc": ["model predictive control"],
    "bim": ["building information modelling"],
    "lca": ["life-cycle assessment"],
    "lcoe": ["levelized cost of energy"],
    "cop": ["coefficient of performance"],
    "hrt": ["hydraulic retention time"],
    "srt": ["solids retention time"],
    "bod": ["biochemical oxygen demand"],
    "cod": ["chemical oxygen demand"],
    "toc": ["total organic carbon"],
    "tss": ["total suspended solids"],
    "ppv": ["positive predictive value"],
    "npv": ["negative predictive value", "net present value"],
    "nnt": ["number needed to treat"],
    "pk": ["pharmacokinetics"],
    "pd": ["pharmacodynamics"],
    "auc": ["area under the curve"],
    "adl": ["activities of daily living"],
    "iadl": ["instrumental activities of daily living"],
    "gdp": ["gross domestic product"],
    "tfp": ["total factor productivity"],
    "ppp": ["purchasing power parity"],
    "npv-finance": ["net present value"],
    "doi": ["digital object identifier"],
    "rag": ["retrieval-augmented generation"],
    "maup": ["modifiable areal unit problem"],
    "ecs": ["equilibrium climate sensitivity"],
    "tcr": ["transient climate response"],
}

SEARCH_EQUIVALENTS = {code: code - 0xFEE0 for code in range(0xFF01, 0xFF5F)}
SEARCH_EQUIVALENTS.update({0x2010: ord("-"), 0x2011: ord("-")})

def normalize(value):
    """Accept common typing variants without flattening scientific notation."""
    value = unicodedata.normalize("NFC", value).translate(SEARCH_EQUIVALENTS)
    return " ".join(value.casefold().split())

def read_records(root):
    root = Path(root)
    manifest = json.loads((root / "bundle-manifest.json").read_text(encoding="utf-8-sig"))
    records = []
    for domain in manifest["domains"]:
        slug = domain["slug"]
        if not re.fullmatch(r"[a-z0-9-]+", slug):
            raise ValueError("Invalid domain slug")
        path = root / "references" / "terms" / (slug + ".md")
        for anchor, en, zh, meaning in ROW.findall(path.read_text(encoding="utf-8-sig")):
            records.append({
                "layer": "foundation", "domain_id": domain["id"], "domain": domain["zh"],
                "slug": slug, "english": en.strip(), "chinese": zh.strip(),
                "meaning": meaning.strip(),
                "path": "references/terms/" + slug + ".md#" + anchor,
            })
    for path in sorted((root / "references" / "glossary").glob("*.md")):
        content = path.read_text(encoding="utf-8-sig")
        for match in re.finditer(r'<a id="(term-\d{2})"></a>\s*\n## \d{2} (.*?)\n(.*?)(?=\n<a id="term-|\Z)', content, re.S):
            anchor, title, body = match.groups()
            english = re.search(r"^英文：(.+)$", body, re.M)
            records.append({
                "layer": "detailed", "domain_id": "legacy", "domain": path.stem,
                "slug": path.stem, "english": english.group(1).strip() if english else "",
                "chinese": title.strip(), "meaning": body.strip(),
                "path": "references/glossary/" + path.name + "#" + anchor,
            })
    return records

def search(records, query, domain=None, exact=False):
    key = normalize(query)
    if not key:
        raise ValueError("Query must not be blank")
    keys = [key] + ALIASES.get(key, [])
    matches = []
    for row in records:
        if domain and domain not in {row["slug"], row["domain_id"]}:
            continue
        fields = [normalize(row["english"]), normalize(row["chinese"])]
        head = any(k in fields for k in keys)
        if head or (not exact and any(k in normalize(" ".join(fields + [row["meaning"]])) for k in keys)):
            rank = 0 if head else 1
            matches.append((rank, row))
    return [row for _, row in sorted(matches, key=lambda item: (item[0], item[1]["path"]))]

def main():
    # JSON is UTF-8 even when redirected from a legacy Windows terminal.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="?", default="", help="Chinese, English, or a supported abbreviation")
    parser.add_argument("--domain", help="Domain ID or slug; use --list-domains to inspect")
    parser.add_argument("--exact", action="store_true", help="Match complete headword or abbreviation mapping")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--list-domains", action="store_true")
    args = parser.parse_args()
    if not 1 <= args.limit <= 200:
        parser.error("--limit must be between 1 and 200")
    root = Path(__file__).resolve().parents[1]
    try:
        records = read_records(root)
        valid = {r["slug"] for r in records} | {r["domain_id"] for r in records}
        if args.domain and args.domain not in valid:
            parser.error("Unknown domain; use --list-domains")
        if args.list_domains:
            domains = sorted({(r["domain_id"], r["slug"], r["domain"]) for r in records})
            result = {"domains": domains}
        else:
            found = search(records, args.query, args.domain, args.exact)
            result = {"query": args.query, "total_matches": len(found), "shown": min(len(found), args.limit),
                      "results": found[:args.limit],
                      "note": "Working reading aids. Confirm specialist meanings in author sources."}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())
