import pandas as pd
import os
from matplotlib import pyplot as plt

def Load_datafile(file_path:str) -> pd.DataFrame:
    """
    Read the csv data file indicated by `file_path`.

    Parameters
    ----------
    file_path: str
        The path to the csv file containing the data files.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the 'callDateTime', 'priority' and 'description' columns.

    Raises
    ------
    FileNotFoundError
        If the file does not exist.

    ValueError
        If the file does not contain the expected columns.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File not found: {file_path}')
    
    columns=['callDateTime', 'priority', 'description', "hour"]
    df = pd.read_csv(file_path, sep = "\t")

    for col in columns:
        if not col in df.columns:
            raise ValueError(f"Colunas esperadas {columns} não encontradas no arquivo.")
    
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

def groupby_by_hour(df: pd.Series,column: str):
    sub_groupby = df.groupby([column]).size()
    return sub_groupby

def most_frequenci(df: pd.Series, gy, head: int):
    sub_groupby= gy.sort_values(ascending=False)
    primeiros_50=sub_groupby.head(head)
    sub_df=df[df['description'].isin(primeiros_50.index)]
    return sub_df