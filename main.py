from scripts.summary_statistics import generate_summary_statistics
from scripts.data_quality_check import check_data_quality
from scripts.time_series_analysis import plot_time_series
from scripts.cleaning_analysis import analyze_cleaning_impact
from scripts.correlation_analysis import generate_correlation_matrix
from scripts.wind_analysis import generate_wind_rose
from scripts.temperature_analysis import analyze_temperature_humidity
from scripts.histograms import generate_histograms
from scripts.z_score_analysis import identify_outliers
from scripts.bubble_charts import plot_bubble_chart

def main():


    generate_summary_statistics()

 
    check_data_quality()

 
    plot_time_series()

 
    analyze_cleaning_impact()


    generate_correlation_matrix()

    generate_wind_rose()


    analyze_temperature_humidity()


    generate_histograms()


    identify_outliers()


    plot_bubble_chart()

if __name__ == "__main__":
    main()
