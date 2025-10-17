import sys
from pathlib import Path

def build_prompt(jd_path, cv_path, out_path):
    template_path = Path("prompt_templates/prompt.md")
    template = template_path.read_text(encoding="utf-8")
    jd = Path(jd_path).read_text(encoding="utf-8")
    cv = Path(cv_path).read_text(encoding="utf-8")
    filled = template.replace("<<INSERT_JD_TEXT_HERE>>", jd).replace("<<INSERT_CV_TEXT_HERE>>", cv)
    Path(out_path).write_text(filled, encoding="utf-8")
    print(f"Sagatavots prompt: {out_path}")

if __name__ == "__main__":
    build_prompt(sys.argv[1], sys.argv[2], sys.argv[3])
