class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def retirar_livro(self):
        if not self.disponivel:
            print(f"\nO livro {self.titulo} não está disponível")
        else:
            print(f"\nLivro {self.titulo} retirado com sucesso")
            self.disponivel = False

catalogo = []
livro1 = Livro("Harry Potter e a Pedra Filosofal","J.K. Rowling", 1997)
livro2 = Livro("1984","George Orwell", 1949)
livro3 = Livro("Dom Casmurro", "Machado de Assis", 1899)

def adiciona_catalogo(catalogo,livro):
    catalogo.append(livro)

def procura_livro(catalogo, livro_proc):
    for livro in catalogo:
        if livro.titulo == livro_proc.titulo and livro.autor == livro_proc.autor and livro.ano == livro_proc.ano:
            livro.disponivel = False
    return None


def remove_catalogo(catalogo,livro_proc):
    for livro in catalogo:
        if livro.titulo == livro_proc == livro_proc.titulo and livro.autor == livro_proc.autor and livro.ano == livro_proc.ano:
            return livro

adiciona_catalogo(catalogo,livro1)
adiciona_catalogo(catalogo,livro2)
adiciona_catalogo(catalogo,livro3)

print("Catálogo da Biblioteca: ")
for livro in catalogo:
    if livro.disponivel:
        print(f"{livro.titulo} {livro.autor} ({livro.ano})")

'''def ligar(self):
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
            print(f"Você precisa ligar o {self.marca} {self.modelo} primeiro.")'''
    