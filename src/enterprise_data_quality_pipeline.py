import json
import re
from pathlib import Path

import pandas as pd

# ==========================================
# Load configuration
# ==========================================

CONFIG_PATH = Path("config/config.json")

with open(CONFIG_PATH, "r") as file:
    config = json.load(file)

INPUT_FILE = config["dirty_output_file"]
OUTPUT_FILE = config["clean_output_file"]

# ==========================================
# Load dataset
# ==========================================

def load_dataset():

    print("\n[1/6] Loading dataset...")

    df = pd.read_csv(INPUT_FILE)

    print(f"Records loaded: {len(df):,}")

    return df

# ==========================================
# Standardize names
# ==========================================

def standardize_names(df):

    print("\n[2/6] Standardizing customer names...")

    df["CustomerName"] = (
        df["CustomerName"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    df["ContactName"] = (
        df["ContactName"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    return df

# ==========================================
# Email validation
# ==========================================

def validate_emails(df):

    print("\n[3/6] Validating email addresses...")

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    valid = df["Email"].fillna("").str.match(pattern)

    invalid_count = (~valid).sum()

    print(f"Invalid emails detected: {invalid_count:,}")

    df = df[valid]

    return df

# ==========================================
# Remove duplicates
# ==========================================

def remove_duplicates(df):

    print("\n[4/6] Removing duplicate customers...")

    before = len(df)

    df = df.drop_duplicates(
        subset=[
            "CustomerName",
            "Email"
        ]
    )

    removed = before - len(df)

    print(f"Duplicates removed: {removed:,}")

    return df

# ==========================================
# Missing values
# ==========================================

def handle_missing_values(df):

    print("\n[5/6] Handling missing values...")

    before = len(df)

    df = df.dropna()

    removed = before - len(df)

    print(f"Rows removed: {removed:,}")

    return df

# ==========================================
# Export
# ==========================================

def export_dataset(df):

    print("\n[6/6] Exporting clean dataset...")

    Path("output").mkdir(exist_ok=True)

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(f"Dataset exported to: {OUTPUT_FILE}")

# ==========================================
# Main
# ==========================================

def main():

    print("=" * 55)
    print("ENTERPRISE DATA QUALITY PIPELINE")
    print("=" * 55)

    df = load_dataset()

    df = standardize_names(df)

    df = validate_emails(df)

    df = remove_duplicates(df)

    df = handle_missing_values(df)

    export_dataset(df)

    print("\nPipeline completed successfully!")

    print(f"Final records: {len(df):,}")

if __name__ == "__main__":
    main()