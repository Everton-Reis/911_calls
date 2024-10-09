import pandas as pd
import os

def load_datafile(file_path: str) -> pd.DataFrame:
    """
    Read the csv data file indicated by `file_path`.
    The file must use a tab separator.

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
        raise FileNotFoundError(f'Error in load_datafile function: File not found: {file_path}')
    
    columns=['callDateTime', 'priority', 'description']
    df = pd.read_csv(file_path, sep = "\t")

    for col in columns:
        if not col in df.columns:
            raise ValueError(f"Erro in load_datafile function: Expected columns {columns} not found in file.")
    
    return df[columns]


def get_hour(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a new Dataframe column called `hour`, which contains the hour information extracted from the `callDateTime` column. 
    The entries in 'callDataTime' must be in the format: 'date hour:minutes:seconds'.

    Parameters
    ----------
    df: pd.DataFrame
        The DataFrame containing the column 'callDataTime'.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the new column 'hour'.

    Raises
    ------
    KeyError
        If the 'callDateTime' column does not exist or is in an unexpected format.
    """

    hour=[]
    try:
        for key in df["callDateTime"]:
            hour.append((key.split(" ")[1]).split(":")[0])
    except KeyError:
        print("Error in get_hour function: 'callDataTime' column not found in file.")
        exit()
    df['hour']=hour
    return df

def get_first_15_most_frequency(df: pd.DataFrame, df_groupy) -> pd.DataFrame:
    """
    Get the rows that contain the first 15 most common description occurrences.

    Parameters
    ----------
    df: pd.DataFrame
        The DataFrame containing the column 'description'.

    df_groupby: pd.core.series.Series
        A core.series.Series with the sizes of the groups by the parameter 'description'.
    
    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the rows with the 15 most common description occurrences.

    Raises
    ------
    KeyError
        If the 'description' column does not exist in the DataFrame.
    """
    
    sub_groupby= df_groupy.sort_values(ascending=False)
    first_15=sub_groupby.head(15)
    try:
        sub_df=df[df['description'].isin(first_15.index)]
    except KeyError:
        print(f"Error in get_first_15_most_frequency function: 'description' column not found in file.")
        exit()
    return sub_df