
import sqlalchemy
from sqlalchemy import text
from scripts.logger import setup_logger
from scripts.config import DATABASE_URI

logger = setup_logger('load')

def load_to_db(df, table_name='sales_transactions'):
    try:
        logger.info(f"Connecting to DB: {DATABASE_URI}")
        engine = sqlalchemy.create_engine(DATABASE_URI)

        with engine.begin() as conn:
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS sales_transactions (
                    invoiceno VARCHAR(20),
                    stockcode VARCHAR(20),
                    description TEXT,
                    quantity INT,
                    invoicedate TIMESTAMP,
                    unitprice DECIMAL(10,2),
                    customerid INT,
                    country VARCHAR(50),
                    total_price DECIMAL(12,2),
                    return_flag BOOLEAN
                );
            """))

            df.to_sql(table_name, conn, if_exists='append', index=False)
            logger.info(f"Inserted {len(df)} rows into {table_name}")
            print(f"Inserted {len(df)} rows into {table_name}")
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        print(f" Error loading data: {e}")
