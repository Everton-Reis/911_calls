import pandas as pd
import auxiliar_geral as lp

columns = ['recordId', 'callDateTime', 'priority', 'district', 'description', 'PoliceDistrict', 'ESRI_OID']

def clean(name: str, columns: list) -> pd.DataFrame:
    """
    Cleans the data from a CSV file, keeping only useful columns and cleaning irregular data.

    Parameters
    ----------
    name : str
        The name of the CSV file to be read. The file must be in tab-delimited format (different from the common comma format).

    columns : list
        List of columns that will remain in the DataFrame.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing only the specified columns, with irregular data handled.
    """
    # File name
    filepath = name
    # Read the file
    df = pd.read_csv(filepath, sep="\t")
    # Select useful columns
    df = lp.get_columns(df, columns)
    # Clean columns with irregular data
    df = lp.clean_DataFrame(df)

    return df

def save_clean(archive: str) -> None:
    """
    Saves a cleaned CSV file containing only the relevant columns for analysis.

    Parameters
    ----------
    archive : str
        The name of the CSV file to be cleaned.
    
    Returns
    -------
    None
        The function saves the cleaned DataFrame to a file named '911_clean.csv'.
    """
    try:
        df_clean = clean(archive, columns)  # Creates a file with only the columns that everyone will work on
        df_clean = df_clean.drop_duplicates()
        df_clean.to_csv('911_clean.csv', sep='\t', index=False)
    except Exception as e:
        print(f"Error saving the file '{archive}': {e}")

save_clean('911_Calls_for_Service.csv')