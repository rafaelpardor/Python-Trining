class Rectangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height


class Square(Rectangle):

    def __init__(self, lado):
        super().__init__(lado, lado)


if __name__ == "__main__":
    rectangulo = Rectangle(base=3, height=4)
    print(rectangulo.area())

    cuadrado = Square(lado=5)
    print(cuadrado.area())
