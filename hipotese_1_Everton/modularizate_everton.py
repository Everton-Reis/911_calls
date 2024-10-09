import pandas as pd
from limpeza_main import clean
from limpeza2 import cleaning_by_term
import visual_everton as ve

def carregar_e_limpar_dados(filepath, columns):
    """
    Carrega e limpa os dados a partir do arquivo especificado.

    Parameters
    ----------
    filepath : str
        Caminho para o arquivo CSV a ser carregado.
    columns : list
        Lista de colunas a serem mantidas no DataFrame.

    Returns
    -------
    pd.DataFrame
        DataFrame limpo contendo apenas as colunas especificadas, sem os dados classificados como "Out of Service".
    """
    df = clean(filepath, columns)
    df = cleaning_by_term(df, 'priority', 'Out of Service')
    return df

def calcular_pontuacao(df, peso_mapeamento):
    """
    Calcula a pontuação total e a quantidade de crimes por local.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contendo os dados com as colunas 'Local' e 'Grau'.
    peso_mapeamento : dict
        Dicionário mapeando cada grau de crime a um peso.

    Returns
    -------
    pd.DataFrame
        DataFrame contendo a pontuação total e a quantidade de crimes por local, ordenado pela pontuação total em ordem decrescente.
    """
    contagem = df.groupby(['Local', 'Grau']).size().reset_index(name='Contagem')

    def pontuacao(row):
        peso = peso_mapeamento.get(row['Grau'], 0) / 10 
        return row['Contagem'] * peso

    contagem['Pontuacao'] = contagem.apply(pontuacao, axis=1)

    pontuacao_total = contagem.groupby('Local')['Pontuacao'].sum().reset_index(name='Pontuacao_Total')
    quantidade_crimes = contagem.groupby('Local')['Contagem'].sum().reset_index(name='Quantidade_Crimes')

    resultado = pd.merge(pontuacao_total, quantidade_crimes, on='Local')
    return resultado.sort_values(by='Pontuacao_Total', ascending=False)

def gerar_graficos(resultado):
    """
    Gera gráficos a partir do DataFrame de resultados.

    Parameters
    ----------
    resultado : pd.DataFrame
        DataFrame contendo as colunas 'Local', 'Pontuacao_Total' e 'Quantidade_Crimes'.

    Returns
    -------
    None
        Esta função não retorna nenhum valor, apenas gera e salva gráficos.
    """
    ve.bar1_plot_df(resultado, 'Local', 'Pontuacao_Total', 'Quantidade_Crimes', 'Grau Perigo')
    ve.bar2_plot_df(resultado, 'Pontuacao_Total', 'Quantidade_Crimes', 'Pontuacao x Quantidade')
    ve.scatter_plot_df(resultado, 'Quantidade_Crimes', 'Pontuacao_Total', 'Locais + perigosos')
