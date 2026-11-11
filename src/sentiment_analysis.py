import os
from dotenv import load_dotenv
from google import genai
import pandas as pd
import json

# Load environment variables from .env
load_dotenv()

# Read Gemini API key
api_key = os.getenv("GOOGLE_API_KEY")

# Check whether API key exists
if not api_key:
    raise ValueError("Google API key not found!")

# Create Gemini client
client = genai.Client(api_key=api_key)

print("Gemini client connected successfully!")


# Load cleaned customer reviews
df = pd.read_csv("data/output/cleaned_customer_reviews.csv")

# Display the number of reviews
print("\nTotal reviews to analyze:", len(df))

# Display customer reviews
print("\nCustomer reviews:")
print(df[["review_id", "customer_review"]])

# Collect all customer reviews
reviews = df["customer_review"].tolist()

# Prepare the batch prompt
prompt = f"""
Analyze the sentiment of each customer review below.

Classify each review into exactly one of these categories:
Positive, Negative, or Neutral.

Rules:
- Positive: The customer expresses satisfaction.
- Negative: The customer expresses dissatisfaction.
- Neutral: The review contains mixed or neither clearly positive nor negative sentiment.

Customer reviews:
{reviews}

Return the results as a JSON array.
Each item must contain:
- review_number
- sentiment

Return only valid JSON without markdown formatting.
"""

# Send all reviews to Gemini in one request
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

# Display Gemini's response
print("\nGemini batch sentiment results:")


# Convert Gemini JSON response into Python data
results = json.loads(response.text)

# Convert results into a pandas DataFrame
sentiment_df = pd.DataFrame(results)

# Match results with the original reviews
sentiment_df = sentiment_df.sort_values("review_number")

df["sentiment"] = sentiment_df["sentiment"].tolist()

# Display final results
print("\nFinal customer sentiment results:")
print(df)

# Save sentiment results to CSV
df.to_csv("data/output/customer_sentiment_results.csv", index=False)

print("\nSentiment results saved successfully!")