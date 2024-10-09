import pandas as pd

def get_columns(file, columns):
    """
    Retorna um sub_file contendo apenas as colunas desejadas.

    Parameters
    ----------
    file : pandas.DataFrame
        DataFrame do qual o sub_file com as colunas desejadas será extraído.
    
    columns : list
        Lista das colunas desejadas no subfile.

    Returns
    -------
    pandas.DataFrame
        DataFrame contendo apenas as colunas especificadas.
    """
    try:
        file_modificate = file[columns].copy()  # Garantir que faz uma cópia
        print(file_modificate.head())
        return file_modificate
    except KeyError as e:
        colunas_faltando = list(set(columns) - set(file.columns))
        print(f"As colunas {colunas_faltando} não estão presentes no DataFrame.")
        return file  # Retorna o dataframe original em caso de erro


def cleaning_by_term(file, column, term):
    """
    Remove linhas de um DataFrame onde uma coluna específica contém um valor específico.

    Parameters
    ----------
    file : pandas.DataFrame
        DataFrame a ser limpo.
    
    column : str
        Coluna na qual a limpeza será aplicada.
    
    term : any
        Termo que será removido da coluna.

    Returns
    -------
    pandas.DataFrame
        DataFrame com as linhas removidas onde o termo estava presente na coluna.
    """
    file_modificate = file[file[column] != term].copy()  # Garantir que faz uma cópia
    return file_modificate


def cleaning_lines(file: pd.Series) -> pd.Series:
    """
    Limpa uma Series, removendo valores nulos e duplicatas.

    Parameters
    ----------
    file : pd.Series
        A Series que será limpa.

    Returns
    -------
    pd.Series
        Series sem valores nulos e duplicatas.
    """
    if not isinstance(file, pd.Series):
        raise ValueError("O argumento fornecido não é uma pd.Series.")
    
    file_modificate = file.dropna().copy()  # Garantir que faz uma cópia
    return file_modificate


def clean_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Limpa colunas específicas de um DataFrame, removendo valores nulos e duplicatas.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame que contém as colunas a serem limpas.
    
    columns : list
        Lista de colunas que serão limpas no DataFrame.

    Returns
    -------
    pandas.DataFrame
        DataFrame com as colunas especificadas limpas.
    """
    for col in columns:
        if col in df.columns:
            print(f"Limpando coluna: {col}")
            print(f"Valores antes da limpeza: {df[col].count()} linhas")
            df[col] = cleaning_lines(df[col])  # Usando a função cleaning_lines para limpar cada coluna
            print(f"Valores após a limpeza: {df[col].count()} linhas")
        else:
            print(f"Coluna '{col}' não encontrada no DataFrame.")
    return df
def padronizate(file: pd.Series):
    """
    Padroniza valores string para letras maiúsculas.

    Parameters
    ----------
    file : pd.Series
        Série de dados a serem padronizados.

    Returns
    -------
    pd.Series
        Série com valores string padronizados para maiúsculas.
    """
    try:
        return file.apply(lambda x: x.lower() if isinstance(x, str) else x)
    except Exception as e:
        print(f"Erro ao padronizar os valores: {e}")
        return file
