import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_csv_files(file_paths, country_names):
    dataframes = []
    for file_path, country in zip(file_paths, country_names):
        df = pd.read_csv(file_path)
        df["Country"] = country  
        dataframes.append(df)
    return pd.concat(dataframes, ignore_index=True)

def clean_combined_data(data):

    data = data.dropna(subset=["GHI"])
    
    for col in ["GHI", "DNI", "DHI"]:
        if col in data.columns:
            data = data[data[col] >= 0]
    
    return data

def analyze_country_trends(data, country_column="Country", variable="GHI"):

    plt.figure(figsize=(12, 6))
    sns.boxplot(data=data, x=country_column, y=variable)
    plt.title(f"{variable} Distribution by Country")
    plt.ylabel(variable)
    plt.xlabel("Country")
    plt.show()

def save_combined_data(data, output_path):

    data.to_csv(output_path, index=False)
