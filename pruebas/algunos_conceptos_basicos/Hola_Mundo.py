# def sumar_numeros_recibidos():

from unittest.mock import patch

class PedirNumeroYSumarTestCase(unittest.TestCase):

    def test_suma_correcta(self):
        user_input = ["4", "2"]
        with patch('builtins.input', side_effect = user_input):
            numero = sumar_numeros_recibidos()
        self.assertEqual(numero, 6)

    def test_pasan_valor_no_numerico_primero(self):
        user_input = ["cinco", "5", "2"]
        with patch('builtins.input', side_effect = user_input):
            numero = sumar_numeros_recibidos()
        self.assertEqual(numero, 7)

    def test_pasan_valor_no_numerico_segundo(self):
        user_input = ["5", "dos", "2"]
        with patch('builtins.input', side_effect = user_input):
            numero = sumar_numeros_recibidos()
        self.assertEqual(numero, 7)


if __name__ == '__main__':
    unittest.main()