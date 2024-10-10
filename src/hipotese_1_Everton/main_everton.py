import numpy as np
import pandas as pd
import modularizate_everton as me
from auxiliary_everton import cleaning_by_term

# Defining weight mapping
peso_inicial = {
        "Non-Emergency": 1,
        "Low": 5,
        "Medium": 25,
        "High": 75,
        "Emergency": 225
}

def main():
    """
    Main function that loads functions from the modularizate.

    Steps:
    1. Defines the path of the CSV file to be loaded.
    2. Specifies the columns of interest ('priority' and 'PoliceDistrict').
    3. Loads and cleans the data using the 'carregar_e_limpar_dados' function from the 'modularizate_everton' module.
    4. Creates a new DataFrame that contains the columns 'Local' (from 'PoliceDistrict') and 'Grau' (from 'priority').
    5. Calculates the total crime score for each location, using the 'calcular_pontuacao' function from the 'modularizate_everton' module.
    6. Generates graphs with the results using the 'gerar_graficos' function from the 'modularizate_everton' module.

    Returns
    -------
    None
        The function does not return any value, but generates graphs based on the calculated results.
    """
    filepath1 = '911.csv'

    columns = ['priority', 'PoliceDistrict']  # Columns that will be used for the analysis

    # Load and clean data
    df = me.carregar_e_modificar_dados(filepath1, columns)
    # Remove a severity that is useless for evaluation
    df = cleaning_by_term(df, 'priority', 'Out of Service')
    # Just a renaming modification.
    df = pd.DataFrame({'Local': df['PoliceDistrict'], 'Grau': df['priority']})
    print(df['Grau'].value_counts())
    # Transforms the occurrence information of grades into a dictionary
    dados_dict = df['Grau'].value_counts().to_dict()
    # Applies the occurrence information dictionary and the initial weight to normalize
    peso = me.pesos_normalizados(dados_dict, peso_inicial)
    print(peso)

    # Calculate score and sort
    resultado_final = me.calcular_pontuacao(df, peso)
    print(resultado_final)
    # Generate graphs
    me.gerar_graficos(resultado_final)

if __name__ == "__main__":
    main()
