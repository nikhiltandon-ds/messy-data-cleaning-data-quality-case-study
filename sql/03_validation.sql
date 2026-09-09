-- Post-cleaning validation
SELECT COUNT(*) AS cleaned_rows FROM retail_clean;
SELECT COUNT(*) AS invalid_quantity FROM retail_clean WHERE Quantity <= 0;
SELECT COUNT(*) AS invalid_price FROM retail_clean WHERE UnitPrice <= 0;
SELECT COUNT(*) AS missing_customer FROM retail_clean WHERE TRIM(CustomerID)='';
SELECT COUNT(*) AS cancellations_remaining FROM retail_clean WHERE UPPER(InvoiceNo) LIKE 'C%';
SELECT ROUND(SUM(Revenue),2) AS cleaned_revenue FROM retail_clean;
