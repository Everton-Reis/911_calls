import pandas as pd
from limpeza_main import clean
from auxiliary_everton import cleaning_by_term
import visual_everton as ve
import math

def carregar_e_modificar_dados(filepath, columns):
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
    try:
        df = clean(filepath, columns)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{filepath}' não foi encontrado.")
        return None
    except ValueError as e:
        print(f"Erro ao carregar colunas do arquivo: {e}")
        return None

    return df

def pesos_normalizados(dados: dict, pesos: dict) -> dict:
    """
    Calcula a pontuação normalizada, utilizando logaritimos e pesos padrões (que ajudam a balancear o peso para cada gravidade de ocorrência). 

    Parameters
    ----------
    dados : dict
        Dicionário contendo os dados de quantidade para cada grau.

    pesos : dict
        Dicionário contendo os pesos para cada grau.

    Returns
    -------
    dict
        Dicionário contendo a pontuação normalizada para cada grau.
    """
    try:
        if not set(pesos.keys()).issubset(dados.keys()):
            raise ValueError("Alguns graus não estão presentes no dicionário de dados.")
        
        # Normalização usando log
        valores = list(dados.values())
        if not valores:
            raise ValueError("O dicionário de dados está vazio.")
        # +1 para evitar log(0)
        log_min_val = math.log(min(valores) + 1)
        log_max_val = math.log(max(valores) + 1)

        if log_max_val == log_min_val:
            raise ValueError("Todos os valores no dicionário de dados são iguais. A normalização não é possível.") # Nesse caso, nossa normalização vai falhar, pois o denominador do grau vai ser zero.
        
        log_normalizado = {
            grau: (math.log(quantidade + 1) - log_min_val) / (log_max_val - log_min_val) # As ocorrências de grau "emergency", por serem em uma quantidade extremamente menor, são zeradas (e elas, de fato, não influenciam na análise)
            for grau, quantidade in dados.items()
        }

        # Cálculo da pontuação final aplicando os pesos e arredondando para 3 casas decimais
        pontuacao = {
            grau: round(log_normalizado[grau] * pesos[grau], 3)
            for grau in log_normalizado
        }

        return pontuacao
    
    except ValueError as ve:
        print(f"Erro de valor: {ve}")
        return {}
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return {}

def calcular_pontuacao(df: pd.DataFrame, peso_mapeamento: dict) -> pd.DataFrame:
    """
    Calcula a pontuação total e a quantidade de crimes por local com precisão de 3 casas decimais.

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
    try:
        contagem = df.groupby(['Local', 'Grau']).size().reset_index(name='Contagem')
    except KeyError as e:
        print(f"Erro: A coluna {e} não foi encontrada no DataFrame.")
        return None
    except Exception as e:
        print(f"Erro ao agrupar dados: {e}")
        return None

    try:
        def pontuacao(row):
            peso = peso_mapeamento.get(row['Grau'], 0) / 10
            return row['Contagem'] * peso

        contagem['Pontuacao'] = contagem.apply(pontuacao, axis=1)

        pontuacao_total = contagem.groupby('Local')['Pontuacao'].sum().reset_index(name='Pontuacao_Total')
        pontuacao_total['Pontuacao_Total'] = pontuacao_total['Pontuacao_Total'].round(3)  # Precisão de 3 casas decimais

        quantidade_crimes = contagem.groupby('Local')['Contagem'].sum().reset_index(name='Quantidade_Crimes')
        resultado = pd.merge(pontuacao_total, quantidade_crimes, on='Local')
        
        return resultado.sort_values(by='Pontuacao_Total', ascending=False)
    except Exception as e:
        print(f"Erro ao calcular a pontuação: {e}")
        return None

def gerar_graficos(resultado: pd.DataFrame) -> None:
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
    ve.bar2_plot_df(resultado, 'Pontuacao_Total', 'Quantidade_Crimes', 'Quantidade x Pontuação')
    ve.scatter_plot_df(resultado, 'Quantidade_Crimes', 'Pontuacao_Total', 'Locais + perigosos')
