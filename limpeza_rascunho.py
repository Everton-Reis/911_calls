import pandas as pd

filepath = "911_Calls_for_Service.csv"

def read_csv(filepath, sep_file):
    df = pd.read_csv(filepath, sep = sep_file)


def get_columns(file, columns):
    """
    Return a sub_file that contains only the used columns
    
    Parameters
    ---------

    file
        File from which the sub_file with the desired columns will be extracted
    
    columns: list
        Desired columns in subfile
    """
    try:
        file_modificate = file[columns]
        return file_modificate
    except KeyError:
        print("There are a non index in columns")    

def cleaning_by_term(file, column, term):
    file_modificate = file[file[column] != term]
    return file_modificate

def cleaning_lines(file: pd.Series):
    file_modificate = file.dropna()
    file_modificate = file_modificate.drop_duplicates()
    return file_modificate

def padronizate(file: pd.Series):
    return file.apply(lambda x: x.upper() if isinstance(x,str) else x)

def checando_entrada(file, columns):
    pass
columns=['recordId', 'callDateTime', 'priority', 'district', 'description', 'PoliceDistrict', 'ESRI_OID']

df = pd.read_csv(filepath, sep = "\t")
get_columns(df, columns)