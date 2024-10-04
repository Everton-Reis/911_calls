import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import visual_everton as ve
import limpeza_main as lm

filepath = '911.csv'
columns=['priority', 'PoliceDistrict']
df = lm.clean(filepath, columns)
print(df.head())

def gerar_dados(dataframe):

    #d_f=dataframe.drop_duplicates() # limpar as duplicatas
    #subset_df = d_f[['PoliceDistrict', 'priority']] # só as duas colunas que vou usar
    
    district = dataframe['PoliceDistrict'] # pegando os distritos
    grau_ocorrencia = dataframe['priority'] # pegando o grau da ocorrencia
    grau_ocorrencia = grau_ocorrencia.dropna()

    df2 = pd.DataFrame({'Local': district, 'Grau': grau_ocorrencia})
    #print(df2)
    df2 = df2[df2['Grau'] != 'Out of Service'] # retirei o tipo que não quero trabalhar, pois ele não diz nada sobre a periculosidade do local
    # print(df2['Grau'].unique()) # isso visualiza se há apenas os graus de ocorrência que quero trabalhar
    contagem = df2.groupby(['Local', 'Grau']).size() # a contagem de cada tipo de ocorrencia para cada local
    #print(contagem)
    # contar_emergencias = df2['Grau'].value_counts() # quantidade de cada tipo
    # print(contar_emergencias)

    contagem = df2.groupby(['Local', 'Grau']).size().reset_index(name='Contagem') # a contagem de cada tipo de ocorrencia para cada local, só que mais especifico
    #print(contagem)
    peso_mapeamento = {
        'Low': 5,
        'Medium': 25,
        'Non-Emergency': 1,
        'High': 75,
        'Emergency': 225
    }
    # tirar  o pesos e colocar pesos_mapeamento
    def calcular_pontuacao(row):
        peso = peso_mapeamento.get(row['Grau'], 0) / (10) # retorna o valor do item com a key especifica, a divisão por 10 é apenas para melhor visualização
        return row['Contagem'] * peso

    contagem['Pontuacao'] = contagem.apply(calcular_pontuacao, axis = 1)
    print(contagem)

    pontuacao_total_regiao = contagem.groupby('Local')['Pontuacao'].sum().reset_index(name='Pontuacao_Total')

    quantidade_crimes = contagem.groupby('Local')['Contagem'].sum().reset_index(name='Quantidade_Crimes')

    resultado_final = pd.merge(pontuacao_total_regiao, quantidade_crimes, on='Local') # junta os dois DF que tenho pela coluna em comum.
    resultado_final = resultado_final.sort_values(by='Pontuacao_Total', ascending=False) # ordena

    print(resultado_final)

    # ve.bar1_plot_df(resultado_final, 'Local', 'Pontuacao_Total', 'Quantidade_Crimes', 'Grau Perigo')
    # ve.bar2_plot_df(resultado_final, 'Pontuacao_Total', 'Quantidade_Crimes', 'Pontuacao x Quantidade')
    # ve.scatter_plot_df(resultado_final, 'Quantidade_Crimes', 'Pontuacao_Total', 'Locais + perigosos')
    
gerar_dados(df)

