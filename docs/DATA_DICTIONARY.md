# Data Dictionary

| Field | Type | Meaning |
|---|---|---|
| InvoiceNo | Text | Transaction identifier; C prefix indicates cancellation in the source convention |
| StockCode | Text | Product/item identifier |
| Description | Text | Product description |
| Quantity | Integer | Units recorded |
| InvoiceDate | DateTime | Transaction timestamp |
| UnitPrice | Decimal | Unit price in GBP |
| CustomerID | Text | Customer identifier |
| Country | Text | Customer country |
| Revenue | Decimal | Quantity × UnitPrice; added in cleaned data |
