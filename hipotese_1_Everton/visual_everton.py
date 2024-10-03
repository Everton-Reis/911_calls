import pandas as pd
import matplotlib.pyplot as plt

def bar1_plot_df(df, linha_1, coluna_2_1, coluna_2_2, titulo):
    """
    Cria um gráfico de barra a partir do DataFrame de entrada, tendo como eixo x a linha_1 e y a coluna_2_1 e/ou coluna_2_2.
    
    Parâmetros
    ----------
    df (pd.DataFrame): O DataFrame com os dados analisados.
    linha_1 (str): Uma das colunas do DataFrame (Contudo, vai representar o eixo x).
    coluna_2_1 (str): Uma das colunas do DataFrame.
    coluna_2_2 (str): Uma das colunas do DataFrame.
    título (str): Título para o gráfico de barra.
    """
    if linha_1 not in df.columns or coluna_2_1 not in df.columns or coluna_2_2 not in df.columns:
        raise ValueError("Não há colunas com os nomes inseridos no DataFrame.")

    # Criar o gráfico de barra
    df.plot.bar(x=linha_1, y=[coluna_2_1, coluna_2_2], title = titulo) 
    plt.legend()
    plt.grid()
    plt.show()

def bar2_plot_df(df, linha_1, coluna_2, titulo):
    """
    Cria um gráfico de barra a partir do DataFrame de entrada, tendo como eixo x a linha_1 e y a coluna_2.
    
    Parâmetros
    ----------
    df (pd.DataFrame): O DataFrame com os dados analisados.
    linha_1 (str): Uma das colunas do DataFrame (Contudo, vai representar o eixo x).
    coluna_2 (str): Uma das colunas do DataFrame.
    título (str): Título para o gráfico de barra.
    """
    if linha_1 not in df.columns or coluna_2 not in df.columns:
        raise ValueError("Não há colunas com os nomes inseridos no DataFrame.")

    # Criar o gráfico de barra
    df.plot.bar(x=linha_1, y=coluna_2, title = titulo) 
    plt.legend()
    plt.grid()
    plt.show()

def scatter_plot_df(df, linha_1, coluna_2, titulo):
    """
    Cria um gráfico de scatter (dispersão) a partir do DataFrame de entrada, tendo como eixo x a linha_1 e y a coluna_2.
    
    Parâmetros
    ----------
    df (pd.DataFrame): O DataFrame com os dados analisados.
    linha_1 (str): Uma das colunas do DataFrame (Contudo, vai representar o eixo x).
    coluna_2 (str): Uma das coluna do DataFrame.
    título (str): Título para o gráfico de barra.
    """
    if linha_1 not in df.columns or coluna_2 not in df.columns:
        raise ValueError("Não há colunas com os nomes inseridos no DataFrame.")

    # Criar o gráfico de scatter
    df.plot.bar(x=linha_1, y=coluna_2, title = titulo) 
    plt.legend()
    plt.grid()
    plt.show()


