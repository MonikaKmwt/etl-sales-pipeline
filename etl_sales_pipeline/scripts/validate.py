
from scripts.logger import setup_logger
logger = setup_logger('validate')

def validate_data(df):
    logger.info("Running data validation checks")
    if df['invoiceno'].isnull().any():
        raise ValueError("Null InvoiceNo detected.")
    if (df['quantity'] <= 0).any():
        raise ValueError("Invalid Quantity values detected.")
    if (df['unitprice'] <= 0).any():
        raise ValueError("Invalid UnitPrice values detected.")
    logger.info("Validation passed successfully!")
