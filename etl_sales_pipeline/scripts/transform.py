
import numpy as np
import pandas as pd
from scripts.logger import setup_logger
logger = setup_logger('transform')

def transform_data(df):
    logger.info("Starting data transformation")

    #Clean column names
    df.columns = df.columns.str.strip().str.lower()

    #Drop duplicates
    df.drop_duplicates(inplace=True)

    df[df['description'].notna()].copy()

    df['customerid'] = df['customerid'].fillna(-1).astype(int)

    df = df[(df['quantity'] > 0) & (df['unitprice'] > 0)].copy()

    df['invoicedate'] = pd.to_datetime(df['invoicedate'], format='%m%d%y %H:%M', errors='coerce')

    df['total_price'] = df['quantity'] * df['unitprice']

    df['return_flag'] = np.where(df['quantity'] < 0, True, False)

    logger.info(f"Transformation complete. {len(df)} rows remain.")
    return df
