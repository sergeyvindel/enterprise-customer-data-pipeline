import json
import random
from pathlib import Path

import pandas as pd

# -------------------------------------------------
# Load configuration
# -------------------------------------------------

CONFIG_PATH = Path("config/config.json")

with open(CONFIG_PATH, "r") as file:
    config = json.load(file)

INPUT_FILE = config["raw_output_file"]
OUTPUT_FILE = config["dirty_output_file"]

DUPLICATE_RATE = config["duplicate_rate"]
INVALID_EMAIL_RATE = config["invalid_email_rate"]
MISSING_VALUES_RATE = config["missing_values_rate"]

random.seed(config["random_seed"])

# -------------------------------------------------
# Load dataset
# -------------------------------------------------

print("\nLoading dataset...")

df = pd.read_csv(INPUT_FILE)

original_rows = len(df)

print(f"Original rows: {original_rows:,}")

# -------------------------------------------------
# Duplicate records
# -------------------------------------------------

duplicates = df.sample(
    frac=DUPLICATE_RATE,
    random_state=config["random_seed"]
)

df = pd.concat([df, duplicates], ignore_index=True)

print(f"Duplicate records added: {len(duplicates):,}")

# -------------------------------------------------
# Invalid emails
# -------------------------------------------------

invalid_rows = random.sample(
    list(df.index),
    int(len(df) * INVALID_EMAIL_RATE)
)

invalid_patterns = [
    "invalid_email",
    "gmail.com",
    "@@company.com",
    "missing_at.com",
    "",
    "test@test",
    "abc@",
    "@gmail.com"
]

for idx in invalid_rows:
    df.at[idx, "Email"] = random.choice(invalid_patterns)

print(f"Invalid emails injected: {len(invalid_rows):,}")

# -------------------------------------------------
# Missing values
# -------------------------------------------------

columns = [
    "ContactName",
    "Phone",
    "AnnualRevenue",
    "Industry"
]

missing_total = int(len(df) * MISSING_VALUES_RATE)

for column in columns:

    rows = random.sample(
        list(df.index),
        missing_total
    )

    df.loc[rows, column] = None

print(f"Missing values injected into {len(columns)} columns.")

# -------------------------------------------------
# Extra spaces
# -------------------------------------------------

space_rows = random.sample(
    list(df.index),
    int(len(df) * 0.03)
)

for idx in space_rows:

    if pd.notna(df.at[idx, "CustomerName"]):

        df.at[idx, "CustomerName"] = (
            "   "
            + str(df.at[idx, "CustomerName"])
            + "   "
        )

print(f"Extra spaces injected: {len(space_rows):,}")

# -------------------------------------------------
# Mixed casing
# -------------------------------------------------

case_rows = random.sample(
    list(df.index),
    int(len(df) * 0.02)
)

for idx in case_rows:

    if pd.notna(df.at[idx, "ContactName"]):

        df.at[idx, "ContactName"] = str(
            df.at[idx, "ContactName"]
        ).upper()

print(f"Uppercase names injected: {len(case_rows):,}")

# -------------------------------------------------
# Save dataset
# -------------------------------------------------

Path("input").mkdir(exist_ok=True)

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nDirty dataset created successfully.")
print(f"Rows: {len(df):,}")
print(f"Output: {OUTPUT_FILE}")