import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from build_index import build_index, main, parse_frontmatter, update_readme


def write_writeup(dir_path, filename, title, platform, category, difficulty, date, tools="nmap"):
    content = (
        f"---\ntitle: {title}\nplatform: {platform}\ncategory: {category}\n"
        f"difficulty: {difficulty}\ndate: {date}\ntools: {tools}\n---\n\n"
        "## Summary\nTest content.\n"
    )
    path = dir_path / filename
    path.write_text(content, encoding="utf-8")
    return path


def test_parse_frontmatter_valid(tmp_path):
    p = write_writeup(tmp_path, "a.md", "Test Room", "TryHackMe", "Web", "Easy", "2026-01-01")
    data = parse_frontmatter(p)
    assert data["title"] == "Test Room"
    assert data["platform"] == "TryHackMe"
    assert data["difficulty"] == "Easy"


def test_parse_frontmatter_missing_returns_empty(tmp_path):
    p = tmp_path / "no_frontmatter.md"
    p.write_text("# Just a heading\nNo frontmatter here.\n", encoding="utf-8")
    assert parse_frontmatter(p) == {}


def test_build_index_row_count(tmp_path):
    d = tmp_path / "writeups"
    d.mkdir()
    write_writeup(d, "a.md", "Room A", "TryHackMe", "Web", "Easy", "2026-01-01")
    write_writeup(d, "b.md", "Room B", "HackTheBox", "Network", "Medium", "2026-02-01")
    table = build_index(d)
    assert "Room A" in table
    assert "Room B" in table
    assert table.count("\n") == 3


def test_build_index_sorted_by_date_desc(tmp_path):
    d = tmp_path / "writeups"
    d.mkdir()
    write_writeup(d, "old.md", "Old Room", "TryHackMe", "Web", "Easy", "2026-01-01")
    write_writeup(d, "new.md", "New Room", "TryHackMe", "Web", "Easy", "2026-03-01")
    table = build_index(d)
    assert table.index("New Room") < table.index("Old Room")


def test_update_readme_replaces_only_marker_section(tmp_path):
    readme = tmp_path / "README.md"
    readme.write_text(
        "# Title\n\nIntro text.\n\n<!-- INDEX:START -->\nold content\n<!-- INDEX:END -->\n\nFooter text.\n",
        encoding="utf-8",
    )
    update_readme(readme, "| new | table |")
    text = readme.read_text(encoding="utf-8")
    assert "new | table" in text
    assert "old content" not in text
    assert "Intro text." in text
    assert "Footer text." in text


def test_format_json_outputs_valid_writeup_list(tmp_path, monkeypatch, capsys):
    d = tmp_path / "writeups"
    d.mkdir()
    write_writeup(d, "a.md", "Room A", "TryHackMe", "Web", "Easy", "2026-01-01")
    readme = tmp_path / "README.md"
    readme.write_text("# T\n<!-- INDEX:START -->\nold\n<!-- INDEX:END -->\n", encoding="utf-8")

    monkeypatch.setattr(
        sys,
        "argv",
        ["build_index.py", "--format", "json", "--writeups-dir", str(d), "--readme", str(readme)],
    )
    main()
    data = json.loads(capsys.readouterr().out)
    assert isinstance(data, list)
    assert data[0]["title"] == "Room A"


def test_format_json_does_not_modify_readme(tmp_path, monkeypatch):
    d = tmp_path / "writeups"
    d.mkdir()
    write_writeup(d, "a.md", "Room A", "TryHackMe", "Web", "Easy", "2026-01-01")
    readme = tmp_path / "README.md"
    original = "# T\n<!-- INDEX:START -->\nold content\n<!-- INDEX:END -->\n"
    readme.write_text(original, encoding="utf-8")
    out_file = tmp_path / "out.json"

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "build_index.py",
            "--format",
            "json",
            "--writeups-dir",
            str(d),
            "--readme",
            str(readme),
            "--output",
            str(out_file),
        ],
    )
    main()
    assert readme.read_text(encoding="utf-8") == original
    data = json.loads(out_file.read_text(encoding="utf-8"))
    assert data[0]["title"] == "Room A"
