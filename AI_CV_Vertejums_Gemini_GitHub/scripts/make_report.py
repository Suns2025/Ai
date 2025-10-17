import json
from pathlib import Path

def make_report(json_path, md_path):
    j = json.loads(Path(json_path).read_text(encoding="utf-8"))
    lines = [
        f"# CV atbilstības pārskats",
        "",
        f"**Match score:** {j.get('match_score', 'N/A')}/100",
        f"**Verdict:** {j.get('verdict', 'N/A')}",
        "",
        "## Kopsavilkums",
        j.get("summary", ""),
        "",
        "## Stiprās puses"
    ]
    for s in j.get("strengths", []):
        lines.append(f"- {s}")
    lines += ["", "## Trūkstošās prasmes"]
    for m in j.get("missing_requirements", []):
        lines.append(f"- {m}")
    Path(md_path).write_text("\n".join(lines), encoding="utf-8")
    print(f"Izveidots pārskats: {md_path}")

if __name__ == "__main__":
    import sys
    make_report(sys.argv[1], sys.argv[2])
