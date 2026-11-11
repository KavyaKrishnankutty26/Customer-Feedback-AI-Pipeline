import pandas as pd
df = pd.read_csv("data/input/customer_reviews.csv")
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