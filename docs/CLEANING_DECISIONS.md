# Cleaning Decisions

This case study uses a **20,000-row deterministic portfolio intake extract** built to reproduce the real-world issue types documented for the UCI Online Retail II dataset. The UCI source itself is a real two-year UK online retail transaction dataset with missing values and cancellation/negative-value records. The full 43.5 MB UCI file could not be fetched into this runtime, so the bundled rows are explicitly **not claimed to be a copy of UCI**.

## Rules

| Issue | Decision | Why |
|---|---|---|
| Exact duplicate rows | Remove duplicates | Prevent double-counting |
| Cancellation invoice (`C*`) | Exclude | Not a completed sale |
| Missing CustomerID | Exclude from customer-level analysis | Cannot safely attribute transaction to a customer |
| Quantity <= 0 | Exclude | Invalid sale quantity for positive-sales analysis |
| UnitPrice <= 0 | Exclude | Invalid sales value |
| Missing/unsupported date | Exclude | Cannot reliably place transaction on timeline |
| Country whitespace/case | Standardize | Ensures consistent grouping |
| Description whitespace/case | Standardize | Prevents duplicate-looking categories/products |
| Supported mixed date formats | Parse to ISO datetime | Creates one canonical date field |

## Important interpretation note

Rows excluded for missing CustomerID are **not evidence of no customer**; they are simply unusable for the customer-attributed analysis.
