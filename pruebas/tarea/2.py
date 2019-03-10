# def diferencia(x1, y1, z1, x2, y2, z2):

import unittest

class TestTarea1(unittest.TestCase):

    def test_diferencia(self):
        self.assertEqual(diferencia(8, 7, -3, 5, 3, 2),  (3, 4, -5))


if __name__ == '__main__':
    unittest.main()