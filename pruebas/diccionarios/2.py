# def contador_palabras(cadena):

class TestStringMethods(unittest.TestCase):

    def test_cadena_vacia_devuelve_diccionario_vacio(self):
        self.assertDictEqual(contador_palabras(""), {})

    def test_cadena_contadores_correctos(self):
        self.assertDictEqual(contador_palabras("Qué lindo día que hace hoy"), { 'Qué': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1})

if __name__ == '__main__':
    unittest.main()