# Enterprise Customer Data Quality Pipeline

## Overview

Enterprise Customer Data Quality Pipeline is a Python-based automation project that simulates a real-world enterprise data engineering workflow.

The pipeline generates a large synthetic customer dataset, injects realistic data quality issues, cleans and validates the data, and automatically generates an executive Excel report.

This project demonstrates practical data engineering concepts such as ETL processing, data validation, automation, and reporting.

---

## Features

* Generate **100,000 synthetic customer records**
* Inject realistic data quality issues
* Remove duplicate records
* Validate email addresses
* Standardize customer names
* Handle missing values
* Export a cleaned dataset
* Generate an executive Excel report
* Execute the complete pipeline with a single command

---

## Project Structure

```text
enterprise-customer-data-pipeline/

├── config/
│   └── config.json
│
├── input/
│   ├── customers_raw.csv
│   └── customers_dirty.csv
│
├── output/
│   ├── customers_clean.csv
│   └── data_quality_report.xlsx
│
├── src/
│   ├── generate_dataset.py
│   ├── inject_data_quality_issues.py
│   ├── enterprise_data_quality_pipeline.py
│   ├── quality_report.py
│   └── run_pipeline.py
│
├── requirements.txt
└── README.md
```

---

## Technologies

* Python
* Pandas
* OpenPyXL
* JSON
* Data Quality
* ETL
* Automation
* AWS S3
* Boto3
* AWS CLI
* IAM

---

## Pipeline Workflow

Generate Dataset
      │
      ▼
Inject Data Quality Issues
      │
      ▼
Clean & Validate Dataset
      │
      ▼
Generate Executive Excel Report
      │
      ▼
Upload Data to AWS S3
      │
      ▼
raw/ | dirty/ | clean/ | reports/

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the complete pipeline:

```bash
python src/run_pipeline.py
```

---

## Output

The pipeline automatically generates:

* `input/customers_raw.csv`
* `input/customers_dirty.csv`
* `output/customers_clean.csv`
* `output/data_quality_report.xlsx`

---

## Author

**Sergio Vindel**

Data Analytics | Data Engineering | Python Automation | Business Intelligence



