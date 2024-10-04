import pandas as pd
import os
from matplotlib import pyplot as plt

def Load_datafile(file_path:str) -> pd.DataFrame:
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

    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File not found: {file_path}')
    
    columns=['callDateTime', 'priority', 'description']
    df = pd.read_csv(file_path, sep = "\t")
    return df[columns]


def get_hour(entrada,arquivo):
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
    horas=[]
    for key in arquivo[entrada]:
        horas.append((key.split(" ")[1]).split(":")[0])
    arquivo['hour']=horas
    return arquivo

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
    plt.savefig(file_name, dpi=300)