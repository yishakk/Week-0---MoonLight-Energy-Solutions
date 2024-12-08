
import pandas as pd
import matplotlib.pyplot as plt

file_path = "data/combined_data.csv"

combined_data = pd.read_csv(file_path)

combined_data['GHI'].plot(kind='hist', bins=50, alpha=0.7, title="GHI Distribution")
plt.xlabel("GHI (W/m²)")
plt.show()
