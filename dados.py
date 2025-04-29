from gerenciadorCSV import GerenciadorCSV

df = GerenciadorCSV()

df_loja_1 = df.pegar_dataframe('loja_1')
df_loja_2 = df.pegar_dataframe('loja_2')
df_loja_3 = df.pegar_dataframe('loja_3')
df_loja_4 = df.pegar_dataframe('loja_4')

def faturamento_total(df_loja):
    return sum(df_loja["Preço"])

total1 = faturamento_total(df_loja_1)
print(f"Total de faturamento da loja 1: R$ {total1}")

total2 = faturamento_total(df_loja_2)
print(f"Total de faturamento da loja 2: R$ {total2}")

total3 = faturamento_total(df_loja_3)
print(f"Total de faturamento da loja 3: R$ {total3}")

total4 = faturamento_total(df_loja_4)
print(f"Total de faturamento da loja 4: R$ {total4}")
