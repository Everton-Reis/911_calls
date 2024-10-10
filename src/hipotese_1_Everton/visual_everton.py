import pandas as pd
import matplotlib.pyplot as plt

def bar1_plot_df(df, line_1, column_2_1, column_2_2, title, file_name='bar_chart1.png'):
    """
    Creates a bar chart from the input DataFrame, using line_1 for the x-axis and column_2_1 and/or column_2_2 for the y-axis.
    
    Parameters
    ----------
    df (pd.DataFrame): The DataFrame containing the analyzed data.
    line_1 (str): One of the columns of the DataFrame (this will represent the x-axis).
    column_2_1 (str): One of the columns of the DataFrame.
    column_2_2 (str): One of the columns of the DataFrame.
    title (str): Title for the bar chart.
    file_name (str): Name of the file where the chart will be saved.
    """
    if line_1 not in df.columns or column_2_1 not in df.columns or column_2_2 not in df.columns:
        raise ValueError("There are no columns with the specified names in the DataFrame.")

    # Create the bar chart with purple and blue colors
    ax = df.plot.bar(x=line_1, y=[column_2_1, column_2_2], title=title, color=['purple', 'blue'])
    
    # Additional settings
    plt.xlabel(line_1)  # X-axis label
    plt.ylabel('Values')  # Y-axis label
    plt.xticks(rotation=45)  # Rotate the x-axis labels
    plt.grid(axis='y')  # Show the grid only on the y-axis
    plt.tight_layout()  # Adjust layout to avoid overlap

    # Save and close the chart to a file
    plt.savefig(file_name)
    plt.close()  

def bar2_plot_df(df, line_1, column_2, title, file_name='bar_chart2.png'):
    """
    Creates a bar chart from the input DataFrame, using line_1 for the x-axis and column_2 for the y-axis.
    
    Parameters
    ----------
    df (pd.DataFrame): The DataFrame containing the analyzed data.
    line_1 (str): One of the columns of the DataFrame (this will represent the x-axis).
    column_2 (str): One of the columns of the DataFrame.
    title (str): Title for the bar chart.
    file_name (str): Name of the file where the chart will be saved.
    """
    if line_1 not in df.columns or column_2 not in df.columns:
        raise ValueError("There are no columns with the specified names in the DataFrame.")

    # Create the bar chart
    ax = df.plot.bar(x=line_1, y=column_2, color='purple', title=title)
    
    # Additional settings
    plt.xlabel(line_1)  # X-axis label
    plt.ylabel('Values')  # Y-axis label
    plt.xticks(rotation=45)  # Rotate the x-axis labels
    plt.grid(axis='y')  # Show the grid only on the y-axis
    plt.tight_layout()  # Adjust layout to avoid overlap

    # Save and close the chart to a file
    plt.savefig(file_name)
    plt.close()  

def scatter_plot_df(df, line_1, column_2, title, file_name='scatter_chart.png'):
    """
    Creates a scatter plot from the input DataFrame, using line_1 for the x-axis and column_2 for the y-axis.
    
    Parameters
    ----------
    df (pd.DataFrame): The DataFrame containing the analyzed data.
    line_1 (str): One of the columns of the DataFrame (this will represent the x-axis).
    column_2 (str): One of the columns of the DataFrame.
    title (str): Title for the scatter plot.
    file_name (str): Name of the file where the chart will be saved.
    """
    if line_1 not in df.columns or column_2 not in df.columns:
        raise ValueError("There are no columns with the specified names in the DataFrame.")

    # Create the scatter plot
    ax = df.plot.scatter(x=line_1, y=column_2, color='purple', title=title)
    plt.grid()

    # Save and close the chart to a file
    plt.savefig(file_name)
    plt.close()  

