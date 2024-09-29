import pandas as pd

filepath = "C:/Users/eliane/OneDrive/Documentos/A1LP/Projeto/Projeto/911_Calls_for_Service.csv"

def load_data(filepath):
    columns_to_use = ['recordId', 'district', 'description']
    df = pd.read_csv(filepath, usecols=columns_to_use, sep="\t") 
    return df[['recordId', 'district', 'description']].dropna()

df = load_data(filepath)

# Get the 30 most frequent descriptions.
top_descriptions = df['description'].value_counts().head(30)

# Save the most frequent descriptions in a CSV file.
top_descriptions_df = top_descriptions.reset_index()
top_descriptions_df.columns = ['Description', 'Count']
top_descriptions_df.to_csv('Top_30_Descriptions.csv', index=False)