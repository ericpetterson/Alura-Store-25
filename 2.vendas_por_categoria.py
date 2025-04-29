from gerenciadorCSV import GerenciadorCSV

df = GerenciadorCSV()

# Quantidade de vendas por categoria
for nome in df.listar_arquivos():
    if nome.startswith('loja_'):
        df_loja = df.pegar_dataframe(nome)
        vendas_por_categoria = df_loja["Categoria do Produto"].value_counts()
        print(f"Quantidade de vendas por categoria da {nome.replace('_', ' ')}:")
        print(vendas_por_categoria)
        print("\n")