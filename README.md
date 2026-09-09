# Messy Data Cleaning & Data Quality Case Study

## Overview

A practical data-quality case study showing how an analyst takes a messy retail transaction intake file, profiles it, documents defects, applies transparent cleaning rules, validates the result, and produces a trusted analytical dataset.

## Source context

The real-world reference is **Online Retail II** from the UCI Machine Learning Repository (Chen, 2012; DOI 10.24432/C5CG6D). UCI documents the dataset as a two-year UK online retail transaction dataset with missing values; its schema includes InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID and Country. The source is licensed CC BY 4.0.

**Reproducibility note:** the 43.5 MB UCI source file could not be retrieved into this execution environment. Therefore, the bundled 20,000-row intake extract is a **deterministic portfolio sample constructed to reproduce the documented quality problems**, not a redistributed copy of UCI. This distinction is intentional and documented.

## Case study goal

Answer: **Can this transaction file be trusted for downstream analysis, and what changed between the raw intake and the validated analytical dataset?**

## Key quality findings

- Raw rows: **20,000**
- Clean rows: **15,480**
- Rows removed: **4,520 (22.6%)**
- Exact duplicate rows: **5**
- Missing CustomerID rows: **3,995**
- Cancellation rows: **199**
- Non-positive quantity rows: **177**
- Non-positive unit price rows: **250**
- Missing/invalid date rows: **34**

## Cleaning workflow

`Raw Intake → Quality Profile → Cleaning Rules → Clean Dataset → Validation → Business Use`

## Tools

- **Excel:** profiling summary, cleaning log, validation and executive dashboard
- **SQL:** quality checks and post-cleaning validation
- **Python:** reproducible cleaning script

## Repository structure

```text
data/raw/retail_messy_intake.csv
data/processed/retail_clean.csv
data/processed/quality_metrics.csv
data/processed/validation_summary.csv
data/retail_data_quality.db
docs/CLEANING_DECISIONS.md
docs/DATA_DICTIONARY.md
sql/01_quality_profile.sql
sql/02_cleaning_rules.sql
sql/03_validation.sql
python/clean_retail_data.py
excel/Messy_Data_Cleaning_Data_Quality_Case_Study.xlsx
images/
```

## Business recommendations

1. Keep raw and cleaned layers separate so source evidence remains auditable.
2. Exclude customer-unattributed rows from customer-level reporting, but retain them in a separate operational-quality metric.
3. Reject non-positive quantity/price records from positive-sales reporting and monitor them as exceptions.
4. Standardize dates and text dimensions before aggregation to prevent duplicate categories and unreliable time trends.
5. Add row-count, duplicate, null, cancellation and revenue tie-out checks to every refresh.

## Source

UCI Machine Learning Repository — Online Retail II: https://archive.ics.uci.edu/dataset/502/online+retail+ii
DOI: https://doi.org/10.24432/C5CG6D
