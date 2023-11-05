def calcular_multa_em_atraso(dias_em_atraso):
   if dias_em_atraso <= 0:
      return 0
   # Suponhamos que a multa seja R$ 2 por dia de atraso.
   multa = 2 * dias_em_atraso
   return multa