# def norma(x, y, z):

class TestTarea1(unittest.TestCase):

    def test_norma(self):
        self.assertAlmostEqual(norma(3,2,-4),  5.385164807134504)


if __name__ == '__main__':
    unittest.main()