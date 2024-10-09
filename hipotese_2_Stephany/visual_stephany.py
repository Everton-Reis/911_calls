import pandas as pd
from matplotlib import pyplot as plt

def plot_graf_pie_by_hour(df: pd.Series, hour: str, file_name: str, column: str):
    """
    Plot a pie graphic based on the values in the `column` for a specific `hour`.

    Parameters
    ----------
    df: pd.DataFrame
        DataFrame containing the data for plotting.
    hour: str
        Hour of the day to analyze and filter the data.
    file_name: str
        Name of the file where the plot will be saved.
    column: str
        Column by which the pie graphic will be grouped and plotted.
        Must be 'description' or 'priority'

    Returns
    -------
    None
        The pie graphic is saved as an image file.

    Raises
    ------
    KeyError
        If the specified `column` or 'hour' does not exist in the DataFrame.
    """
    try:
        graf_df = df[df['hour'] == hour]
        graf_df_groupby = graf_df.groupby([column]).size()
    except KeyError:
        print(f"Error in plot_graf_pie_by_hour function: {column} or 'hour' column not found in file.")
        exit()

    graf_df_groupby = graf_df_groupby.sort_values(ascending=[False])
    
    graf_df_groupby.plot.pie(
        y=column,
        autopct='%1.1f%%',  #Show percentages
        colors=['#3A3661', '#423b6a', '#6b6295', '#9589bf','#beb0ea'],
        explode=[0.1] + [0] * (len(graf_df_groupby) - 1),  #Highlighting the first slice
    )

    if column == 'description':
        plt.title(f"Main occurrences at {hour}:00", fontsize=14, pad=20)
    elif column == 'priority':
        plt.title(f"Percentage of severity of occurrences at {hour}:00", fontsize=14, pad=20)

    plt.tight_layout()
    plt.savefig(file_name, dpi=300, format='png')
    plt.close()

def plot_graf_bar(df: pd.Series, x: str,y: str, file_name: str):
    """
    Plot a bar graphic representing the data in the specified columns.

    Parameters
    ----------
    df: pd.DataFrame
        DataFrame containing the data for plotting.
    x: str
        Column to be used for the x-axis.
    y: str
        Column to be used for the y-axis.
    file_name: str
        Name of the file where the plot will be saved.

    Returns
    -------
    None
        The bar graphic is saved as an image file.
    """
    colors = ['#3A3661', '#423b6a', '#6b6295', '#9589bf', '#beb0ea']
    ax = df.plot.bar(x=x, y=y, color=colors, width=0.8, figsize=(15, 6))
    plt.title('Number of calls per hour', fontsize=18, weight='bold')
    plt.xlabel('hour', fontsize=12)
    plt.ylabel('calls', fontsize=12)


    # Girando os rótulos do eixo X, se necessário
    plt.xticks(rotation=45, ha='right', fontsize=10)  # Rotaciona os rótulos no eixo X
    plt.yticks(fontsize=10)  # Tamanho da fonte no eixo Y

    # Adicionando rótulos de valor nas barras
    for columns in ax.containers:
        ax.bar_label(columns, label_type='edge', fontsize=10, color='black')

    plt.tight_layout()
    plt.savefig(file_name, dpi=300, format='png')
    plt.close()