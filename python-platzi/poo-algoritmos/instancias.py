class Cordenate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_cordenate):
        x_diff = (self.x + other_cordenate.x)**2
        y_diff = (self.y + other_cordenate.y)**2

        return (x_diff + y_diff)**0.5

if __name__ == '__main__':
    cord_1 = Cordenate(3, 10)
    cord_2 = Cordenate(4, 8)

    #print(cord_1.distance(cord_2))
    print(isinstance(cord_2, Cordenate))
