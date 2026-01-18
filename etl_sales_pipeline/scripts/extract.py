
import pandas as pd
from scripts.logger import setup_logger
logger = setup_logger('extract')

def extract_csv(path):
    logger.info(f"Extracting CSV from {path}")
    df = pd.read_csv(path, encoding="latin1")
    logger.info(f"Extracted {len(df)} rows and {len(df.columns)} columns.")
    return df
