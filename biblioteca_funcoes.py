def calcular_multa_em_atraso(dias_em_atraso):
   if dias_em_atraso <= 0:
      return 0
   # Suponhamos que a multa seja R$ 2 por dia de atraso.
   multa = 2 * dias_em_atraso
   return multa

def busca_catalogo(livro_buscado, catalogo):
   for livro in catalogo:
      if livro_buscado in livro:
         return livro
   
   if livro is not None:
      print("\nDisponível para retirada!")
   else:
      print("\nLivro não disponível!")