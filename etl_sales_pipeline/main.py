
from scripts.extract import extract_csv
from scripts.transform import transform_data
from scripts.validate import validate_data
from scripts.load import load_to_db
from scripts.logger import setup_logger
from scripts.config import CSV_PATH
from datetime import datetime

logger = setup_logger('main')

def main():
    start = datetime.now()
    logger.info("ETL Pipeline started")
    try:
        raw_df = extract_csv(CSV_PATH)
        transformed_df = transform_data(raw_df)
        validate_data(transformed_df)
        load_to_db(transformed_df)
        logger.info("ETL Pipeline completed successfully.")
    except Exception as e:
        logger.error(f"ETL Pipeline failed: {e}")
    finally:
        logger.info(f"Pipeline runtime: {datetime.now() - start}")

if __name__ == "__main__":
    main()
