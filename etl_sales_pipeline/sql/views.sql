
--Sales & Customer Analytics Views

-- 1 -- Customer Sales Summary
CREATE OR REPLACE VIEW customer_sales_summary AS
SELECT
    customerid,
    COUNT(DISTINCT invoiceno) AS total_invoices,
    SUM(total_price) AS total_spent,
    AVG(total_price) AS avg_invoice_value,
    MIN(invoicedate) AS first_purchase,
    MAX(invoicedate) AS last_purchase,
    COUNT(*) AS total_items_purchased
FROM sales_transactions
WHERE customerid <> -1
GROUP BY customerid;

-- 2 -- Country-Level Sales
CREATE OR REPLACE VIEW country_sales_summary AS
SELECT
    country,
    COUNT(DISTINCT invoiceno) AS total_orders,
    SUM(total_price) AS total_revenue,
    COUNT(DISTINCT customerid) AS unique_customers
FROM sales_transactions
GROUP BY country
ORDER BY total_revenue DESC;

-- 3 -- Product Performance Summary
CREATE OR REPLACE VIEW product_sales_summary AS
SELECT
    stockcode,
    description,
    SUM(quantity) AS total_units_sold,
    SUM(total_price) AS total_sales,
    AVG(unitprice) AS avg_unit_price
FROM sales_transactions
GROUP BY stockcode, description
ORDER BY total_sales DESC;

-- 4 -- Daily Sales Trend
CREATE OR REPLACE VIEW daily_sales_trend AS
SELECT
    DATE(invoicedate) AS sales_date,
    SUM(total_price) AS total_sales,
    COUNT(DISTINCT invoiceno) AS num_orders
FROM sales_transactions
GROUP BY DATE(invoicedate)
ORDER BY sales_date;
