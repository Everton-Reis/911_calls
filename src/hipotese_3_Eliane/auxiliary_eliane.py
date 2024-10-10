import pandas as pd

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
    """
    if df.empty or 'description' not in df.columns:
        raise ValueError("DataFrame is empty or missing 'description' column")
    
    top_descriptions = df['description'].value_counts().head(50)
    top_descriptions_df = top_descriptions.reset_index()
    top_descriptions_df.columns = ['Description', 'Count']
    top_descriptions_df.to_csv(output_csv, index=False)

    return top_descriptions_df

def remove_lines(filepath2):
    """
    Removes lines from CSV file where 'district' column contains unwanted words 
    and saves the cleaned data to a new CSV file to be used to generate the call
    distribution map by district in Baltimore.

    Parameters
    ----------
    filepath2: str
        The path to the CSV file that contains the data to be cleaned.

    Returns
    -------
    pandas.DataFrame
        A DataFrame with the rows containing unwanted words in the 'district' column removed.
    
    Notes
    -----
    The function removes rows where the 'district' column contains any of the following words: 
    'EVT1', 'TRU', 'SS', 'CW'. These words refer to special units or designations not linked to
    geographic districts, and are therefore excluded for the purposes of analyzing calls by standard districts.
    The cleaned data is saved in a new file called 'Cleaned_Call_Distribution.csv'.
    """
   
    df = pd.read_csv(filepath2)

    words_to_remove = ['EVT1', 'TRU', 'SS', 'CW'] 

    # If the line has either 'EVT1' or 'TRU' or 'SS' or 'CW', it is removed
    pattern = '|'.join(words_to_remove)
    df_cleaned = df[~df['district'].str.contains(pattern, case=False, na=False)]
    df_cleaned.to_csv('Cleaned_Call_Distribution.csv', index=False)

    return df_cleaned

def process_and_save_data(filepath, filepath2):
    """
    Main function to process data and save it for visualization. Calls the functions.

    Parameters
    ----------
    filepath : str
        The path to the CSV file containing the data '911_Calls_for_Service.csv'.
    filepath2 : str
        The path to the CSV file containing the data 'Call_Distribution_Percentage.csv'    
    """

    # Clean data in filepath2
    print("Removing unwanted rows from the file...")
    df_cleaned = remove_lines(filepath2)
    print("Rows removed. Cleaned data saved to 'Cleaned_Call_Distribution.csv'.")

    # Load and process the main data
    print("Loading data from the main file...")
    df = load_data(filepath)
    
    if not df.empty:
        print("Data loaded successfully. Extracting top 50 descriptions...")
        top_descriptions_df = save_top_descriptions(df)
        print("Top 50 descriptions saved to 'Top_50_Descriptions.csv'.")
    else:
        print("Failed to load data or data is empty.")