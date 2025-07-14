import polars as pl

# to loop through each dataset without repeating code
datasets = {
    "FACEBOOK ADS": "period_03/2024_fb_ads_president_scored_anon.csv",
    "FACEBOOK POSTS": "period_03/2024_fb_posts_president_scored_anon.csv",
    "TWITTER POSTS": "period_03/2024_tw_posts_president_scored_anon.csv"
}

# This function loads and analyzes each dataset using Polars
def analyze_with_polars(name, filepath):
    print(f"\n=== {name} ===")

    # Load the CSV file into a Polars df
    df = pl.read_csv(filepath)

    # Print basic descriptive statistics for all columns (like count, mean, min, max)
    print("\n--- GENERAL STATISTICS ---")
    print(df.describe())

    # Go through each column to check if it is a text/categorical column (string type)
    # For these, prints the number of unique values and the most frequent one
    print("\n--- UNIQUE VALUES & MOST FREQUENT (CATEGORICAL) ---")
    for col in df.columns:
        if df[col].dtype == pl.Utf8:  # Checks if column type is string (categorical)
            uniques = df[col].n_unique()  # Counts how many unique values exist
            vc_df = df.select(pl.col(col).value_counts())  # Gets value counts
            vc_dicts = vc_df.to_dicts()  # Convert to list of dictionaries for easy access

            # If there are any rows in the result, get the most frequent value
            if vc_dicts:
                most_common = vc_dicts[0][col]  # The key will here is the column name
            else:
                most_common = "N/A"

            print(f"{col}: unique={uniques}, most_frequent={most_common}")

    # List of columns that are numeric (float or integer)
    numeric_cols = [col for col in df.columns if df[col].dtype in [pl.Float64, pl.Int64]]

    # If the dataset contains a 'page_id' column, grouping by and calculate counts + averages
    if "page_id" in df.columns:
        print("\n--- GROUPED BY page_id ---")
        group1 = df.group_by("page_id").agg(
            [pl.count()] + [pl.mean(col).alias(f"{col}_mean") for col in numeric_cols]
        )
        print(group1.head()) 

    # If both 'page_id' and 'ad_id' exist, doing a more detailed grouping
    if "page_id" in df.columns and "ad_id" in df.columns:
        print("\n--- GROUPED BY page_id AND ad_id ---")
        group2 = df.group_by(["page_id", "ad_id"]).agg(
            [pl.count()] + [pl.mean(col).alias(f"{col}_mean") for col in numeric_cols]
        )
        print(group2.head())


# ---------------------------------------------------
# Loop through each dataset and analyze it using the function above
# ---------------------------------------------------
for name, path in datasets.items():
    analyze_with_polars(name, path)
