import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import geopandas as gpd
from calls_by_category import call_counter, load_data, distribution_in_percentage

filepath = "911_Calls_for_Service.csv"
filepath2 = "Cleaned_Call_Distribution.csv"

def line_chart_district_calls(df):
    """
    Create a line chart showing the call count per district, categorized by call type.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing the call data with district and call categories.
    """
    # Get the categorized data using the call_counter function
    category_distribution = call_counter(df)
    
    # Create the line plot
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=category_distribution, x='district', y='call_count', hue='category', marker="o")

    # Customize the plot
    plt.title("Call Count per District and Category")
    plt.xlabel("District")
    plt.ylabel("Call Count")
    plt.xticks(rotation=45)
    plt.legend(loc='upper right') 
    plt.tight_layout()
    
    # Save the plot as an image
    plt.savefig("District_Distribution_Calls.png")
    plt.show()

def bar_chart_distribution_percentage(df):
    """
    Create a bar chart showing the percentage distribution of calls by district and category.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing the call data with district and call categories.
    """
    # Get percentage distribution of calls by category
    df_category_percentage = distribution_in_percentage(call_counter(df))

    # Create the bar plot
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_category_percentage, x='district', y='percentage', hue='category')

    # Customize the plot
    plt.title("Percentage Distribution of Calls by Category")
    plt.xlabel("District")
    plt.ylabel("Percentage of Calls")
    plt.xticks(rotation=45)
    plt.legend(loc='upper right')
    plt.tight_layout()

    # Save the plot as an image
    plt.savefig("Distribution_Percentage.png")
    plt.show()

def map_generator(filepath2):
    """
    Generate a geographical map showing the distribution of calls across Baltimore districts.

    Parameters
    ----------
    filepath2 : str
        The path to the CSV file containing the cleaned call distribution data.
    """

    df = pd.read_csv(filepath2)

    # Load the map data (Baltimore police districts shapefile)
    map_data = gpd.read_file('C:/Users/eliane/OneDrive/Documentos/A1LP/Projeto/Projeto/Police_Districts_2023.zip')

    # Sum call counts by district and sort the map data 
    call_sums = df.groupby('district')['call_count'].sum()
    df_map = gpd.GeoDataFrame(map_data).sort_values(by="Dist_Abbr")

    # Add the call count data to the map
    df_map['Call Counts'] = call_sums.values

    # Plot the map with a color gradient showing the call counts per district
    df_map.plot(column='Call Counts', legend=True, cmap='Blues')
    plt.title("Distribution of Calls Across Baltimore Districts")

    # Save the map as an image
    plt.savefig("Baltimore.png")
    plt.show()

def main():
    """
    Main function to load the data and generate charts and a map.
    """

    df = load_data(filepath)

    # Generate the line chart for district calls
    print("Generating line chart for call count by district...")
    line_chart_district_calls(df)

    # Generate the bar chart for percentage distribution
    print("Generating bar chart for percentage distribution...")
    bar_chart_distribution_percentage(df)

    # Generate the map showing call distribution across districts
    print("Generating map of call distribution...")
    map_generator(filepath2)

if __name__ == "__main__":
    main()