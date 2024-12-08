import pandas as pd

file_path = "data/combined_data.csv"

combined_data = pd.read_csv(file_path)

missing_values = combined_data.isnull().sum()

negative_values = combined_data[(combined_data['GHI'] < 0) | 
                                 (combined_data['DNI'] < 0) | 
                                 (combined_data['DHI'] < 0)]

missing_values.to_csv("output/missing_values.csv")
negative_values.to_csv("output/negative_values.csv")

print("Missing values:", missing_values)
print("Negative values:", negative_values)
