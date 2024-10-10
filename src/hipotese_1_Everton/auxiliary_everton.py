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
        file = file[columns]  # Trabalha diretamente na referência ao DataFrame original
        return file
    except KeyError as e:
        colunas_faltando = list(set(columns) - set(file.columns))
        print(f"As colunas {colunas_faltando} não estão presentes no DataFrame.")
        return file  # Retorna o DataFrame original em caso de erro

def cleaning_by_term(file: pd.DataFrame, column: str, term: any) -> pd.DataFrame:
    """
    Remove linhas de um DataFrame onde uma coluna específica contém um valor específico, alterando o DataFrame original.

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
        O DataFrame original com as linhas removidas onde o termo estava presente na coluna.
    """
    try:
        # Verifica se a coluna existe no DataFrame
        if column not in file.columns:
            raise ValueError(f"A coluna '{column}' não existe no DataFrame.")
        
        # Remove as linhas onde o valor da coluna é igual ao termo
        file.drop(file[file[column] == term].index, inplace=True)
        
    except Exception as e:
        print(f"Ocorreu um erro durante a limpeza do DataFrame: {e}")
    
    return file

def clean_DataFrame(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpa as linhas do DataFrame que possuem ao menos um valor faltando em uma de suas linhas.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame que contém as colunas a serem limpas.
    
    Returns
    -------
    pandas.DataFrame
        DataFrame com as colunas/linhas limpas.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("O argumento fornecido não é um pd.DataFrame.")  # Verifica se o df é um DataFrame e não uma Series
    
    try:
        df_clean = df.dropna()
    except Exception as e:
        raise ValueError(f"Não foi possível limpar as linhas: {e}")  # Inclui detalhes do erro na mensagem de exceção
        
    return df_clean