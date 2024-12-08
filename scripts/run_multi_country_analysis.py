from src.multi_country_analysis import *

file_paths = [
    "data/benin-malanville.csv",
    "data/sierraleone-bumbuna.csv",
    "data/togo-dapaong_qc.csv"
]
country_names = ["Benin", "Sierraleone", "Togo"]


combined_data = load_csv_files(file_paths, country_names)
print("Combined Data Shape:", combined_data.shape)

cleaned_data = clean_combined_data(combined_data)
print("Cleaned Data Shape:", cleaned_data.shape)

analyze_country_trends(cleaned_data, variable="GHI")

save_combined_data(cleaned_data, "data/combined_data.csv")
