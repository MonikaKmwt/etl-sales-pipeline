# scripts/logger.py
import logging
import os
from scripts.config import LOG_FILE

os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def setup_logger(name):
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    return logging.getLogger(name)
