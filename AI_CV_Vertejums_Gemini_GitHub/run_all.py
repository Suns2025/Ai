import subprocess
from pathlib import Path

JD_PATH = "sample_inputs/jd.txt"
CV_FILES = ["cv1.txt", "cv2.txt"]

Path("outputs").mkdir(exist_ok=True)

for cv in CV_FILES:
    name = Path(cv).stem
    prompt = f"outputs/{name}_prompt.md"
    json_out = f"outputs/{name}.json"
    report = f"outputs/{name}_report.md"

    print(f"Apstrādā {cv}")
    subprocess.run(["python", "scripts/build_prompt.py", JD_PATH, f"sample_inputs/{cv}", prompt])
    subprocess.run(["python", "scripts/call_model.py", prompt, json_out])
    subprocess.run(["python", "scripts/make_report.py", json_out, report])
