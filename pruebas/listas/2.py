# def invertir_lista(lista):

class TestListas2(unittest.TestCase):

    def test_lista(self):
        self.assertEqual(invertir_lista([1,3,2]), [2,3,1])

    def test_lista_vacia(self):
        self.assertEqual(invertir_lista([]), [])

if __name__ == '__main__':
    unittest.main()