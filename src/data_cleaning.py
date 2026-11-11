import pandas as pd

df = pd.read_csv("data/input/customer_reviews.csv")

print("Duplicates before cleaning:")
print(df.duplicated(subset=["customer_review"]).sum())

df["customer_review"] = df["customer_review"].str.strip()
df = df.drop_duplicates(subset=["customer_review"])

df = df.dropna(subset=["customer_review"])
df = df[df["customer_review"].str.strip() != ""]

print("\nCleaned dataset:")
print(df)

print("\nRemaining rows:")
print(len(df))

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDuplicate reviews after cleaning:")
print(df.duplicated(subset=["customer_review"]).sum())

df.to_csv("data/output/cleaned_customer_reviews.csv", index=False)

print("\nCleaned dataset saved successfully!")