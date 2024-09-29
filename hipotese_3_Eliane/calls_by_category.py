import pandas as pd

filepath = "911_Calls_for_Service.csv"

# Load data from CSV file
def load_data(filepath):
    columns_to_use = ['recordId', 'district', 'description']
    df = pd.read_csv(filepath, usecols=columns_to_use, sep="\t")
    return df[['recordId', 'district', 'description']].dropna()

# Categorization of illegal activities to better visualize the distribution of calls
def categorize_activity(description):
    
    # Converting to uppercase to ensure all comparisons are consistent
    description = description.upper()

    # Categories
    against_person = ['HIT AND RUN', 'COMMON ASSAULT', 'FAMILY DISTURB', 'MISSING PERSON', 
                      'SUSPICIOUS PERS', 'LEWD ACT', 'DEATH REPORT', 'INTOXICATED PERS', 
                      'ASSISTANCE']
    
    against_public_property = ['DESTRUCT PROP', 'LOUD MUSIC', 'FALSE PRETENSE', 'AUTO ACCIDENT', 
                               'BURGLARY', 'LARCENY', 
                               'RECOVER PROPERTY', 'RECOVERED VEH', 'SQUEEGEE DIST', 'ILLEGAL DUMPING',
                               'AUDIBLE ALARM']

    against_public_welfare = ['NARCOTICS', 'DISORDERLY', 'LOUD MUSIC', 'PROSTITUTION']

    against_unknown = ['INVESTIGATE', 'OTHER', 'WANTED ON WARR', 'INVESTIGATE AUTO', 
                       'SUPV COMPLAINT', 'NOTIFY', 'FOLLOW UP']
    
    others = ['REPO', 'PRIVATE TOW', 'LOST PROPERTY', 'ESCORT', 'TOWED VEHICLE', 'PANHANDLER']

    # Checking the description category
    if any(keyword in description for keyword in against_person):
        return 'Against Person'
    elif any(keyword in description for keyword in against_public_property):
        return 'Against Public Property'
    elif any(keyword in description for keyword in against_public_welfare):
        return 'Against Public Welfare'
    elif any(keyword in description for keyword in against_unknown):
        return 'Against Unknown'
    elif any(keyword in description for keyword in others):
        return 'Others'
    else:
        return None

# Count the Calls
def call_counter(df):
    df['category'] = df['description'].apply(categorize_activity)
    return df.groupby(['district', 'category']).size().reset_index(name='call_count')

# Calculate distribution in percentage
def distribution_in_percentage(df):
    total_calls = df['call_count'].sum()
    df['percentage'] = (df['call_count'] / total_calls) * 100
    return df

# Save the processed data to a CSV file
def save_data(df, output_filepath):
    df.to_csv(output_filepath, index=False)

# Main function to process data and save it for visualization
def process_and_save_data(filepath, output_filepath):
    df = load_data(filepath)
    df_category_count = call_counter(df)
    df_category_percentage = distribution_in_percentage(df_category_count)
    
    # Save the data to CSV for visualization
    save_data(df_category_percentage, output_filepath)

if __name__ == "__main__":
    output_filepath = 'call_distribution_percentage.csv'  # Output file path for processed data
    process_and_save_data(filepath, output_filepath)