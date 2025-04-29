from gerenciadorCSV import GerenciadorCSV

df = GerenciadorCSV()

for nome in df.listar_arquivos():
    if nome.startswith('loja_'):
        df_loja = df.pegar_dataframe(nome)
        media = df_loja["Frete"].mean()
        print(f"A media do valor do frete da {nome.replace('_', ' ')} é: R$ {media:.2f}")