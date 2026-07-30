import boto3
from pathlib import Path

# ============================================
# AWS Configuration
# ============================================

BUCKET_NAME = "sergio-vindel-enterprise-data-pipeline"

FILES = {
    "input/customers_raw.csv": "raw/customers_raw.csv",
    "input/customers_dirty.csv": "dirty/customers_dirty.csv",
    "output/customers_clean.csv": "clean/customers_clean.csv",
    "output/data_quality_report.xlsx": "reports/data_quality_report.xlsx",
}

# ============================================
# Create S3 Client
# ============================================

s3 = boto3.client("s3")

print("=" * 60)
print("UPLOADING FILES TO AWS S3")
print("=" * 60)

for local_file, s3_key in FILES.items():

    path = Path(local_file)

    if not path.exists():
        print(f"❌ File not found: {local_file}")
        continue

    print(f"\nUploading {path.name}...")

    s3.upload_file(
        Filename=str(path),
        Bucket=BUCKET_NAME,
        Key=s3_key
    )

    print(f"✅ Uploaded to s3://{BUCKET_NAME}/{s3_key}")

print("\n" + "=" * 60)
print("ALL FILES UPLOADED SUCCESSFULLY")
print("=" * 60)