import pandas as pd
import pandas as pd
from pathlib import Path

# Define input file path
input_file = Path("data/input/customer_reviews.csv")

# Check whether the file exists
if not input_file.exists():
    raise FileNotFoundError("Customer reviews CSV file not found!")

try:
    df = pd.read_csv(input_file)
except pd.errors.EmptyDataError:
    raise ValueError("Customer reviews CSV file is empty!")
#df = pd.read_csv("data/input/test_invalid_reviews.csv")

# Validate input file
required_columns = ["review_id", "customer_review"]

if not all(column in df.columns for column in required_columns):
    raise ValueError("Dataset is missing required columns!")

if df.empty:
    raise ValueError("Dataset is empty!")

if df["customer_review"].isnull().any():
    raise ValueError("Dataset contains missing customer reviews!")

if df["customer_review"].str.strip().eq("").any():
    raise ValueError("Dataset contains empty customer reviews!")

print("\nData validation successful!")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate records:")
print(df.duplicated().sum())

print("\nEmpty reviews:")
print(df["customer_review"].str.strip().eq("").sum())