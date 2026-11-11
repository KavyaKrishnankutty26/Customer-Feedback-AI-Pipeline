
import subprocess
import sys
from pathlib import Path
import logging


# Find the main project folder
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Create a folder for pipeline logs
LOG_DIR = PROJECT_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=LOG_DIR / "pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

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

logging.info("Customer Feedback AI Pipeline started.")

# Run each script one by one
for script in scripts:

    script_path = PROJECT_ROOT / "src" / script

    print(f"\n[STARTED] Running {script}", flush=True)

    logging.info(f"Started: {script}")

    try:
        subprocess.run(
            [sys.executable, str(script_path)],
            cwd=PROJECT_ROOT,
            check=True
        )

        print(f"[SUCCESS] {script} completed!", flush=True)
        logging.info(f"Successfully completed: {script}")

    except subprocess.CalledProcessError:
        print(f"\n[FAILED] {script} encountered an error.", flush=True)
        logging.error(f"Pipeline failed while running: {script}")

        print("Pipeline stopped. Please check the error above.", flush=True)
        sys.exit(1)

print("\n========== PIPELINE COMPLETED SUCCESSFULLY! ==========", flush=True)
logging.info("Customer Feedback AI Pipeline completed successfully.")
