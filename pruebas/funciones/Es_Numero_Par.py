# def es_numero_par(n):

class TestStringMethods(unittest.TestCase):

    def test_numero_par(self):
        msg = "2 es un número par"
        self.assertTrue(es_numero_par(2), msg)

    def test_numero_par(self):
        msg = "5 es un número impar"
        self.assertFalse(es_numero_par(5), msg)


if __name__ == '__main__':
    unittest.main()