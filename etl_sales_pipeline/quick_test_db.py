from sqlalchemy import create_engine, text

DATABASE_URI = "postgresql+psycopg2://postgres:Your_Password@localhost:5432/etl_sales_db"

def test_connection():
    try:
        engine = create_engine(DATABASE_URI)
        with engine.connect() as conn:
            version = conn.execute(text("SELECT version();"))
            print("Connection successful!")
            print("PostgreSQL version:", version.fetchone()[0])
    except Exception as e:
        print("Connection failed:", e)

if __name__ == "__main__":
    test_connection()
