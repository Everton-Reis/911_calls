import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from calls_by_category import call_counter, load_data, distribution_in_percentage

# File path for the CSV data
filepath = "C:/Users/eliane/OneDrive/Documentos/A1LP/Projeto/Projeto/911_Calls_for_Service.csv"

# Create line chart for district vs call_count with different lines for each category
def line_chart_district_calls(df):
    # Get the data categorized
    category_distribution = call_counter(df)
    
    # Create the line plot
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))

    sns.lineplot(data=category_distribution, x='district', y='call_count', hue='category', marker="o")

    plt.title("Call Count per District and Category")
    plt.xlabel("District")
    plt.ylabel("Call Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Create bar chart for the distribution percentage
def bar_chart_distribution_percentage(df):

    df_category_percentage = distribution_in_percentage(call_counter(df))

    # Plotting
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))

    sns.barplot(data=df_category_percentage, x='district', y='percentage', hue='category')

    plt.title("Percentage Distribution of Calls by Category")
    plt.xlabel("District")
    plt.ylabel("Percentage of Calls")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main function to load data and generate charts
def main():
    df = load_data(filepath) 
    line_chart_district_calls(df)  
    bar_chart_distribution_percentage(df)  

if __name__ == "__main__":
    main()