import pandas as pd
from windrose import WindroseAxes
import matplotlib.pyplot as plt

file_path = "data/combined_data.csv"

combined_data = pd.read_csv(file_path)

ax = WindroseAxes.from_ax()
ax.bar(combined_data['WD'], combined_data['WS'], normed=True, opening=0.8, edgecolor='white')
ax.set_legend()
plt.title("Windrose Plot")
plt.show()
