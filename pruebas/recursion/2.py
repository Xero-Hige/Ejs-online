# def es_potencia_de(a,b):

import unittest

class TestStringMethods(unittest.TestCase):

    def test_25_es_potencia_de_5(self):
        msg = "25 es potencia de 5"
        self.assertTrue(es_potencia_de(25,5), msg)

    # def test_potencia_y_base_negativa(self):
    #     msg = "-8 es potencia de -2"
    #     self.assertTrue(es_potencia_de(-8,-2), msg)


if __name__ == '__main__':
    unittest.main()
