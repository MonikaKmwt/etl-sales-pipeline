#Automated ETL Pipeline for Sales & Customer Analytics

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16+-316192.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Production--Ready-success.svg)

An **end-to-end ETL (Extract, Transform, Load)** pipeline that automates the process of loading, cleaning, transforming, and analyzing **sales and customer data** using Python, Pandas, and PostgreSQL.  
It demonstrates data engineering best practices including modular scripting, database integration, SQL optimization, and data validation.  

---

##Project Overview

This project extracts data from **CSV & JSON sources**, transforms it into a clean and analytics-ready format, and loads it into a **PostgreSQL database**.  
It then creates **SQL views** for customer, product, and country-level analytics.

The pipeline is automated, modular, and includes **logging, data quality checks**, and **error handling**.

---

##Tech Stack

| Layer | Technology Used |
|--------|-----------------|
| **Language** | Python 3.10+ |
| **Libraries** | Pandas, NumPy, SQLAlchemy, psycopg2 |
| **Database** | PostgreSQL |
| **Version Control** | Git & GitHub |
| **IDE** | Visual Studio Code |
| **Logging** | Python’s logging module |
| **Validation** | Pandas-based checks |

---

##Project Structure
etl_sales_pipeline/
├── data/ # Raw CSV / JSON input files
├── logs/ # Log files for ETL runs
├── scripts/ # Modular Python scripts
│ ├── extract.py # Data extraction logic
│ ├── transform.py # Data cleaning & transformation
│ ├── validate.py # Data validation checks
│ ├── load.py # Load transformed data into PostgreSQL
│ ├── logger.py # Centralized logging utility
│ ├── config.py # Database config & constants
│ └── init.py
├── sql/
│ ├── create_tables.sql # Table creation schema
│ └── views.sql # Analytics SQL views
├── main.py # Main ETL pipeline orchestrator
├── requirements.txt # Python dependencies
└── README.md # Project documentation
##Pipeline Flow

1. **Extract**  
   - Reads data from CSV (and JSON in future extensions)
   - Handles missing and malformed records  

2. **Transform**  
   - Cleans nulls, drops duplicates, standardizes column names  
   - Converts datatypes (`InvoiceDate` → datetime, etc.)  
   - Creates derived metrics (`total_price`, `return_flag`)  

3. **Validate**  
   - Ensures no nulls in critical columns  
   - Checks for duplicate invoice IDs  
   - Validates numeric column ranges  

4. **Load**  
   - Inserts cleaned data into PostgreSQL  
   - Logs success/failure for each batch
  
5. **Analytics Views**  
   - `customer_sales_summary` → total spend per customer  
   - `country_sales_summary` → revenue by country  
   - `product_sales_summary` → top-selling products  
   - `daily_sales_trend` → sales trends over time  

##Run the ETL Pipeline
python main.py

##Verify in PostgreSQL
\c etl_sales_db
\dt
SELECT COUNT(*) FROM sales_transactions;
SELECT * FROM customer_sales_summary LIMIT 5;

##Example Analytics Views
Customer Sales Summary
customerid	total_invoices	total_spent	avg_invoice_value
17850	291	13500.00	46.40
12748	170	6450.32	37.95
Country Sales Summary
country	total_orders	total_revenue	unique_customers
United Kingdom	24000	5,320,000	3700
Germany	2100	150,000	120
