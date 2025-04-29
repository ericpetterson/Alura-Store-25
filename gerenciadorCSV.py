import os
import pandas as pd

class GerenciadorCSV:
    def __init__(self, pasta_dados="dados"):
        self.pasta_dados = pasta_dados
        self.dataframes = {}
        self._carregar_csvs()

    def _carregar_csvs(self):
        """Carrega todos os arquivos CSV da pasta para o dicionário."""
        if not os.path.exists(self.pasta_dados):
            raise FileNotFoundError(f"Pasta '{self.pasta_dados}' não encontrada.")

        arquivos = [f for f in os.listdir(self.pasta_dados) if f.endswith('.csv')]

        for arquivo in arquivos:
            nome_base = os.path.splitext(arquivo)[0]
            caminho = os.path.join(self.pasta_dados, arquivo)
            self.dataframes[nome_base] = pd.read_csv(caminho)

    def listar_arquivos(self):
        """Lista todos os nomes de DataFrames carregados."""
        return list(self.dataframes.keys())

    def pegar_dataframe(self, nome):
        """Retorna o DataFrame correspondente ao nome dado."""
        if nome in self.dataframes:
            return self.dataframes[nome]
        else:
            raise KeyError(f"DataFrame '{nome}' não encontrado.")

    def analise_inicial(self, nome):
        """Realiza uma análise inicial do DataFrame especificado."""
        if nome in self.dataframes:
            df = self.dataframes[nome]
            print("Formato:", df.shape)
            print("\nColunas:", df.columns.tolist())
            print("\nTipos de dados:")
            print(df.dtypes)
            print("\nValores nulos:")
            print(df.isnull().sum())
            print("\nResumo estatístico:")
            print(df.describe())
            print("\nPrimeiras linhas:")
            print(df.head())
        else:
            raise KeyError(f"DataFrame '{nome}' não encontrado.")
