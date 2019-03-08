# def lista_ordenada(lista):

import unittest

class TestStringMethods(unittest.TestCase):

    def test_lista_no_ordenada(self):
        self.assertFalse(lista_ordenada([1,3,2]))

    def test_lista_ordenada(self):
        self.assertTrue(lista_ordenada([1,2,3]))

    def test_lista_vacia_esta_ordenada(self):
        self.assertTrue(lista_ordenada([]))

if __name__ == '__main__':
    unittest.main()