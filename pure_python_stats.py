import csv
from collections import defaultdict, Counter

# to loop through each dataset without repeating code
datasets = {
    "FACEBOOK ADS": "period_03/2024_fb_ads_president_scored_anon.csv",
    "FACEBOOK POSTS": "period_03/2024_fb_posts_president_scored_anon.csv",
    "TWITTER POSTS": "period_03/2024_tw_posts_president_scored_anon.csv"
}

# Function to check if a value is numeric (can be converted to float)
def is_float(value):
    try:
        float(value)
        return True
    except:
        return False

# Main function to analyze a CSV file using pure Python
def analyze_with_pure_python(name, filepath):
    print(f"\n=== {name} ===")

    # Open the CSV file and read it into a list of dictionaries (each row = dict)
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    # If the file is empty exits early
    if not rows:
        print("Empty file.")
        return

    #Use separate dictionaries to store numeric and text column values
    numeric_data = defaultdict(list)
    text_data = defaultdict(list)

    # Loop through each row and categorize each column value as numeric or text
    for row in rows:
        for col, val in row.items():
            if val == "":
                continue  #skips empty cells
            if is_float(val):
                numeric_data[col].append(float(val))
            else:
                text_data[col].append(val)

    # === STATS FOR NUMERIC COLUMNS ===
    print("\n--- NUMERIC COLUMNS ---")
    for col, values in numeric_data.items():
        count = len(values)
        _min = min(values)
        _max = max(values)
        _mean = sum(values) / count if count else 0
        print(f"{col}: count={count}, min={_min}, max={_max}, mean={_mean:.2f}")

    # === STATS FOR TEXT COLUMNS ===
    print("\n--- TEXT COLUMNS ---")
    for col, values in text_data.items():
        count = len(values)
        unique_vals = set(values)
        most_common = Counter(values).most_common(1)[0]  # Get most frequent value
        print(f"{col}: count={count}, unique={len(unique_vals)}, most_frequent={most_common[0]} ({most_common[1]} times)")

# ---------------------------------------------------
# Loop through each dataset and analyze it using the function above
# ---------------------------------------------------
for name, path in datasets.items():
    analyze_with_pure_python(name, path)
