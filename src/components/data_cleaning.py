# src/components/data_cleaning.py
import pandas as pd
import sys
from src.logger import setup_logger
from src.exception import CustomException

# Setting up logger for this module
logger = setup_logger("data_cleaning")

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform data cleaning on the dataset.

    Args:
        df: Pandas DataFrame containing the raw data

    Returns:
        Pandas DataFrame containing the cleaned data
    """
    try:
        logger.info("Starting data cleaning process")

        # Dropping rows with missing essential data
        df = df.dropna(subset=['Age', 'Gender', 'Medical Condition'])

        # Standardizing text (e.g., gender values)
        df['Gender'] = df['Gender'].str.strip().str.capitalize()

        # Converting date columns to datetime
        df['Date of Admission'] = pd.to_datetime(df['Date of Admission'], errors='coerce')
        df['Discharge Date'] = pd.to_datetime(df['Discharge Date'], errors='coerce')

        logger.info("Data cleaning completed successfully")
        return df
    except Exception as e:
        logger.error("Data cleaning failed")
        raise CustomException(e, error_detail=sys)
