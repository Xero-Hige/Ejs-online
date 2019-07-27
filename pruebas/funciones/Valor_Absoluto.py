# def valor_absoluto(n):

class TestStringMethods(unittest.TestCase):

    def test_valor_absoluto_numero_entero_positivo(self):
        msg = "El valor absoluto de 5 es 5"
        self.assertEqual(valor_absoluto(5), 5, msg)

    def test_valor_absoluto_numero_entero_negativo(self):
        msg = "El valor absoluto de -10 es 10"
        self.assertEqual(valor_absoluto(-10), 10, msg)

    def test_valor_absoluto_fraccion_positiva(self):
        msg = "El valor absoluto de 5.4 es 5.4"
        self.assertEqual(valor_absoluto(5.4), 5.4, msg)

    def test_valor_absoluto_numero_entero_negativo(self):
        msg = "El valor absoluto de -12.6 es 12.6"
        self.assertEqual(valor_absoluto(-12.6), 12.6, msg)



if __name__ == '__main__':
    unittest.main()