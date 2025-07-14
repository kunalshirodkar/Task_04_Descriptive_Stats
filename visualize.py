# visualize_stats.py

import pandas as pd  
import seaborn as sns  # For beautiful statistical plots
import matplotlib.pyplot as plt  # Core plotting library
import os  

#the data is located here
DATA_DIR = "period_03"

# Dictionary holding each dataset's name and file path
files = {
    "Facebook Ads": "2024_fb_ads_president_scored_anon.csv",
    "Facebook Posts": "2024_fb_posts_president_scored_anon.csv",
    "Twitter Posts": "2024_tw_posts_president_scored_anon.csv"
}

# Making sure there's a folder to save all the plot images
os.makedirs("plots", exist_ok=True)

# Looping through each dataset and generate plots
for name, file in files.items():
    print(f"\n📊 Generating charts for: {name}")

    # Load the CSV file using pandas
    df = pd.read_csv(os.path.join(DATA_DIR, file))

    # taking only the numeric columns (int and float) for histograms and boxplots
    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    # --- HISTOGRAMS ---
    for col in numeric_cols[:5]:  # We'll limit to 5 columns 
        plt.figure(figsize=(8, 4))  
        sns.histplot(df[col], bins=30, kde=True)  
        plt.title(f"{name} - Histogram of {col}")
        plt.tight_layout()
        # Save the plot with a readable filename
        plt.savefig(f"plots/{name.replace(' ', '_')}_{col}_hist.png")
        plt.close()  # Close the figure so the next plot doesn’t overlap

