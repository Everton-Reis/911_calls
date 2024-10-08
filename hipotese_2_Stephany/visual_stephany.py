import pandas as pd
from matplotlib import pyplot as plt

def plot_graf_pie_by_hour(df: pd.Series, hour: str, file_name: str):
    """
    Read the data file indicated by file_path.
    The file must be in csv format.

    Parameters
    ----------
    file_path: str
        The path to the file containing the data files.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the 'callDateTime', 'priority' and 'description' columns.

    Raises
    ------
    FileNotFoundError
        If the file does not exist
    """
    graf_df = df[df['hour'] == hour]
    graf_df_groupby = graf_df.groupby(['description']).size()
    graf_df_groupby = graf_df_groupby.sort_values(ascending=[False])
    
    graf_df_groupby.plot.pie(
        y='description', 
        autopct='%1.1f%%',  # Mostrar percentuais
        colors=['#3A3661', '#423b6a', '#6b6295', '#9589bf','#beb0ea'],
        explode=[0.1] + [0] * (len(graf_df_groupby) - 1),  # Destacando a primeira fatia
    )

    plt.title(f"Principais ocorencias às {hour} horas")
    plt.savefig(file_name, dpi=300)

def plot_graf_bar(df: pd.Series, x: str,y: str):
   # df.plot.bar(x=x, y=y)
   
    colors = ['#3A3661', '#423b6a', '#6b6295', '#9589bf', '#beb0ea']
    ax = df.plot.bar(x=x, y=y, color=colors, width=0.8, figsize=(15, 6))
    plt.title('Número de ligações por hora', fontsize=18, weight='bold')
    plt.xlabel('horarios', fontsize=12)
    plt.ylabel('ligações', fontsize=12)

    # Girando os rótulos do eixo X, se necessário
    plt.xticks(rotation=45, ha='right', fontsize=10)  # Rotaciona os rótulos no eixo X
    plt.yticks(fontsize=10)  # Tamanho da fonte no eixo Y
    
    # Adicionando rótulos de valor nas barras
    for columns in ax.containers:
        ax.bar_label(columns, label_type='edge', fontsize=10, color='black')

    plt.savefig('test_image_2.png', dpi=300)