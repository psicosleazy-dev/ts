import re

def validaID(id):
    # Usando expressões regulares para validar o padrão
    padrao = r'^[a-zA-Z][a-zA-Z0-9]{0,5}$'
    
    if re.match(padrao, id):
        return 'válido'
    else:
        return 'inválido'
    
print(validaID('a'))
print(validaID('1039810830hxsna'))