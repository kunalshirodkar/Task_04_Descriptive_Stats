# 📊 Task_04_Descriptive_Stats

This repository contains descriptive statistics scripts built using:

- ✅ Pure Python (no external libraries)
- ✅ Pandas
- ✅ Polars

Each approach is applied to analyze datasets related to the **2024 US Presidential Elections and Social Media Activity**, with consistent statistical outputs across tools.

---

## 🎯 Objective

The goal of this project is to explore and summarize large real-world datasets using different Python strategies. It helps compare performance, flexibility, and ease of use across base Python, Pandas, and Polars — especially for new analysts.

---

## 📁 Datasets Used

All datasets are provided externally — **do not include them in the repo**. Download the ZIP file from:

🔗 [Download period_03.zip from Google Drive](https://drive.google.com/file/d/1Jq0fPb-tq76Ee_RtM58fT0_M3o-JDBwe/view?usp=sharing)

Extracted CSV files:
- `2024_fb_ads_president_scored_anon.csv`
- `2024_fb_posts_president_scored_anon.csv`
- `2024_tw_posts_president_scored_anon.csv`

Place them inside a local folder named `period_03_data/`

---

## 🧾 Files in This Repo

| File                 | Description                                        |
|----------------------|----------------------------------------------------|
| `pure_python_stats.py` | Descriptive statistics using only standard Python |
| `pandas_stats.py`      | Same analysis using Pandas                        |
| `polars_stats.py`      | Same analysis using Polars                        |
| `README.md`            | Project summary and instructions                  |

---

## ⚙️ How to Run

Install required packages (only once):

```bash
pip install pandas polars
Then run each script one by one:

python pure_python_stats.py
python pandas_stats.py
python polars_stats.py
Make sure your CSV files are correctly placed in the folder period_03_data/.



📊 Summary of Findings
Facebook Ads
Ads were heavily targeted using specific regions and demographics.

The most frequent sponsor was "HARRIS FOR PRESIDENT".

Metrics like estimated_spend and estimated_impressions were highly skewed.

Over 200,000 unique ads and thousands of distinct delivery profiles.

Facebook Posts
Majority of posts came from pages categorized as "PERSON" or "POLITICAL_CANDIDATE".

Videos and live streams generated significantly higher engagement.

Posts showed large variance in likes, shares, and reactions.

Twitter Posts
Most tweets came from mobile platforms like Twitter for iPhone.

Engagement followed a long-tail pattern — a few tweets went viral.

English (lang = en) was dominant; controversial topics (like "scam") were flagged rarely.

💭 Reflections
Pure Python: Required the most manual work (loops, type checks), but gave full control.

Pandas: Easiest to use; its describe(), groupby(), and value_counts() made quick analysis smooth and readable.

Polars: Faster than Pandas, especially for large files. The lazy evaluation is impressive, but syntax has a learning curve.

Getting consistent results across the three approaches involved careful type handling and null value treatment.

I found AI tools like ChatGPT helpful in resolving syntax errors, especially for Polars.

If I were mentoring a junior data analyst, I’d recommend starting with Pandas, then exploring Polars for performance.

