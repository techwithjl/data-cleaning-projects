# Data Cleaning Project: Cafe Sales
import pandas as pd
import numpy as np

# Read the dirty cafe sales dataset
df = pd.read_csv('dirty_cafe_sales.csv')

# Display the initial shape, info, head, and null values of the dataset
print(df.shape)
print(df.info())
print(df.head())
print(df.isnull().sum())

# Display the unique values of specific columns to identify potential issues
print(df['Quantity'].unique())
print(df['Price Per Unit'].unique())
print(df['Total Spent'].unique())

# Display the unique values of all columns to identify potential issues
for col in df.columns:
    print(col, df[col].unique()[:15])

# Replace 'ERROR' and 'UNKNOWN' with NaN for better handling of missing values
df = df.replace(['ERROR', 'UNKNOWN'], np.nan)

# Convert the relevant columns to numeric types and handle errors by coercing them to NaN
numeric_cols = ['Quantity', 'Price Per Unit', 'Total Spent']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Convert the 'Transaction Date' column to datetime format and handle errors by coercing them to NaN
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')

# Fill missing values in 'Total Spent', 'Price Per Unit', and 'Quantity' based on the available data
mask = df['Total Spent'].isnull() & df['Quantity'].notnull() & df['Price Per Unit'].notnull()
df.loc[mask, 'Total Spent'] = df.loc[mask, 'Quantity'] * df.loc[mask, 'Price Per Unit']

mask2 = df['Price Per Unit'].isnull() & df['Quantity'].notnull() & df['Total Spent'].notnull()
df.loc[mask2, 'Price Per Unit'] = df.loc[mask2, 'Total Spent'] / df.loc[mask2, 'Quantity']

mask3 = df['Quantity'].isnull() & df['Total Spent'].notnull() & df['Price Per Unit'].notnull() & (df['Price Per Unit'] != 0)
df.loc[mask3, 'Quantity'] = df.loc[mask3, 'Total Spent'] / df.loc[mask3, 'Price Per Unit']

# Fill missing values in categorical columns with 'Unknown' to maintain consistency
df['Item'] = df['Item'].fillna('Unknown')
df['Payment Method'] = df['Payment Method'].fillna('Unknown')
df['Location'] = df['Location'].fillna('Unknown')

# Drop rows with missing values in critical columns to ensure data integrity
df = df.dropna(subset=['Transaction Date', 'Quantity', 'Price Per Unit', 'Total Spent'])

# Display the final shape, null values, and data types of the cleaned dataset
print(df.isnull().sum())
print(df.shape)
print(df.dtypes)

# Save the cleaned dataset to a new CSV file for further analysis
df.to_csv('cleaned_cafe_sales.csv', index=False)
