# data/data_loading.py
import pandas as pd
import sys
from src.logger import setup_logger
from src.exception import CustomException

# Set up logger for this module
logger = setup_logger("data_loading")

def load_data(file_path: str) -> pd.DataFrame:
    """Load dataset from the specified file path."""
    try:
        logger.info(f"Attempting to load data from {file_path}")
        data = pd.read_csv(file_path)
        logger.info("Data loaded successfully")
        return data
    except FileNotFoundError as e:
        logger.error(f"File not found: {file_path}")
        raise CustomException(e, error_detail=sys)
    except pd.errors.EmptyDataError as e:
        logger.error("Data file is empty")
        raise CustomException(e, error_detail=sys)
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise CustomException(e, error_detail=sys)
