import numpy as np
import pandas as pd
filepath = "911.csv"

df = pd.read_csv(filepath, sep='\t')
#print(df.head()) # observar as 5 primeiras linhas
#print(df.columns)

def gerar_dados(dataframe):
    d_f=dataframe.drop_duplicates() # limpar as duplicatas
    subset_df = d_f[['PoliceDistrict', 'priority']] # só as duas colunas que vou usar
    
    district = subset_df['PoliceDistrict'] # pegando os distritos
    grau_ocorrencia = subset_df['priority'] # pegando o grau da ocorrencia

    df2 = pd.DataFrame({'Local': district, 'Grau': grau_ocorrencia})
    #print(df2)
    df2 = df2[df2['Grau'] != 'Out of Service'] # retirei o tipo que não quero trabalhar, pois ele não diz nada sobre a periculosidade do local
    print(df2['Grau'].unique())
    contagem = df2.groupby(['Local', 'Grau']).size() # a contagem de cada tipo de ocorrencia pra cada tipo de local

    print(contagem) 

    contar_emergencias = df2['Grau'].value_counts() # quantidade de cada tipo
    print(contar_emergencias)
    list_points = [1, 5, 25, 75, 225]
    # total = contar_emergencias.sum() # pegando a soma total pra ponderar
    pont_total = 10000 # atribuindo uma pontuação para o numero final de pontos de cada cidade não ser tão pequeno
    pesos = (df2['Grau'].value_counts() * list_points / (10 ** 6))
    print(pesos)

    contagem = df2.groupby(['Local', 'Grau']).size().reset_index(name='Contagem')
    #print(contagem)

    def calcular_pontuacao(row):
        peso = pesos.get(row['Grau'], 0) # retorna o valor do item com a key especifica
        return row['Contagem'] * peso

    contagem['Pontuacao'] = contagem.apply(calcular_pontuacao, axis = 1)
    print(contagem)

    pontuacao_total_regiao = contagem.groupby('Local')['Pontuacao'].sum().reset_index(name='Pontuacao_Total')

    quantidade_crimes = contagem.groupby('Local')['Contagem'].sum().reset_index(name='Quantidade_Crimes')

    resultado_final = pd.merge(pontuacao_total_regiao, quantidade_crimes, on='Local')
    resultado_final = resultado_final.sort_values(by='Pontuacao_Total', ascending=False)
    print(resultado_final)
    # max_contagem = contagem.groupby('Local')['Contagem'].max().reset_index(name='MaxContagem')
    # print(max_contagem)

    # idx_max_contagem = contagem.groupby('Local')['Contagem'].idxmax()
    # max_contagem = contagem.loc[idx_max_contagem].reset_index(drop=True)
    # print(max_contagem)
    
gerar_dados(df)

