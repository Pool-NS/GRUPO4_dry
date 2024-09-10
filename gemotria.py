class Geometria:
    def area(self, figura, *args):
        if figura == 'cuadrado':
            return args[0] * args[0]
        elif figura == 'rectangulo':
            return args[0] * args[1]
        else:
            raise ValueError("Figura no reconocida")

    def perimetro(self, figura, *args):
        if figura == 'cuadrado':
            return 4 * args[0]
        elif figura == 'rectangulo':
            return 2 * (args[0] + args[1])
        else:
            raise ValueError("Figura no reconocida")

if __name__ == '__main__':
    geom = Geometria()

    figura = input("Ingrese la figura (cuadrado/rectangulo): ").strip().lower()
    if figura == 'cuadrado':
        lado = float(input("Ingrese el lado del cuadrado: "))
        print("El Área del cuadrado es:", geom.area(figura, lado))
        print("El Perímetro del cuadrado es:", geom.perimetro(figura, lado))
    elif figura == 'rectangulo':
        ancho = float(input("Ingrese el ancho del rectángulo: "))
        alto = float(input("Ingrese el alto del rectángulo: "))
        print("El Área del rectángulo es:", geom.area(figura, ancho, alto))
        print("El Perímetro del rectángulo es:", geom.perimetro(figura, ancho, alto))
    else:
        print("Figura no reconocida.")
