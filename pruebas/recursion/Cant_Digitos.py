# def cantidad_digitos(n):

class TestStringMethods(unittest.TestCase):

    def test_numero_de_un_digito_tiene_largo_1(self):
        msg = "Un número de un dígito tiene largo 1"
        self.assertEqual(cantidad_digitos(5),1, msg)

    def test_numero_de_un_digito_megativo_tiene_largo_1(self):
        msg = "Un número negativo de un dígito tiene largo 1"
        self.assertEqual(cantidad_digitos(5),1, msg)
    
    def test_numero_aleatorio(self):
        msg = "Largo incorrecto para número aleatorio positivo"
        self.assertEqual(cantidad_digitos(5577),4, msg)

    def test_numero_negativo_aleatorio(self):
        msg = "Largo incorrecto para número aleatorio negativo"
        self.assertEqual(cantidad_digitos(-555089),6, msg)

if __name__ == '__main__':
    unittest.main()