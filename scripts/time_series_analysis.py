import pandas as pd
import matplotlib.pyplot as plt


file_path = "data/combined_data.csv"

combined_data = pd.read_csv(file_path)

combined_data['Timestamp'] = pd.to_datetime(combined_data['Timestamp'], errors='coerce')
combined_data.set_index('Timestamp', inplace=True)
numeric_data = combined_data.select_dtypes(include=['number'])

month_data = numeric_data.resample('M').mean()

plt.figure(figsize=(12, 6))
for country in combined_data['Country'].unique():
    country_data = combined_data[combined_data['Country'] == country]
    plt.plot(combined_data.index, combined_data['GHI'], label=country)

plt.title("GHI Trends Over Time")
plt.xlabel("Time")
plt.ylabel("GHI (W/m²)")
plt.legend()
plt.show()