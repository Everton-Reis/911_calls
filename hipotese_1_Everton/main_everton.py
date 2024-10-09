import numpy as np
import pandas as pd
import modularizate_everton as me

# Definição do mapeamento de pesos 
peso_mapeamento = {
        "Non-Emergency": 1,
        "Low": 5,
        "Medium": 25,
        "High": 75,
        "Emergency": 225
}
def main():
    filepath = '911.csv'
    columns = ['priority', 'PoliceDistrict'] # colunas dentre as que quero trabalhar

    # Carregar e limpar dados
    df = me.carregar_e_limpar_dados(filepath, columns)

    # Adicionar colunas de Local e Grau
    df = pd.DataFrame({'Local': df['PoliceDistrict'], 'Grau': df['priority']})

    # Calcular pontuação e ordenar

    resultado_final = me.calcular_pontuacao(df, peso_mapeamento)

    # Gerar gráficos
    me.gerar_graficos(resultado_final)

if __name__ == "__main__":
    main()