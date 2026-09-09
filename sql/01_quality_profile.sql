-- Quality profile checks on raw intake data
SELECT COUNT(*) AS raw_rows FROM retail_raw;
SELECT COUNT(*) AS missing_customer_id FROM retail_raw WHERE TRIM(CustomerID)='';
SELECT COUNT(*) AS cancellations FROM retail_raw WHERE UPPER(InvoiceNo) LIKE 'C%';
SELECT COUNT(*) AS non_positive_quantity FROM retail_raw WHERE Quantity <= 0;
SELECT COUNT(*) AS non_positive_price FROM retail_raw WHERE UnitPrice <= 0;
