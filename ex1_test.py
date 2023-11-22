import unittest
from ex1 import calculaTaxaDesconto

class TestTaxa(unittest.TestCase):
    # testando classes de equivalencia
    def test_cte1(self):
        taxa = calculaTaxaDesconto(True,"prata",150)
        self.assertEqual(taxa,10)
    
    def test_cte2(self):
        taxa = calculaTaxaDesconto(False,"bronze",300)
        self.assertEqual(taxa,5)
    
    def test_cte3(self):
        taxa = calculaTaxaDesconto(False,"ouro",400)
        self.assertEqual(taxa,15)

    def test_cte4(self):
        taxa = calculaTaxaDesconto(False,"prata",-50)
        self.assertEqual(taxa,0)
    
    def test_cte5(self):
        taxa = calculaTaxaDesconto(True,"platina",100)
        self.assertEqual(taxa,0)
    
    def test_cte6(self):
        taxa = calculaTaxaDesconto(False,"bronze",300)
        self.assertEqual(taxa,10)

    def test_cte7(self):
        taxa = calculaTaxaDesconto(False,"prata",450)
        self.assertEqual(taxa,10)
    
    def test_cte8(self):
        taxa = calculaTaxaDesconto(False,"ouro",600)
        self.assertEqual(taxa,15)

    #testando valores limite

    def test_ctvl1(self):
        taxa = calculaTaxaDesconto(False,"bronze",0.01)
        self.assertEqual(taxa,5)
    
    def test_ctvl2(self):
        taxa = calculaTaxaDesconto(False,"prata",200)
        self.assertEqual(taxa,5)

    def test_ctvl3(self):
        taxa = calculaTaxaDesconto(False,"ouro",500)
        self.assertEqual(taxa,15)

    def test_ctvl4(self):
        taxa = calculaTaxaDesconto(False,"bronze",501)
        self.assertEqual(taxa,15)

    def test_ctvl5(self):
        taxa = calculaTaxaDesconto(False,"prata",-50)
        self.assertEqual(taxa,0)

    def test_ctvl6(self):
        taxa = calculaTaxaDesconto(False,"ouro",0)
        self.assertEqual(taxa,15)

if __name__ == '__main__':
    unittest.main()