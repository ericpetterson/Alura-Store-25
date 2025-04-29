from gerenciadorCSV import GerenciadorCSV

df = GerenciadorCSV()

for nome in df.listar_arquivos():
    if nome.startswith('loja_'):
        df_loja = df.pegar_dataframe(nome)
        media = df_loja["Avaliação da compra"].mean()
        print(f"A media de avaliação da {nome.replace('_', ' ')} é:  {media:.2f}")