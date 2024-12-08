import pandas as pd

file_path = "data/combined_data.csv"

combined_data = pd.read_csv(file_path)

summary_stats = combined_data.describe()

summary_stats.to_csv("output/summary_statistics.csv")

print(summary_stats)
