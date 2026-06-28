import subprocess
import sys
import time

PIPELINE_STEPS = [
    ("Generate Customer Dataset", "src/generate_dataset.py"),
    ("Inject Data Quality Issues", "src/inject_data_quality_issues.py"),
    ("Run Data Quality Pipeline", "src/enterprise_data_quality_pipeline.py"),
    ("Generate Executive Report", "src/quality_report.py")
]


def run_step(step_name, script):
    print("\n" + "=" * 70)
    print(step_name)
    print("=" * 70)

    start = time.time()

    result = subprocess.run(
        [sys.executable, script],
        text=True
    )

    if result.returncode != 0:
        print(f"\n❌ Pipeline failed while executing: {script}")
        sys.exit(1)

    elapsed = time.time() - start

    print(f"\n✅ Completed in {elapsed:.2f} seconds")


def main():

    overall = time.time()

    print("=" * 70)
    print("ENTERPRISE CUSTOMER DATA QUALITY PIPELINE")
    print("=" * 70)

    for name, script in PIPELINE_STEPS:
        run_step(name, script)

    total = time.time() - overall

    print("\n" + "=" * 70)
    print("PIPELINE EXECUTED SUCCESSFULLY")
    print("=" * 70)

    print(f"Total execution time : {total:.2f} seconds")

    print("\nGenerated files:")
    print("✔ input/customers_raw.csv")
    print("✔ input/customers_dirty.csv")
    print("✔ output/customers_clean.csv")
    print("✔ output/data_quality_report.xlsx")

    print("\nProject completed successfully!")


if __name__ == "__main__":
    main()