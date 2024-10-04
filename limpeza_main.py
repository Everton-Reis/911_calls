import pandas as pd
import limpeza2 as lp

#columns=['recordId', 'callDateTime', 'priority', 'district', 'description', 'PoliceDistrict', 'ESRI_OID']

def clean(name, columns):
    filepath = name
    df = pd.read_csv(filepath, sep = "\t")
    #df = df[columns]
    df = lp.get_columns(df, columns)
    df = lp.clean_columns(df, columns)
    #print(df.head(5))
    #df = lp.padronizate(df)
    return df

# def read_csv(filepath, sep_file):
#     df = pd.read_csv(filepath, sep = sep_file)