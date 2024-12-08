import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = "data/combined_data.csv"

combined_data = pd.read_csv(file_path)

correlation_matrix = combined_data[['GHI', 'DNI', 'DHI', 'Tamb', 'TModA', 'TModB']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
