# src/components/feature_engineering.py
import pandas as pd
import numpy as np
import sys
from src import setup_logger, CustomException

# Set up logger for this module
logger = setup_logger("feature_engineering")

def add_age_group(df: pd.DataFrame) -> pd.DataFrame:
    """Add age group feature.

    Args:
        df (pd.DataFrame): DataFrame with Age column.

    Returns:
        pd.DataFrame: DataFrame with Age Group column.
    """
    try:
        logger.info("Adding age group feature")
        bins = [0, 18, 35, 50, 65, np.inf]
        labels = ['Child', 'Young Adult', 'Adult', 'Senior', 'Elderly']
        df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, include_lowest=True)
        logger.info("Age group feature added successfully")
        return df
    except Exception as e:
        logger.error("Failed to add age group feature")
        raise CustomException(e, error_detail=sys)

def calculate_stay_duration(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate duration of stay in days.

    Args:
        df (pd.DataFrame): DataFrame with Date of Admission and Discharge Date columns.

    Returns:
        pd.DataFrame: DataFrame with Stay Duration column.
    """
    try:
        logger.info("Calculating stay duration")
        df['Stay Duration'] = (df['Discharge Date'] - df['Date of Admission']).dt.days.astype('int16')
        logger.info("Stay duration calculated successfully")
        return df
    except Exception as e:
        logger.error("Failed to calculate stay duration")
        raise CustomException(e, error_detail=sys)

