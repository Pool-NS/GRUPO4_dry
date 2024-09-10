import unittest
from geometria import Geometria  # Asegúrate de que el archivo de código esté en geometria.py

class TestGeometria(unittest.TestCase):
    def setUp(self):
        self.geom = Geometria()

    def test_area_cuadrado(self):
        self.assertEqual(self.geom.area('cuadrado', 4), 16)

    def test_area_rectangulo(self):
        self.assertEqual(self.geom.area('rectangulo', 5, 10), 50)

    def test_perimetro_cuadrado(self):
        self.assertEqual(self.geom.perimetro('cuadrado', 4), 16)

    def test_perimetro_rectangulo(self):
        self.assertEqual(self.geom.perimetro('rectangulo', 5, 10), 30)

    def test_area_invalid(self):
        with self.assertRaises(ValueError):
            self.geom.area('triangulo', 5, 10)

    def test_perimetro_invalid(self):
        with self.assertRaises(ValueError):
            self.geom.perimetro('circulo', 5)

if __name__ == '__main__':
    unittest.main()
