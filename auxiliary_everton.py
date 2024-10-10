import pandas as pd

def get_columns(file: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """
    Returns a sub_file containing only the desired columns.

    Parameters
    ----------
    file : pandas.DataFrame
        DataFrame from which the sub_file with the desired columns will be extracted.
    
    columns : list
        List of desired columns in the subfile.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing only the specified columns.
    """
    try:
        file = file[columns]  # Works directly on the reference to the original DataFrame
        return file
    except KeyError as e:
        missing_columns = list(set(columns) - set(file.columns))
        print(f"KeyError: {e}. The columns {missing_columns} are not present in the DataFrame.")
        return file  # Returns the original DataFrame in case of an error

def cleaning_by_term(file: pd.DataFrame, column: str, term: any) -> pd.DataFrame:
    """
    Removes rows from a DataFrame where a specific column contains a specific value, modifying the original DataFrame.

    Parameters
    ----------
    file : pandas.DataFrame
        DataFrame to be cleaned.
    
    column : str
        Column on which the cleaning will be applied.
    
    term : any
        Term that will be removed from the column.

    Returns
    -------
    pandas.DataFrame
        The original DataFrame with rows removed where the term was present in the column.
    """
    try:
        # Check if the column exists in the DataFrame
        if column not in file.columns:
            raise ValueError(f"The column '{column}' does not exist in the DataFrame.")
        
        # Remove the rows where the column value is equal to the term
        file.drop(file[file[column] == term].index, inplace=True)
        
    except Exception as e:
        print(f"An error occurred during DataFrame cleaning: {e}")
    
    return file

def clean_DataFrame(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the rows of the DataFrame that have at least one missing value in any of their rows.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the columns to be cleaned.
    
    Returns
    -------
    pandas.DataFrame
        DataFrame with the columns/rows cleaned.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The provided argument is not a pd.DataFrame.")  # Checks if df is a DataFrame and not a Series
    
    try:
        df_clean = df.dropna()
    except Exception as e:
        raise ValueError(f"Could not clean the rows: {e}")  # Includes error details in the exception message
        
    return df_clean
