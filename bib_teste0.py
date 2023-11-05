import unittest
from biblioteca_funcoes import calcular_multa_em_atraso
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
if __name__ == '__main__':
 unittest.main()