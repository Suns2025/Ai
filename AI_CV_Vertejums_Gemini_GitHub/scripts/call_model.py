import os, json, re
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("GEMINI_API_KEY nav atrasts (.env fails nav pievienots).")
    def call_model(prompt_text: str):
        return '{"match_score": 0, "summary": "Demo režīms — nav AI atbildes.", "strengths": [], "missing_requirements": [], "verdict": "not a match"}'
else:
    genai.configure(api_key=api_key)
    def call_model(prompt_text: str):
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt_text, generation_config={"temperature": 0.3})
        content = response.text.strip()
        match = re.search(r'(\{.*\})', content, re.S)
        return match.group(1) if match else content

def main(prompt_path, out_json_path):
    prompt_text = Path(prompt_path).read_text(encoding="utf-8")
    raw = call_model(prompt_text)
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        match = re.search(r'(\{.*\})', raw, re.S)
        if not match:
            raise
        data = json.loads(match.group(1))
    Path(out_json_path).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saglabāts: {out_json_path}")

if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2])
