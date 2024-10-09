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

def categorize_activity(description):
    """"
    This function do the categorization of illegal activities to better visualize the distribution of calls.

    Before the categorization the descritions are converting to uppercase to ensure all comparisons are consistent.

    Parameters
    ----------
    descriptions: str
        A column that has the types of illegal activities.

    Returns
    -------
        Illegal activities categorized.   
    """
    
    description = description.upper()

    # Categories
    against_person = ['HIT AND RUN', 'COMMON ASSAULT', 'FAMILY DISTURB', 'MISSING PERSON', 
                  'ARMED PERSON', 'ROBBERY ARMED', 'AUTO ACCIDENT', 'BURGLARY', 'LARCENY',
                  'BEHAVIOR CRISIS', 'SICK CASE', 'AUTO ACC/INJURY']

    against_public_property = ['DESTRUCT PROP', 'FALSE PRETENSE', 
                            'AUTO THEFT', 'VEHICLE DISTURB', 'LARCENY F/AUTO']

    against_public_welfare = ['NARCOTICS', 'DISORDERLY', 'LOUD MUSIC', 'HOLDUP ALARM', 'SHOOTING',
                            'AGGRAV ASSAULT', 'OVERDOSE', 'DISCHRG FIREARM', 'SUSPICIOUS PERS',
                            'LYING IN STREET', 'STREET OBSTRUCT', 'SILENT ALARM', 'JUV DISTURBANCE']

    against_unknown = ['INVESTIGATE', 'OTHER', 'WANTED ON WARR', 'INVESTIGATE AUTO', 
                    'SUPV COMPLAINT', 'FOLLOW UP', '911/NO VOICE', 
                    'CHECK WELL BEING', 'CHECK WELLBEING', 'SEE TEXT', 'POLICE NOTIFY ON']
    
    uncategorized_high_frequency_descriptions = ['REPO', 'PRIVATE TOW', 'DIRECTED PATROL', 
                                                 'Business Check', 'INVEST','PICKUP ORDERS',
                                                 'AUDIBLE ALARM', 'PRKG COMPLAINT', 'EXPART/PROT/PEAC']

    # Checking the description category
    if any(keyword in description for keyword in against_person):
        return 'Against Person'
    elif any(keyword in description for keyword in against_public_property):
        return 'Against Public Property'
    elif any(keyword in description for keyword in against_public_welfare):
        return 'Against Public Welfare'
    elif any(keyword in description for keyword in against_unknown):
        return 'Against Unknown'
    elif any(keyword in description for keyword in uncategorized_high_frequency_descriptions):
        return 'Uncategorized High Frequency Descriptions'
    else:
        return 'Low Frequency Descriptions'

def call_counter(df):
    """ 
    This function counts calls from each category grouped by district to better analyze the distribution.

    Parameterr
    ----------
    df: DataFrame
        The DataFrame countains the recordId', 'district', and 'description' columns.

    Returns
    -------
    pandas.DataFrame
        A DataFrame with the values oh each category by district.
    """

    df['category'] = df['description'].apply(categorize_activity)
    return df.groupby(['district', 'category']).size().reset_index(name='call_count')

def distribution_in_percentage(df):
    """
    This function calculates the distribution in percentage of each category by district.

    Parameters
    ----------
    df: DataFrame
        The DataFrame countains the recordId', 'district', and 'description' columns.

    Returns
    -------
    df: pandas.DataFrame
        A DataFrame with the percentage of each category by district. 
    """

    df['total_calls'] = df.groupby('district')['call_count'].transform('sum')
    df['percentage'] = (df['call_count'] / df['total_calls']) * 100
    
    return df

def save_data(df, output_filepath):
    """
    This function save the processed data to a CSV file.

    Parameters
    ----------
    df: DataFrame
        The DataFrame countains the recordId', 'district', and 'description' columns.
    output_filepath: 'Call_Distribution_Percentage.csv'
        Used after the process of the following function 'process_and_save_data' called in the start. 
    """

    df.to_csv(output_filepath, index=False)

def process_and_save_data(filepath, output_filepath):
    """
    Main function to process data and save it for visualization. Calls the functions.

    Parameters
    ----------
    filepath : str
        The path to the CSV file containing the data.
    output_filepath: 'Call_Distribution_Percentage.csv'    
    """

    df = load_data(filepath)
    df_category_count = call_counter(df)
    df_category_percentage = distribution_in_percentage(df_category_count)
    save_data(df_category_percentage, output_filepath)