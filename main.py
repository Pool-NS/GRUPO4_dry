class Geometria:
    def area_cuadrado(self, lado):
        return self._area(lado, lado)

    def area_rectangulo(self, ancho, alto):
        return self._area(ancho, alto)

    def perimetro_cuadrado(self, lado):
        return self._perimetro(lado, lado)

    def perimetro_rectangulo(self, ancho, alto):
        return self._perimetro(ancho, alto)

    def _area(self, dimension1, dimension2):
        return dimension1 * dimension2

    def _perimetro(self, dimension1, dimension2):
        return 2 * (dimension1 + dimension2)
