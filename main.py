# main_script.py
from src.components.data_loading import load_data
from src.components.data_cleaning import clean_data
from src.components.feature_engineering import add_age_group, calculate_stay_duration

from pandas import DataFrame

def main(data_path: str) -> DataFrame:
    """
    Runs the entire data processing pipeline.

    Args:
        data_path (str): The path to the raw dataset.

    Returns:
        DataFrame: The processed data.
    """
    # Load data
    data: DataFrame = load_data(data_path)

    # Clean data
    cleaned_data: DataFrame = clean_data(data)

    # Add features
    data_with_age_groups: DataFrame = add_age_group(cleaned_data)
    data_with_stay_duration: DataFrame = calculate_stay_duration(data_with_age_groups)

    return data_with_stay_duration

if __name__ == '__main__':
    main('data/raw/healthcare_dataset.csv')


