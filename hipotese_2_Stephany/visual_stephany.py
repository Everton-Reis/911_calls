import pandas as pd
from matplotlib import pyplot as plt

def plot_graf_pie_by_hour(df: pd.Series, hour: str, file_name: str):
    """
    Read the data file indicated by file_path.
    The file must be in csv format.

    Parameters
    ----------
    file_path: str
        The path to the file containing the data files.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the 'callDateTime', 'priority' and 'description' columns.

    Raises
    ------
    FileNotFoundError
        If the file does not exist
    """
    graf_df = df[df['hour'] == hour]
    graf_df_groupby = graf_df.groupby(['description']).size()
    graf_df_groupby = graf_df_groupby.sort_values(ascending=[False])
    graf_df_groupby.plot.pie(y='description')
    plt.title(f"Principais ocorencias às {hour} horas")
    plt.savefig(file_name, dpi=300)

def plot_graf_bar(df: pd.Series, x: str,y: str):
    df.plot.bar(x=x, y=y)
    plt.savefig('test_1.png', dpi=300)