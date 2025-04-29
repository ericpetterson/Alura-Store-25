from gerenciadorCSV import GerenciadorCSV

df = GerenciadorCSV()

# Quantidade de produtos mais e menos vendidos por loja
for nome in df.listar_arquivos():
    if nome.startswith('loja_'):
        df_loja = df.pegar_dataframe(nome)
        produtos_mais_vendidos = df_loja["Produto"].value_counts().head(5)
        produtos_menos_vendidos = df_loja["Produto"].value_counts().tail(5)
        
        print(f"Produtos mais vendidos da {nome.replace('_', ' ')}:")
        print(produtos_mais_vendidos)
        print("\n")
        
        print(f"Produtos menos vendidos da {nome.replace('_', ' ')}:")
        print(produtos_menos_vendidos)
        print("\n")