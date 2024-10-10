import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import pandas as pd

def bar1_plot_df(df, linha_1, coluna_2_1, coluna_2_2, titulo, nome_arquivo='grafico_barra1.png'):
    """
    Cria um gráfico de barra a partir do DataFrame de entrada, tendo como eixo x a linha_1 e y a coluna_2_1 e/ou coluna_2_2.
    
    Parâmetros
    ----------
    df (pd.DataFrame): O DataFrame com os dados analisados.
    linha_1 (str): Uma das colunas do DataFrame (Contudo, vai representar o eixo x).
    coluna_2_1 (str): Uma das colunas do DataFrame.
    coluna_2_2 (str): Uma das colunas do DataFrame.
    titulo (str): Título para o gráfico de barra.
    nome_arquivo (str): Nome do arquivo onde o gráfico será salvo.
    """
    if linha_1 not in df.columns or coluna_2_1 not in df.columns or coluna_2_2 not in df.columns:
        raise ValueError("Não há colunas com os nomes inseridos no DataFrame.")

    # Criar o gráfico de barra com cores roxo e azul
    ax = df.plot.bar(x=linha_1, y=[coluna_2_1, coluna_2_2], title=titulo, color=['purple', 'blue'])
    
    # Configurações adicionais
    plt.xlabel(linha_1)  # Rótulo do eixo X
    plt.ylabel('Valores')  # Rótulo do eixo Y
    plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo X
    plt.grid(axis='y')  # Mostra a grade apenas no eixo Y
    plt.tight_layout()  # Ajusta o layout para evitar sobreposição

    # Salvar e fechar o gráfico em um arquivo
    plt.savefig(nome_arquivo)
    plt.close()  

import matplotlib.pyplot as plt
import pandas as pd

def bar2_plot_df(df, linha_1, coluna_2, titulo, nome_arquivo='grafico_barra2.png'):
    """
    Cria um gráfico de barra a partir do DataFrame de entrada, tendo como eixo x a linha_1 e y a coluna_2.
    
    Parâmetros
    ----------
    df (pd.DataFrame): O DataFrame com os dados analisados.
    linha_1 (str): Uma das colunas do DataFrame (Contudo, vai representar o eixo x).
    coluna_2 (str): Uma das colunas do DataFrame.
    titulo (str): Título para o gráfico de barra.
    nome_arquivo (str): Nome do arquivo onde o gráfico será salvo.
    """
    if linha_1 not in df.columns or coluna_2 not in df.columns:
        raise ValueError("Não há colunas com os nomes inseridos no DataFrame.")

    # Criar o gráfico de barra 
    ax = df.plot.bar(x=linha_1, y=coluna_2, color='purple', title=titulo)
    
    # Configurações adicionais
    plt.xlabel(linha_1)  # Rótulo do eixo X
    plt.ylabel('Valores')  # Rótulo do eixo Y
    plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo X
    plt.grid(axis='y')  # Mostra a grade apenas no eixo Y
    plt.tight_layout()  # Ajusta o layout para evitar sobreposição

    # Salvar e fechar o gráfico em um arquivo
    plt.savefig(nome_arquivo)
    plt.close()  

import pandas as pd
import matplotlib.pyplot as plt

def scatter_plot_df(df, linha_1, coluna_2, titulo, nome_arquivo='grafico_scatter.png'):
    """
    Cria um gráfico de scatter (dispersão) a partir do DataFrame de entrada, tendo como eixo x a linha_1 e y a coluna_2.
    
    Parâmetros
    ----------
    df (pd.DataFrame): O DataFrame com os dados analisados.
    linha_1 (str): Uma das colunas do DataFrame (Contudo, vai representar o eixo x).
    coluna_2 (str): Uma das colunas do DataFrame.
    titulo (str): Título para o gráfico de scatter.
    nome_arquivo (str): Nome do arquivo onde o gráfico será salvo.
    """
    if linha_1 not in df.columns or coluna_2 not in df.columns:
        raise ValueError("Não há colunas com os nomes inseridos no DataFrame.")

    # Criar o gráfico de scatter
    ax = df.plot.scatter(x=linha_1, y=coluna_2, color='purple', title=titulo)
    plt.grid()

    # Salvar e fechar o gráfico em um arquivo
    plt.savefig(nome_arquivo)
    plt.close() 

