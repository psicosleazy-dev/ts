class Atleta:
    def __init__(self, nome, modalidade, idade, categoria):
        self.nome = nome
        self.modalidade = modalidade
        self.idade = idade
        self.categoria = categoria

    def classificaAtleta(idade):
        if idade == 15 or idade == 16 or idade == 17:
            return 'menor'
        elif idade == 18 or idade == 19:
            return 'juvenil'
        elif idade >= 20 and idade <= 34:
            return 'adulto'
        elif idade >= 35:
            return 'masters'
        else:
            return 'invalido'
