import json
import random
from pathlib import Path

import pandas as pd
from faker import Faker

# -------------------------------------------------
# Load configuration
# -------------------------------------------------

CONFIG_PATH = Path("config/config.json")

with open(CONFIG_PATH, "r") as file:
    config = json.load(file)

RECORDS = config["records"]
OUTPUT_FILE = config["raw_output_file"]
SEED = config["random_seed"]

fake = Faker()
Faker.seed(SEED)
random.seed(SEED)

# -------------------------------------------------
# Reference data
# -------------------------------------------------

countries = [
    "United States",
    "Canada",
    "Mexico",
    "Brazil",
    "United Kingdom",
    "Germany",
    "Spain",
    "France",
    "Argentina",
    "Colombia",
    "Chile",
    "Peru",
    "El Salvador",
    "Guatemala"
]

industries = [
    "Banking",
    "Retail",
    "Healthcare",
    "Insurance",
    "Technology",
    "Education",
    "Telecommunications",
    "Manufacturing",
    "Energy",
    "Logistics"
]

customer_segments = [
    "Enterprise",
    "SMB",
    "Startup"
]

# -------------------------------------------------
# Generate dataset
# -------------------------------------------------

rows = []

print(f"\nGenerating {RECORDS:,} customer records...\n")

for customer_id in range(1, RECORDS + 1):

    annual_revenue = random.randint(5000, 5000000)

    employee_count = random.randint(5, 10000)

    rows.append({
        "CustomerID": customer_id,
        "CustomerName": fake.company(),
        "ContactName": fake.name(),
        "Email": fake.company_email(),
        "Phone": fake.phone_number(),
        "Country": random.choice(countries),
        "Industry": random.choice(industries),
        "CustomerSegment": random.choice(customer_segments),
        "AnnualRevenue": annual_revenue,
        "Employees": employee_count,
        "CreatedDate": fake.date_between(
            start_date="-5y",
            end_date="today"
        ),
        "IsActive": random.choice([True, True, True, False])
    })

df = pd.DataFrame(rows)

# -------------------------------------------------
# Save dataset
# -------------------------------------------------

Path("input").mkdir(exist_ok=True)

df.to_csv(OUTPUT_FILE, index=False)

print("Dataset generated successfully.")
print(f"Rows: {len(df):,}")
print(f"Output: {OUTPUT_FILE}")