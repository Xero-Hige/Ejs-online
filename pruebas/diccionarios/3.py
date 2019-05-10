# def contar_caracteres(cadena):

class TestStringMethods(unittest.TestCase):

    def test_cadena_vacia_devuelve_diccionario_vacio(self):
        self.assertDictEqual(contar_caracteres(""), {})

    def test_cadena_contadores_correctos(self):
        self.assertDictEqual(contar_caracteres("Hola mama"), { 'h': 1, 'o': 1, 'l': 1, 'a': 3, 'm': 2})

if __name__ == '__main__':
    unittest.main()