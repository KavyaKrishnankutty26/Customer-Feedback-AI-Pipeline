import os
import pandas as pd
from dotenv import load_dotenv
from google import genai
import json

# Load environment variables
load_dotenv()

# Read Gemini API key
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("Google API key not found!")

# Create Gemini client
client = genai.Client(api_key=api_key)

print("Gemini client connected successfully!")

# Load existing sentiment results
df = pd.read_csv("data/output/customer_sentiment_results.csv")

# Display review information
print("\nTotal reviews to categorize:", len(df))

print("\nCustomer reviews:")
print(df[["review_id", "customer_review", "sentiment"]])

# Collect review details
reviews = df[["review_id", "customer_review"]].to_dict(orient="records")

# Prepare the category analysis prompt
prompt = f"""
Analyze each customer review and assign exactly one category.

Use only these four categories:

1. Product: Product quality, defects, features, or pricing.
2. Delivery: Shipping delays, packaging, wrong or missing items.
3. Payment: Payments, duplicate charges, transactions, or checkout.
4. Support: Customer service, refunds, complaints, or assistance.

Rules:
- Select the category that best represents the main issue or topic.
- Assign only one category to each review.
- Do not change the review IDs.
- Do not invent or omit any reviews.

Customer reviews:
{reviews}

Return the results as a JSON array.
Each item must contain:
- review_id
- category

Return only valid JSON without markdown formatting.
"""

print("\nCategory prompt prepared successfully!")

# Send all reviews to Gemini in one request
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

# Display Gemini's response
print("\nGemini category results:")
print(response.text)

# Convert Gemini JSON response into Python data
results = json.loads(response.text)

# Convert category results into a DataFrame
category_df = pd.DataFrame(results)

# Match categories with original reviews using review_id
df = df.merge(category_df, on="review_id", how="left")

# Display final analysis
print("\nFinal customer feedback analysis:")
print(df)

# Save the final customer feedback analysis
df.to_csv("data/output/customer_feedback_analysis.csv", index=False)

print("\nCustomer feedback analysis saved successfully!")