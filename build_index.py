import argparse
import json
import re
from pathlib import Path

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?\n)---\s*\n", re.DOTALL)
FIELDS = ["title", "platform", "category", "difficulty", "date", "tools"]
INDEX_START = "<!-- INDEX:START -->"
INDEX_END = "<!-- INDEX:END -->"


def parse_frontmatter(md_path: Path) -> dict:
    text = md_path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    data = {}
    for line in match.group(1).splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip().lower()
        if key in FIELDS:
            data[key] = value.strip()
    return data


def collect_writeups(writeups_dir: Path) -> list:
    rows = [d for d in (parse_frontmatter(p) for p in sorted(writeups_dir.glob("*.md"))) if d]
    rows.sort(key=lambda d: d.get("date", ""), reverse=True)
    return rows


def build_index(writeups_dir: Path) -> str:
    rows = collect_writeups(writeups_dir)
    if not rows:
        return "_No writeups yet._"
    lines = ["| Title | Platform | Category | Difficulty | Date |", "|---|---|---|---|---|"]
    for d in rows:
        lines.append(
            f"| {d.get('title', '')} | {d.get('platform', '')} | "
            f"{d.get('category', '')} | {d.get('difficulty', '')} | {d.get('date', '')} |"
        )
    return "\n".join(lines)


def update_readme(readme_path: Path, table_md: str) -> None:
    text = readme_path.read_text(encoding="utf-8")
    start = text.index(INDEX_START) + len(INDEX_START)
    end = text.index(INDEX_END)
    readme_path.write_text(text[:start] + "\n" + table_md + "\n" + text[end:], encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Rebuild the writeup index table in README.md")
    parser.add_argument("--writeups-dir", default="writeups")
    parser.add_argument("--readme", default="README.md")
    parser.add_argument(
        "--format",
        choices=["markdown", "json"],
        default="markdown",
        help="markdown (default): update the README index table. "
        "json: print/write the writeup list as JSON without touching README.md.",
    )
    parser.add_argument(
        "--output", default=None, help="json format only: file to write output to (default: stdout)"
    )
    args = parser.parse_args()

    base = Path(__file__).parent
    writeups_dir = base / args.writeups_dir
    readme_path = base / args.readme

    if args.format == "json":
        rows = collect_writeups(writeups_dir)
        payload = json.dumps(rows, indent=2, ensure_ascii=False)
        if args.output:
            Path(args.output).write_text(payload + "\n", encoding="utf-8")
            print(f"Wrote {len(rows)} writeup(s) to {args.output}")
        else:
            print(payload)
        return

    table_md = build_index(writeups_dir)
    update_readme(readme_path, table_md)
    print(f"Index updated in {readme_path} ({len(list(writeups_dir.glob('*.md')))} writeup(s) found)")


if __name__ == "__main__":
    main()
