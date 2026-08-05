# Data Cleaning Project: Students Performances
import pandas as pd
import numpy as np

# Read the dirty students performance dataset
df = pd.read_csv('students_performances.csv')

# Display the initial shape, info, head, and null values of the dataset
print(df.info())
print(df.shape)
print(df.head())

# Display the unique values of specific columns to identify potential issues
for col in df:
    print(col, df[col].unique()[:15])

# Replace np.nan with 'Unknown' for better handling of missing values
df = df.replace(np.nan, 'Unknown')

# Check how many null values are present in each column and the data types of each column
print(df.isnull().sum())
print(df.dtypes)

# Save the cleaned dataset to a new CSV file for further analysis
df.to_csv('Datasets/Students Performance Dataset/cleaned_student_performance.csv', index=False)
