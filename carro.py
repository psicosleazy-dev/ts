class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O {self.marca} {self.modelo} está ligado.")
        else:
            print(f"O {self.marca} {self.modelo} já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"O {self.marca} {self.modelo} está desligado.")
        else:
            print(f"O {self.marca} {self.modelo} já está desligado.")

    def acelerar(self):
        if self.ligado:
            print(f"O {self.marca} {self.modelo} está acelerando.")
        else:
            print(f"Você precisa ligar o {self.marca} {self.modelo} primeiro.")

# Criando uma instância da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2023)

# Interagindo com a instância
# meu_carro.ligar()
meu_carro.acelerar()
meu_carro.desligar()
print()

def adicionar_carro_ao_catalogo(catalogo, carro):
    catalogo.append(carro)

# Inicialize um catálogo vazio
catalogo_de_carros = []

# Crie instâncias de carros
carro1 = Carro("Toyota", "Corolla", 2023)
carro2 = Carro("Ford", "Focus", 2022)

# Adicione carros ao catálogo
adicionar_carro_ao_catalogo(catalogo_de_carros, carro1)
adicionar_carro_ao_catalogo(catalogo_de_carros, carro2)

# Agora, o catálogo_de_carros contém as instâncias dos carros
print("Catálogo de Carros:")
for carro in catalogo_de_carros:
    print(f"{carro.marca} {carro.modelo} ({carro.ano})")