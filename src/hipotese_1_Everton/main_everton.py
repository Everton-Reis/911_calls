import numpy as np
import pandas as pd
import modularizate_everton as me
from auxiliary_everton import cleaning_by_term

# Definição do mapeamento de pesos 
peso_inicial = {
        "Non-Emergency": 1,
        "Low": 5,
        "Medium": 25,
        "High": 75,
        "Emergency": 225
}

def main():
    """
    Função principal que carrega as funções da modularizate.

    Steps:
    1. Define o caminho do arquivo CSV a ser carregado.
    2. Especifica as colunas de interesse ('priority' e 'PoliceDistrict').
    3. Carrega e limpa os dados utilizando a função 'carregar_e_limpar_dados' do módulo 'modularizate_everton'.
    4. Cria um novo DataFrame que contém as colunas 'Local' (a partir de 'PoliceDistrict') e 'Grau' (a partir de 'priority').
    5. Calcula a pontuação total de crimes para cada local, utilizando a função 'calcular_pontuacao' do módulo 'modularizate_everton'.
    6. Gera gráficos com os resultados utilizando a função 'gerar_graficos' do módulo 'modularizate_everton'.

    Returns
    -------
    None
        A função não retorna nenhum valor, mas gera gráficos baseados nos resultados calculados.
    """
    filepath1 = '911.csv'

    columns = ['priority', 'PoliceDistrict']  # Colunas que vão ser usadas para a análise

    # Carregar e limpar dados
    df = me.carregar_e_modificar_dados(filepath1, columns)
    # Retirar uma gravidade inutil para a avaliação
    df = cleaning_by_term(df, 'priority', 'Out of Service')
    # Apenas uma modificação de nomes.
    df = pd.DataFrame({'Local': df['PoliceDistrict'], 'Grau': df['priority']})
    print(df['Grau'].value_counts())
    # Transforma as informações de ocorrência dos graus em dicionario
    dados_dict = df['Grau'].value_counts().to_dict()
    # Aplica o diciorio de informações de ocorrência e de peso inicial para normalizar
    peso = me.pesos_normalizados(dados_dict, peso_inicial)
    print(peso)

    # Calcular pontuação e ordenar
    resultado_final = me.calcular_pontuacao(df, peso)
    print(resultado_final)
    # Gerar gráficos
    me.gerar_graficos(resultado_final)

if __name__ == "__main__":
    main()
