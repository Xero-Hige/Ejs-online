# def dividir_por_enteros(lista, k):

class TestStringMethods(unittest.TestCase):

    def test_k_mayor_a_todos(self):
        self.assertEqual(dividir_por_enteros([1,3,2],4), ([1,3,2],[],[]))

    def test_lista_vacia(self):
        self.assertEqual(dividir_por_enteros([],5) , ([],[],[]))

    def test_lista_con_valores_mayores_menores_iguales(self):
        self.assertEqual(dividir_por_enteros([9.3,4,7,5],5), ([3,4],[5],[9,7]))

if __name__ == '__main__':
    unittest.main()
