# pure_pandas_stats.py
# This script analyzes 3 different social media datasets (Twitter, Facebook posts, and Facebook ads)
# from the 2024 U.S. presidential election using pandas. It provides summary statistics and grouped insights.

import pandas as pd

# ---------------------------------------------------
# ---------------------------------------------------
files = {
    "FACEBOOK ADS": "period_03/2024_fb_ads_president_scored_anon.csv",
    "FACEBOOK POSTS": "period_03/2024_fb_posts_president_scored_anon.csv",
    "TWITTER POSTS": "period_03/2024_tw_posts_president_scored_anon.csv"
}

# ---------------------------------------------------
# This function takes a dataset and prints key stats:
#  Overall summary (like mean, count, std)
#  Unique + most common values for text columns
#  Grouped stats by page_id and ad_id (if available)
# ---------------------------------------------------
def analyze_with_pandas(name, file_path):
    print(f"\n\n=== {name} ===")

    # Load the CSV file into a pandas df
    df = pd.read_csv(file_path)

    # Show general summary statistics — this includes count, mean, std, min, max, etc.
    # Includes both numeric and categorical columns
    print("\n--- GENERAL STATISTICS ---")
    print(df.describe(include='all'))

    # For every column that contains text (object type),
    # we'll print the number of unique values and the most frequently occurring one
    print("\n--- UNIQUE VALUES & MOST FREQUENT (CATEGORICAL) ---")
    for col in df.select_dtypes(include='object').columns:
        unique_vals = df[col].nunique()
        most_freq = df[col].value_counts().idxmax()
        print(f"{col}: unique = {unique_vals}, most frequent = {most_freq}")

    # Now we focus only on numeric columns (int or float) for grouped statistics
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    # Group by page_id if it exists — this shows stats for each page separately
    if 'page_id' in df.columns:
        print("\n--- GROUPED BY page_id ---")
        grouped = df.groupby('page_id')[numeric_cols].agg(['count', 'mean', 'min', 'max', 'std'])
        print(grouped.head())  # show only the first few groups

    # Group by page_id and ad_id — this is useful for the ads dataset where both columns exist
    if 'page_id' in df.columns and 'ad_id' in df.columns:
        print("\n--- GROUPED BY page_id + ad_id ---")
        grouped = df.groupby(['page_id', 'ad_id'])[numeric_cols].agg(['count', 'mean', 'min', 'max', 'std'])
        print(grouped.head())

# ---------------------------------------------------
# Loop through each dataset and analyze it using the function above
# ---------------------------------------------------
for name, path in files.items():
    analyze_with_pandas(name, path)
