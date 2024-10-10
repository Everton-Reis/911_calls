import unittest
import pandas as pd
from unittest.mock import patch
from modularizate_everton import carregar_e_modificar_dados, calcular_pontuacao, pesos_normalizados, gerar_graficos

class TestDataProcessing(unittest.TestCase):

    @patch('modularizate_everton.clean')  # Mock da função clean
    def test_carregar_e_modificar_dados(self, mock_clean):
        # Configura o mock para retornar um DataFrame de exemplo
        mock_clean.return_value = pd.DataFrame({
            'Local': ['Local1', 'Local2'],
            'Grau': ['Low', 'High']
        })

        # Caso 1: Arquivo existe e colunas estão corretas
        df = carregar_e_modificar_dados('911.csv', ['Local', 'Grau'])
        self.assertIsNotNone(df)
        self.assertEqual(len(df), 2)  # Agora temos 2 entradas
        self.assertEqual(df.iloc[0]['Local'], 'Local1')
        self.assertEqual(df.iloc[1]['Local'], 'Local2')

        # Verifica se o DataFrame contém as colunas necessárias
        self.assertIn('Local', df.columns)
        self.assertIn('Grau', df.columns)

        # Caso 2: Simular erro de arquivo não encontrado
        mock_clean.side_effect = FileNotFoundError  # Simula que o arquivo não foi encontrado
        df = carregar_e_modificar_dados('inexistente.csv', ['Local', 'Grau'])
        self.assertIsNone(df)

    def test_calcular_pontuacao(self):
        # DataFrame de exemplo
        df = pd.DataFrame({
            'Local': ['Local1', 'Local1', 'Local2', 'Local2'],
            'Grau': ['Low', 'High', 'Low', 'High']
        })

        peso_mapeamento = {
            'Low': 1,
            'High': 2
        }

        resultado = calcular_pontuacao(df, peso_mapeamento)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.shape[0], 2)  # Deve retornar 2 locais / Uma verificação se o tamanho corresponde

        # Verificando a existência das colunas no resultado
        self.assertIn('Local', resultado.columns)
        self.assertIn('Pontuacao_Total', resultado.columns)
        self.assertIn('Quantidade_Crimes', resultado.columns)

        # Verificando os valores esperados
        esperado = pd.DataFrame({
            'Local': ['Local1', 'Local2'],
            'Pontuacao_Total': [0.3, 0.3],  # Ajustado já levando em conta a divisão por 10
            'Quantidade_Crimes': [2, 2]
        })

        pd.testing.assert_frame_equal(resultado.reset_index(drop=True), esperado)

    def test_pesos_normalizados(self):
        # Dados de exemplo para o teste
        dados = {
            'Low': 100,
          'High': 200,
           'Medium': 150
        }

        pesos = {
            'Low': 1,
            'High': 2,
            'Medium': 1.5
        }

        # Executando a função
        resultado = pesos_normalizados(dados, pesos)
        self.assertIsNotNone(resultado)

        # Valores esperados, calculados previamente com base nos dados e pesos
        esperado = {
            'Low': 0.000,
            'Medium': 0.877,
            'High': 2.000
        }

        # Verificando a existência de todas as chaves esperadas e valores próximos dos esperados
        for grau in pesos.keys():
            self.assertIn(grau, resultado)
            self.assertAlmostEqual(resultado[grau], esperado[grau], places=3)  # Comparação aproximada até 3 casas decimais

if __name__ == '__main__':
    unittest.main()
