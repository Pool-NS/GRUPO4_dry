import unittest
from geometria import Geometria  # Asegúrate de que el archivo de la clase se llame geometria.py o ajusta la importación.

class TestGeometria(unittest.TestCase):
    def setUp(self):
        self.geo = Geometria()

    def test_area_cuadrado(self):
        self.assertEqual(self.geo.area_cuadrado(4), 16)
        self.assertEqual(self.geo.area_cuadrado(5), 25)

    def test_area_rectangulo(self):
        self.assertEqual(self.geo.area_rectangulo(4, 5), 20)
        self.assertEqual(self.geo.area_rectangulo(7, 3), 21)

    def test_perimetro_cuadrado(self):
        self.assertEqual(self.geo.perimetro_cuadrado(4), 16)
        self.assertEqual(self.geo.perimetro_cuadrado(5), 20)

    def test_perimetro_rectangulo(self):
        self.assertEqual(self.geo.perimetro_rectangulo(4, 5), 18)
        self.assertEqual(self.geo.perimetro_rectangulo(7, 3), 20)

if __name__ == '__main__':
    unittest.main()
