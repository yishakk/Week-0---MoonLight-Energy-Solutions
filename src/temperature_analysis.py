import pandas as pd
import matplotlib.pyplot as plt

file_path = "data/combined_data.csv"

combined_data = pd.read_csv(file_path)

plt.scatter(combined_data['RH'], combined_data['Tamb'], alpha=0.5)
plt.title("Relative Humidity vs Ambient Temperature")
plt.xlabel("Relative Humidity (%)")
plt.ylabel("Ambient Temperature (°C)")
plt.show()
