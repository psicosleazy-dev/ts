class Horario:
    def __init__(self, horas, minutos):
        self.horas = horas
        self.minutos = minutos

def calcula_preco_chamada(horario_inicio, horario_fim):
    # Definindo os valores e limites das faixas
    valor_faixa_1 = 0.40
    valor_faixa_2 = 0.20
    limite_faixa_1_inicio = Horario(8, 0)
    limite_faixa_1_fim = Horario(18, 0)

    # Convertendo Horario para minutos
    horario_inicio_min = horario_inicio.horas * 60 + horario_inicio.minutos
    horario_fim_min = horario_fim.horas * 60 + horario_fim.minutos
    limite_faixa_1_inicio_min = limite_faixa_1_inicio.horas * 60 + limite_faixa_1_inicio.minutos
    limite_faixa_1_fim_min = limite_faixa_1_fim.horas * 60 + limite_faixa_1_fim.minutos

    # Verificando se os horários estão dentro da mesma faixa
    mesma_faixa = (
        (horario_inicio_min >= limite_faixa_1_inicio_min and horario_fim_min <= limite_faixa_1_fim_min) or
        (horario_inicio_min >= limite_faixa_1_inicio_min and horario_fim_min >= limite_faixa_1_fim_min) or
        (horario_inicio_min <= limite_faixa_1_inicio_min and horario_fim_min <= limite_faixa_1_fim_min)
    )

    # Calculando o valor da chamada
    if mesma_faixa:
        minutos_faixa_1 = max(0, min(horario_fim_min, limite_faixa_1_fim_min) - max(horario_inicio_min, limite_faixa_1_inicio_min))
        minutos_faixa_2 = 0
    else:
        minutos_faixa_1 = max(0, limite_faixa_1_fim_min - max(horario_inicio_min, limite_faixa_1_inicio_min))
        minutos_faixa_2 = max(0, min(horario_fim_min, 24 * 60) - limite_faixa_1_fim_min)

    valor = minutos_faixa_1 * valor_faixa_1 + minutos_faixa_2 * valor_faixa_2
    return valor

# Exemplo de uso
horario_inicio = Horario(18, 30)
horario_fim = Horario(19, 40)
preco = calcula_preco_chamada(horario_inicio, horario_fim)
print(f'O preço da chamada é R$ {preco:.2f}')