import pandas as pd
import matplotlib.pyplot as plt

file_path = "data/combined_data.csv"

combined_data = pd.read_csv(file_path)

plt.scatter(combined_data['GHI'], combined_data['Tamb'], 
            s=combined_data['RH']*10, alpha=0.5, c=combined_data['WS'], cmap='viridis')
plt.title("GHI vs Tamb vs WS (Bubble size = RH)")
plt.xlabel("GHI (W/m²)")
plt.ylabel("Ambient Temperature (°C)")
plt.colorbar(label="Wind Speed (m/s)")
plt.show()
