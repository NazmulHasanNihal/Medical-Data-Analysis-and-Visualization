# src/components/data_loading.py
"""
Load dataset from a specified file path.

This module provides a single function, `load_data`, which attempts to load a
dataset from a specified file path. If the file is not found, or if the file
is empty, this function will raise a `CustomException` with an appropriate
error message.

If an unexpected error occurs while loading the data, this function will
raise a `CustomException` with the error message.

"""
import pandas as pd
import sys
from src.logger import setup_logger
from src.exception import CustomException

# Setting up logger for this module
logger = setup_logger("data_loading")

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load dataset from the specified file path.

    Parameters
    ----------
    file_path : str
        The path to the file containing the dataset.

    Returns
    -------
    pd.DataFrame
        The loaded dataset.

    Raises
    ------
    CustomException
        If an error occurs while loading the data.
    """
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


