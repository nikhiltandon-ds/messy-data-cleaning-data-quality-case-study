# Source & Reproducibility Note

## Public reference

This case study uses the **UCI Online Retail II** dataset as the real-world reference for schema and data-quality issue types.

Source: https://archive.ics.uci.edu/dataset/502/online+retail+ii  
DOI: https://doi.org/10.24432/C5CG6D  
License: CC BY 4.0

UCI documents Online Retail II as a real two-year UK online retail transaction dataset with missing values; its transaction schema includes InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID and Country. The source also uses a `C` prefix on InvoiceNo to identify cancellations.

## Why the original file is not bundled

The original UCI file is approximately 43.5 MB. It could not be retrieved into the execution environment used to build this portfolio artifact. Therefore, this repository **does not claim that the bundled rows are the original UCI records**.

## Bundled data

`data/raw/retail_messy_intake.csv` is a deterministic 20,000-row portfolio intake extract built to reproduce the same *types* of issues an analyst must handle in the real UCI dataset, including missing customer IDs, cancellations, negative/non-positive values, duplicates, inconsistent text formatting, and mixed date representations.

The exact transformation and cleaning rules are documented in `docs/CLEANING_DECISIONS.md` and implemented in `python/clean_retail_data.py`.
