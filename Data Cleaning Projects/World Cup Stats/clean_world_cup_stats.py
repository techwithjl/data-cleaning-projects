# Data Cleaning Project: World Cup Stats
import pandas as pd
import numpy as np

# Read the dirty World Cup stats dataset
df = pd.read_csv('Datasets/World Cup Stats Dataset/wcplayerstatistics2026.csv')

# Display the initial shape, info, head, and null values of the dataset
print(df.info())
print(df.shape)
print(df.head())

# Display the unique values of dirty columns to identify potential issues
dirty_cols = ['Club', 'SecondPos']
for col in dirty_cols:
    print(col, df[col].unique())

# Replace np.nan with 'Unknown' for better handling of missing values
df = df.replace(np.nan, 'Unknown')

# Check how many null values are present in each column and the data types of each column
print(df.isnull().sum())
print(df.dtypes)

# Save the cleaned dataset to a new CSV file for further analysis
df.to_csv('Datasets/World Cup Stats Dataset/cleaned_wcplayerstatistics2026.csv', index=False)