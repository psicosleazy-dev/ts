import unittest
from atleta import classificaAtleta

class TestAtleta(unittest.TestCase):
    def test_classifica_atleta_menor(self):
        classe = classificaAtleta(15)
        self.assertEqual('menor', classe)
    
    def test_classifica_atleta_juvenil(self):
        classe = classificaAtleta(18)
        self.assertEqual('juvenil', classe)
    
    def test_classifica_atleta_juvenil(self):
        classe = classificaAtleta(22)
        self.assertEqual('adulto', classe)
    
    def test_classifica_atleta_master(self):
        classe = classificaAtleta(40)
        self.assertEqual('masters', classe)
