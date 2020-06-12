#!/usr/bin/python3

class Coordenates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_coordenate):
        x_diff = (self.x + other_coordenate.x)**2
        y_diff = (self.y + other_coordenate.y)**2

        return (x_diff + y_diff)**0.5

if __name__ == '__main__':
    coord_1 = Coordenates(3, 10)
    coord_2 = Coordenates(4, 8)

    print(coord_1.distance(coord_2))
    print("Is coord_2 instances of Coordenates?", isinstance(coord_2, Coordenates))
    print("Is 21 instace if Coordenates?", isinstance(32, Coordenates))

