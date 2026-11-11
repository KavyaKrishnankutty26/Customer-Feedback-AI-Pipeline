# Intelligent Customer Feedback Processing Pipeline

An end to end AI-powered data pipeline that processes customer reviews, performs sentiment analysis and feedback categorization using Google Gemini, and generates business insights and visualizations.

## Project Overview

Customer feedback contains valuable information about product quality, delivery performance, payment experiences, and customer support.

This project automates the process of transforming raw customer reviews into structured, actionable business insights using Python, Pandas, and Google's Gemini API.

The pipeline combines traditional data engineering practices with Generative AI to demonstrate an end-to-end AI data processing workflow.

## Project Workflow

1. **Data Inspection** – Checks dataset structure, data types, missing values, duplicate records, and empty reviews.
2. **Data Cleaning** – Removes unnecessary spaces, duplicate reviews, missing values, and empty reviews.
3. **Sentiment Analysis** – Uses Google Gemini to classify customer reviews as Positive, Negative, or Neutral.
4. **Feedback Categorization** – Classifies reviews into Product, Delivery, Payment, or Support categories.
5. **Business Insights** – Calculates sentiment distribution, category distribution, and negative feedback percentages.
6. **Data Visualization** – Generates charts to communicate customer feedback trends.

## Technologies Used

- Python
- Pandas
- Google Gemini API
- Google GenAI SDK
- Matplotlib
- python-dotenv
- CSV data processing

## Project Structure

```text
Customer-Feedback-AI-Pipeline/
│
├── data/
│   ├── input/
│   │   └── customer_reviews.csv
│   │
│   └── output/
│       ├── cleaned_customer_reviews.csv
│       ├── customer_sentiment_results.csv
│       ├── customer_feedback_analysis.csv
│       ├── customer_feedback_report.txt
│       ├── sentiment_distribution.png
│       ├── feedback_category_distribution.png
│       ├── negative_feedback_by_category.png
│       └── sentiment_by_category.png
│
├── src/
│   ├── data_inspection.py
│   ├── data_cleaning.py
│   ├── sentiment_analysis.py
│   ├── category_analysis.py
│   ├── feedback_insights.py
│   ├── feedback_visualization.py
│   └── run_pipeline.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone <https://github.com/KavyaKrishnankutty26/Customer-Feedback-AI-Pipeline.git>
```

### 2. Navigate to the project directory

```bash
cd Customer-Feedback-AI-Pipeline
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a `.env` file in the project root directory and add:

```text
GOOGLE_API_KEY=your_google_gemini_api_key
```

Replace the placeholder with your own API key.

**Security:** Never upload your `.env` file or expose your API key on GitHub.

## Run the Pipeline

Execute the complete workflow with one command:

```bash
python src/run_pipeline.py
```

The pipeline executes all six processing stages sequentially and stops if a stage encounters an error.

## Sample Business Insights

The sample dataset contains 10 customer reviews.

### Sentiment Distribution

| Sentiment | Reviews | Percentage |
| --------- | ------: | ---------: |
| Negative  |       5 |        50% |
| Positive  |       4 |        40% |
| Neutral   |       1 |        10% |

### Feedback Category Distribution

| Category | Reviews |
| -------- | ------: |
| Product  |       3 |
| Delivery |       3 |
| Payment  |       2 |
| Support  |       2 |

### Key Business Observations

- 50% of the sample reviews are negative.
- Delivery has the highest negative feedback rate at 66.67%.
- Payment and Support each have a negative feedback rate of 50%.
- Product feedback includes positive, negative, and neutral experiences.

These findings are illustrative insights from a small sample dataset, not statistically representative customer trends.

## Generated Visualizations

The pipeline generates four visual reports:

1. Customer Sentiment Distribution
2. Customer Feedback Category Distribution
3. Negative Customer Feedback by Category
4. Sentiment Distribution by Category

All charts are saved as PNG files in `data/output/`.

## Key Features

- Automated data inspection and cleaning.
- Batch AI-powered sentiment analysis.
- AI-based customer feedback categorization.
- Structured CSV output generation.
- Business insight calculations using Pandas.
- Automated chart generation using Matplotlib.
- Sequential pipeline execution.
- Basic error handling and execution status messages.
- Secure API key configuration using environment variables.

## Future Improvements

- Process larger customer review datasets.
- Add automated data validation and logging.
- Build an interactive Streamlit dashboard.
- Introduce scheduled pipeline execution.
- Add database integration for persistent storage.
- Expand feedback categories and business reporting.

## Project Purpose

This project demonstrates practical skills in data engineering, Python-based ETL workflows, Generative AI integration, structured data processing, and business analytics.

It is designed as a portfolio project showcasing how AI can enhance traditional data processing workflows.

---

**Author:** Kavya Krishnankutty
