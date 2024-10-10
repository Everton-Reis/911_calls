import pandas as pd
import visual_everton as ve
import math
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from limpeza_main import clean

def carregar_e_modificar_dados(filepath, columns):
    """
    Loads and cleans data from the specified file.

    Parameters
    ----------
    filepath : str
        Path to the CSV file to be loaded.
    columns : list
        List of columns to be retained in the DataFrame.

    Returns
    -------
    pd.DataFrame
        Cleaned DataFrame containing only the specified columns, without data classified as "Out of Service".
    """
    try:
        df = clean(filepath, columns)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return None
    except ValueError as e:
        print(f"Error loading columns from the file: {e}")
        return None

    return df

def pesos_normalizados(dados: dict, pesos: dict) -> dict:
    """
    Calculates the normalized score using logarithms and standard weights (which help balance the weight for each severity of occurrence).

    Parameters
    ----------
    dados : dict
        Dictionary containing the quantity data for each severity.

    pesos : dict
        Dictionary containing the weights for each severity.

    Returns
    -------
    dict
        Dictionary containing the normalized score for each severity.
    """
    try:
        if not set(pesos.keys()).issubset(dados.keys()):
            raise ValueError("Some degrees are not present in the data dictionary.")
        
        # Normalization using log
        valores = list(dados.values())
        if not valores:
            raise ValueError("The data dictionary is empty.")
        # +1 for evite log(0)
        log_min_val = math.log(min(valores) + 1)
        log_max_val = math.log(max(valores) + 1)

        if log_max_val == log_min_val:
            raise ValueError("All values in the data dictionary are equal. Normalization is not possible.")  # In this case, our normalization will fail because the degree denominator will be zero.
        
        log_normalizado = {
            grau: (math.log(quantidade + 1) - log_min_val) / (log_max_val - log_min_val) # The occurrences of degree "emergency", due to being extremely fewer, are zeroed (and they indeed do not influence the analysis)
            for grau, quantidade in dados.items()
        }

        # Calculate the final score applying the weights and rounding to 3 decimal places
        pontuacao = {
            grau: round(log_normalizado[grau] * pesos[grau], 3)
            for grau in log_normalizado
        }

        return pontuacao
    
    except ValueError as ve:
        print(f"Value error: {ve}")
        return {}
    except Exception as e:
        print(f"An unexpected error ocurred: {e}")
        return {}

def calcular_pontuacao(df: pd.DataFrame, peso_mapeamento: dict) -> pd.DataFrame:
    """
    Calculates the total score and the number of crimes per location with a precision of 3 decimal places.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing data with the columns 'Local' and 'Grau'.
    weight_mapping : dict
        Dictionary mapping each degree of crime to a weight.

    Returns
    -------
    pd.DataFrame
        DataFrame containing the total score and the number of crimes per location, sorted by total score in descending order.
    """
    try:
        contagem = df.groupby(['Local', 'Grau']).size().reset_index(name='Contagem')
    except KeyError as e:
        print(f"Error: The column {e} was not found in the DataFrame.")
        return None
    except Exception as e:
        print(f"Error grouping data: {e}")
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
        print(f"Error calculating score: {e}")
        return None

def gerar_graficos(resultado: pd.DataFrame) -> None:
    """
    Generates charts from the result DataFrame.

    Parameters
    ----------
    result : pd.DataFrame
        DataFrame containing the columns 'Local', 'Total_Score', and 'Crime_Count'.

    Returns
    -------
    None
        This function does not return any value; it only generates and saves charts.
    """
    ve.bar1_plot_df(resultado, 'Local', 'Pontuacao_Total', 'Quantidade_Crimes', 'Mais perigosos')
    ve.bar2_plot_df(resultado, 'Pontuacao_Total', 'Quantidade_Crimes', 'Quantidade x Pontuação')
    ve.scatter_plot_df(resultado, 'Quantidade_Crimes', 'Pontuacao_Total', 'Relação')
