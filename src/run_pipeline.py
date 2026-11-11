
import subprocess
import sys
from pathlib import Path

# Find the main project folder
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# List all pipeline scripts in execution order
scripts = [
    "data_inspection.py",
    "data_cleaning.py",
    "sentiment_analysis.py",
    "category_analysis.py",
    "feedback_insights.py",
    "feedback_visualization.py"
]

print("\n========== CUSTOMER FEEDBACK AI PIPELINE ==========", flush=True)

# Run each script one by one
for script in scripts:

    script_path = PROJECT_ROOT / "src" / script

    print(f"\n[STARTED] Running {script}", flush=True)

    try:
        subprocess.run(
            [sys.executable, str(script_path)],
            cwd=PROJECT_ROOT,
            check=True
        )

        print(f"[SUCCESS] {script} completed!", flush=True)

    except subprocess.CalledProcessError:
        print(f"\n[FAILED] {script} encountered an error.", flush=True)
        print("Pipeline stopped. Please check the error above.", flush=True)
        sys.exit(1)

print("\n========== PIPELINE COMPLETED SUCCESSFULLY! ==========", flush=True)
