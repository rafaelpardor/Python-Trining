#!/usr/bin/python3

class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height

    def printing(self):
        print('Function from Rectangle')

class Square(Rectangle):
    def __init__(self, lado):
        super().__init__(lado, lado)


if __name__ == "__main__":
    rectangulo = Rectangle(base=3, height=4)
    print("Area de un rectangulo:", rectangulo.area())

    cuadrado = Square(lado=5)
    print("Area de un cuadrado:",cuadrado.area())

    cuadrado.printing()
