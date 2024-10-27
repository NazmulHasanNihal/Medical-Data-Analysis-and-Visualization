# main_script.py
from src.components.data_loading import load_data
from src.components.data_cleaning import clean_data
from src.components.feature_engineering import add_age_group, calculate_stay_duration


# Load data
data = load_data('data/raw/healthcare_dataset.csv')

# Clean data
cleaned_data = clean_data(data)

# Add features
data_with_age_groups = add_age_group(cleaned_data)
data_with_stay_duration = calculate_stay_duration(data_with_age_groups)

