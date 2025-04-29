from gerenciadorCSV import GerenciadorCSV

df = GerenciadorCSV()

class AnaliseDados:
    def __init__(self, df):
        self.df = df

    def analise_faturamento(self):
        for nome in self.df.listar_arquivos():
            if nome.startswith('loja_'):
                df_loja = self.df.pegar_dataframe(nome)
                faturamento = df_loja["Preço"].sum()
                print(f"Total de faturamento da {nome.replace('_', ' ')}: R$ {faturamento:.2f}")

    def vendas_por_categoria(self):
        for nome in self.df.listar_arquivos():
            if nome.startswith('loja_'):
                df_loja = self.df.pegar_dataframe(nome)
                vendas_por_categoria = df_loja["Categoria do Produto"].value_counts()
                print(f"Quantidade de vendas por categoria da {nome.replace('_', ' ')}:")
                print(vendas_por_categoria)
                print("\n")

    def produtos_mais_menos_vendidos(self):
        for nome in self.df.listar_arquivos():
            if nome.startswith('loja_'):
                df_loja = self.df.pegar_dataframe(nome)
                produtos_mais_vendidos = df_loja["Produto"].value_counts().head(5)
                produtos_menos_vendidos = df_loja["Produto"].value_counts().tail(5)

                print(f"Produtos mais vendidos da {nome.replace('_', ' ')}:")
                print(produtos_mais_vendidos)
                print("\n")

                print(f"Produtos menos vendidos da {nome.replace('_', ' ')}:")
                print(produtos_menos_vendidos)
                print("\n")
                
    def media_avaliacao(self):
        for nome in self.df.listar_arquivos():
            if nome.startswith('loja_'):
                df_loja = self.df.pegar_dataframe(nome)
                media_avaliacao = df_loja["Avaliação da compra"].mean()
                print(f"Média de avaliação da {nome.replace('_', ' ')}: {media_avaliacao:.2f}")
                
    def media_frete(self):
        for nome in self.df.listar_arquivos():
            if nome.startswith('loja_'):
                df_loja = self.df.pegar_dataframe(nome)
                media_frete = df_loja["Frete"].mean()
                print(f"Média de frete da {nome.replace('_', ' ')}: R$ {media_frete:.2f}")