import pandas as pd

filepath = "911_Calls_for_Service.csv"

def load_data(filepath):
    """
    Load data from a CSV file, selecting specific columns and dropping rows with missing values.

    Parameters
    ----------
    filepath : str
        The path to the CSV file containing the data.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the 'recordId', 'district', and 'description' columns, with missing values removed.
    """
    
    columns_to_use = ['recordId', 'district', 'description']
    try:
        df = pd.read_csv(filepath, usecols=columns_to_use, sep="\t") 
        return df[['recordId', 'district', 'description']].dropna()
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found.")
        return pd.DataFrame() 
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame() 


def save_top_descriptions(df, output_csv='Top_50_Descriptions.csv'):
    """
    Extracts the 50 most frequent descriptions from the DataFrame and saves them to a CSV file.

    Parameters
    ----------
    df : pandas.DataFrame
        The input DataFrame that contains the 'description' column.
    output_csv : str
        The path where the output CSV file will be saved (default is 'Top_50_Descriptions.csv').

    Returns
    -------
    top_descriptions_df
    """
    
    top_descriptions = df['description'].value_counts().head(50)
    top_descriptions_df = top_descriptions.reset_index()
    top_descriptions_df.columns = ['Description', 'Count']
    top_descriptions_df.to_csv(output_csv, index=False)

    return top_descriptions_df

df = load_data(filepath)
if not df.empty: 
    save_top_descriptions(df)