

import turtle as turtle

def main ():
    window = turtle.Screen()
    rafa = turtle.Turtle()
    make_square(rafa)
    turtle.mainloop()

def make_square(rafa):
    # length = int(input('tamano de cuadrado: '))
    for i in range(200):
        makeLineAndTurn(rafa, length)


def makeLineAndTurn(rafa, length):
    rafa.forward(150)
    rafa.left(430)
    rafa.speed(600)

if __name__=='__main__':
    main()


