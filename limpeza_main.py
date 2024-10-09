import pandas as pd
import limpeza2 as lp

#columns=['recordId', 'callDateTime', 'priority', 'district', 'description', 'PoliceDistrict', 'ESRI_OID']

def clean(name, columns):
    # file name
    filepath = name
    # read the file
    df = pd.read_csv(filepath, sep = "\t")
    # choose useful columns
    df = lp.get_columns(df, columns)
    # clean columns with irregular data
    df = lp.clean_columns(df, columns)
    
    return df