from scipy.stats import zscore
import pandas as pd

file_path = "data/combined_data.csv"

combined_data = pd.read_csv(file_path)

combined_data['GHI_Z'] = zscore(combined_data['GHI'])


outliers = combined_data[combined_data['GHI_Z'].abs() > 3]

outliers.to_csv("output/ghi_outliers.csv", index=False)
print(outliers)
