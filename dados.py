from gerenciadorCSV import GerenciadorCSV
from analise_dos_dados import AnaliseDados

df = GerenciadorCSV()

analise = AnaliseDados(df)
analise.analise_faturamento()
analise.vendas_por_categoria()
analise.produtos_mais_menos_vendidos()
analise.media_avaliacao()
analise.media_frete()


