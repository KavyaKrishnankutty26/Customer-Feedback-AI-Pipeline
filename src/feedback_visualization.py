import pandas as pd
import matplotlib.pyplot as plt

# Load final customer feedback analysis
df = pd.read_csv("data/output/customer_feedback_analysis.csv")

# Display the dataset
print("Customer feedback data loaded successfully!")
print(df)

# Count reviews by sentiment
sentiment_counts = df["sentiment"].value_counts()

# Create a bar chart
plt.figure(figsize=(8, 5))

plt.bar(
    sentiment_counts.index,
    sentiment_counts.values
)

# Add chart title and labels
plt.title("Customer Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")

# Save the chart as an image
plt.savefig("data/output/sentiment_distribution.png")

# Display the chart
plt.show()

# Count reviews by feedback category
category_counts = df["category"].value_counts()

# Create a bar chart
plt.figure(figsize=(8, 5))

plt.bar(
    category_counts.index,
    category_counts.values
)

# Add chart title and labels
plt.title("Customer Feedback Category Distribution")
plt.xlabel("Feedback Category")
plt.ylabel("Number of Reviews")

# Save the chart as an image
plt.savefig("data/output/feedback_category_distribution.png")
plt.show()

# Filter negative reviews
negative_reviews = df[df["sentiment"] == "Negative"]

# Count negative reviews by category
negative_category_counts = negative_reviews["category"].value_counts()

# Create a bar chart
plt.figure(figsize=(8, 5))

plt.bar(
    negative_category_counts.index,
    negative_category_counts.values
)

# Add chart title and labels
plt.title("Negative Customer Feedback by Category")
plt.xlabel("Feedback Category")
plt.ylabel("Number of Negative Reviews")

plt.savefig("data/output/negative_feedback_by_category.png")
plt.show()

# Calculate sentiment distribution by category
category_sentiment = pd.crosstab(
    df["category"],
    df["sentiment"]
)

# Create a stacked bar chart
category_sentiment.plot(
    kind="bar",
    stacked=True,
    figsize=(8, 5)
)

# Add chart title and labels
plt.title("Sentiment Distribution by Category")
plt.xlabel("Feedback Category")
plt.ylabel("Number of Reviews")

plt.savefig("data/output/sentiment_by_category.png")
plt.show()