import pandas as pd

file_path = "data/combined_data.csv"

combined_data = pd.read_csv(file_path)

cleaned = combined_data[combined_data['Cleaning'] == 1]
not_cleaned = combined_data[combined_data['Cleaning'] == 0]


cleaned_avg = cleaned[['ModA', 'ModB']].mean()
not_cleaned_avg = not_cleaned[['ModA', 'ModB']].mean()

print("Average sensor values after cleaning:\n", cleaned_avg)
print("Average sensor values without cleaning:\n", not_cleaned_avg)
