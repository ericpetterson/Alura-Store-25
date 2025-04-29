from gerenciadorCSV import GerenciadorCSV

df = GerenciadorCSV()

for nome in df.listar_arquivos():
    if nome.startswith('loja_'):
        df_loja = df.pegar_dataframe(nome)
        faturamento = df_loja["Preço"].sum()
        print(f"Total de faturamento da {nome.replace('_', ' ')}: R$ {faturamento:.2f}")
