import pandas as pd
import numpy as np

# Confirm the number of null values in the dataset, include ('-') 
def null_in_dataset(df):
    data = pd.DataFrame(df)
    # Replace '-' with NaN
    data.replace('-', np.nan, inplace=True)
    # Count null values (including NaN and '-')
    null_counts = data.isnull().sum()/ len(data) * 100
    return null_counts

# Find duplicates in data
def duplicates(df):
    return df.duplicated().sum()