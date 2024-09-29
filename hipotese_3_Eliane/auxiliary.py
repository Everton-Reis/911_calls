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

    Notes
    -----
    The CSV file is expected to have columns 'recordId', 'district', and 'description'.
    The function reads the file with tab (`\t`) as the separator and selects only these columns.
    """
    
    columns_to_use = ['recordId', 'district', 'description']
    df = pd.read_csv(filepath, usecols=columns_to_use, sep="\t") 
    return df[['recordId', 'district', 'description']].dropna()


def save_top_descriptions(df, output_csv="Top_30_Descriptions.csv"):
    """
    Extracts the 30 most ferquent descriptions from the DataFrame and saves them to a CSV file.

    Parameters
    ----------
    df : pandas.DataFrame
        The input DataFrame that contains the 'description' column.
    output_csv : str
        The path where the output CSV file will be saved (defalt is 'Top_30_Descriptions.csv').

    Returns
    -------
    None

    Notes
    -----
    The function selects the top 30 most frequent values from the 'description' column,
    counts their occurrences, and saves them to a csv file with two columns:
    'Descriptions' and 'Count'.
    """
    
    top_descriptions = df['description'].value_counts().head(30)
    top_descriptions_df = top_descriptions.reset_index()
    top_descriptions_df.columns = ['Description', 'Count']
    top_descriptions_df.to_csv('Top_30_Descriptions.csv', index=False)

df = load_data(filepath)
save_top_descriptions(df)