import unittest
from biblioteca_funcoes import calcular_multa_em_atraso

class TestBiblioteca(unittest.TestCase):

# meus testes
    def test_valida_login(self):
        login = input("Login: ")
        self.assertEqual("lucas",login)

        senha = input("Senha: ")
        self.assertEqual("1234",senha)

if __name__ == '__main__':
    unittest.main()