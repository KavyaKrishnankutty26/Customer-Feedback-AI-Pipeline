import pandas as pd

# Load the final customer feedback analysis
df = pd.read_csv("data/output/customer_feedback_analysis.csv")

# Display the total number of reviews
print("Total customer reviews:", len(df))

# Display the dataset
print("\nCustomer feedback data:")
print(df)

# Count reviews in each sentiment category
sentiment_counts = df["sentiment"].value_counts()

print("\nSentiment distribution:")
print(sentiment_counts)

# Calculate sentiment percentages
sentiment_percentages = df["sentiment"].value_counts(normalize=True) * 100

print("\nSentiment percentages:")
print(sentiment_percentages.round(2))

# Count reviews in each feedback category
category_counts = df["category"].value_counts()

print("\nFeedback category distribution:")
print(category_counts)

# Filter only negative customer reviews
negative_reviews = df[df["sentiment"] == "Negative"]

# Count negative reviews in each category
negative_category_counts = negative_reviews["category"].value_counts()

print("\nNegative feedback by category:")
print(negative_category_counts)

# Calculate total reviews in each category
total_category_counts = df["category"].value_counts()

# Calculate negative feedback percentage by category
negative_percentages = (
    negative_category_counts / total_category_counts
) * 100

print("\nNegative feedback percentage by category:")
print(negative_percentages.round(2))

# Display consolidated business insights
print("\n========== CUSTOMER FEEDBACK INSIGHTS ==========")

print("\nTotal reviews:", len(df))

print("\nSentiment Summary:")
print(sentiment_counts)

print("\nCategory Summary:")
print(category_counts)

print("\nNegative Feedback by Category:")
print(negative_category_counts)

print("\nNegative Feedback Percentage:")
print(negative_percentages.round(2))

print("\n=================================================")

# Analyze sentiment distribution by category
category_sentiment = pd.crosstab(
    df["category"],
    df["sentiment"]
)

print("\nSentiment distribution by category:")
print(category_sentiment)

# Prepare business insights report
report = f"""
CUSTOMER FEEDBACK ANALYSIS REPORT
=================================

Total customer reviews: {len(df)}

1. SENTIMENT SUMMARY
--------------------
{sentiment_counts.to_string()}

2. SENTIMENT PERCENTAGES
------------------------
{sentiment_percentages.round(2).to_string()}

3. FEEDBACK CATEGORY SUMMARY
----------------------------
{category_counts.to_string()}

4. NEGATIVE FEEDBACK BY CATEGORY
--------------------------------
{negative_category_counts.to_string()}

5. NEGATIVE FEEDBACK PERCENTAGES
--------------------------------
{negative_percentages.round(2).to_string()}

6. SENTIMENT DISTRIBUTION BY CATEGORY
-------------------------------------
{category_sentiment.to_string()}
"""

print("\nBusiness report prepared successfully!")

# Save the business insights report
with open("data/output/customer_feedback_report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("\nBusiness report saved successfully!")