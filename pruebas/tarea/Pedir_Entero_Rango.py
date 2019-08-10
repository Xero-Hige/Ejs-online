# def pedir_entero(mensaje, min, max):

from unittest.mock import patch

class PedirEnteroEnRangoTestCase(unittest.TestCase):

    def test_ingresa_numeros_correcto_primero(self):
        user_input = ["4"]
        with patch('builtins.input', side_effect = user_input):
            numero = pedir_entero("Hola",3,7)
        self.assertEqual(numero, 4)

    def test_ingresa_numeros_fuera_de_rango_antes_del_correcto(self):
        user_input = ["0", "34", "-2", "4" ]
        with patch('builtins.input', side_effect = user_input):
            numero = pedir_entero("Hola",3,7)
        self.assertEqual(numero, 4)
    
    def test_ingresa_cadenas_antes_del_numero_correcto(self):
        user_input = ["hola", "madre", "4" ]
        with patch('builtins.input', side_effect = user_input):
            numero = pedir_entero("Hola",3,7)
        self.assertEqual(numero, 4)

    def test_ingresa_rango_negativo(self):
        user_input = ["-10", "-5", "-4" ]
        with patch('builtins.input', side_effect = user_input):
            numero = pedir_entero("Hola",-7,-3)
        self.assertEqual(numero, -5)

    def test_ingresa_input_vacio(self):
        user_input = ["", "7" ]
        with patch('builtins.input', side_effect = user_input):
            numero = pedir_entero("Hola",3,8)
        self.assertEqual(numero, 7)


if __name__ == '__main__':
    unittest.main()