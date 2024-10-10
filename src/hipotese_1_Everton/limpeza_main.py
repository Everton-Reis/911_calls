import pandas as pd
import auxiliary_everton as lp

columns = ['recordId', 'callDateTime', 'priority', 'district', 'description', 'PoliceDistrict', 'ESRI_OID']

def clean(name, columns):
    """
    Limpa os dados de um arquivo CSV, mantendo apenas as colunas úteis e limpando dados irregulares.

    Parameters
    ----------
    name : str
        O nome do arquivo CSV a ser lido. O arquivo deve estar no formato tabulado (diferente do comum que é a virgula).

    columns : list
        Lista de colunas que continuam no DataFrame.

    Returns
    -------
    pd.DataFrame
        Um DataFrame contendo apenas as colunas especificadas, com dados irregulares tratados.
    """
    # Nome do arquivo
    filepath = name
    # Lê o arquivo
    df = pd.read_csv(filepath, sep="\t")
    # Seleciona as colunas úteis
    df = lp.get_columns(df, columns)
    # Limpa colunas com dados irregulares
    df = lp.clean_DataFrame(df)

    return df

def save_clean(archive):
    """
    Salva um arquivo CSV limpo contendo apenas as colunas relevantes para análise.

    Parameters
    ----------
    archive : str
        O nome do arquivo CSV a ser limpo.
    
    Returns
    -------
    None
        A função salva o DataFrame limpo em um arquivo chamado '911_clean.csv'.
    """
    try:
        df_clean = clean(archive, columns)  # Criação do arquivo com apenas as colunas que todos irão trabalhar
        df_clean.to_csv('911_clean.csv', index=False)
    except Exception as e:
        print(f"Erro ao salvar o arquivo '{archive}': {e}")