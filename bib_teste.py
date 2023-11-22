import unittest
from biblioteca_funcoes import calcular_multa_em_atraso, busca_catalogo

class TestBiblioteca(unittest.TestCase):
    def test_calcula_multa_em_atraso_com_zero_dias(self):
        multa = calcular_multa_em_atraso(0)
        self.assertEqual(multa, 0)
    def test_calcula_multa_em_atraso_com_um_dia(self):
        multa = calcular_multa_em_atraso(1)
        self.assertEqual(multa, 2)
    def test_calcula_multa_em_atraso_com_cinco_dias(self):
        multa = calcular_multa_em_atraso(5)
        self.assertEqual(multa, 10)

# **** MEUS TESTES *****
# a funcao a seguir valida em um sistema de biblioteca com usuario (login) e senha. so se torna valido se o login for 'lucas' e a senha '1234'
    def test_valida_login(self):
        login = input("\nLogin: ")
        self.assertEqual("lucas",login)

        senha = input("Senha: ")
        self.assertEqual("1234",senha)

# as 2 funcoes a seguir buscam um livro em um dado catalogo
    def test_livro_disponivel(self):
        catalogo = ["Harry Potter e a Pedra Filosofal", "Dom Casmurro", "1984"]
        livro_buscado = "Dom Casmurro"
        resultado = busca_catalogo(livro_buscado, catalogo)
        self.assertEqual(resultado, "Dom Casmurro")
    
    def test_livro_indisponivel(self):
        catalogo = ["Harry Potter e a Pedra Filosofal", "1984"]
        livro_buscado = "Dom Casmurro"
        resultado = busca_catalogo(livro_buscado, catalogo)
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()