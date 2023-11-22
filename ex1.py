def calculaTaxaDesconto(primeira_compra, tipo_cliente, valor):
    if not (isinstance(valor, (int, float)) and valor > 0):
        return 0  # Valor inválido
    taxa = 0

    if primeira_compra == True:
        taxa = 10

    if tipo_cliente == 'bronze':
        taxa = max(taxa,5)
    elif tipo_cliente == 'prata':
        taxa = max(taxa,10)
    elif tipo_cliente == 'ouro':
        taxa = max(taxa,15)
    else:
        return 0

    if valor > 500:
        taxa = max(taxa,15)
    elif valor > 400 and valor <= 499:
        taxa = max(taxa,10)
    elif valor > 200 and valor <= 399:
        taxa = max(taxa,5)
            
    return taxa