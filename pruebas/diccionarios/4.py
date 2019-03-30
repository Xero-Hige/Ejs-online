# def cadenas_mas_largas(cadena):

class TestStringMethods(unittest.TestCase):

    def test_cadena_vacia_devuelve_diccionario_vacio(self):
        self.assertDictEqual(cadenas_mas_largas(""), {})

    def test_cadena_mas_larga_con_caracter_en_dos_cadenas(self):
        self.assertDictEqual(cadenas_mas_largas("Mar azul"),{ 'm': 'mar', 'a': 'azul', 'r': 'mar', 'z': 'azul', 'u': 'azul', 'l': 'azul' })

if __name__ == '__main__':
    unittest.main()