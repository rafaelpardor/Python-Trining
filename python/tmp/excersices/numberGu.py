
import random

def run():
    #Se crea una variable de booleano False
    number_found = False
    #Se crea una var. int random 
    number1 = int(input('Introduzca el numero inicial: '))
    number2 = int(input('Introduzca el numero final: '))

    random_number = random.randint(number1, number2)

    #Se crea un while not y llamamos a la var. random, mientras el numero no se encuentra el loop se reinicia cuantas veces quiera
    while not number_found:
        #Declaramos una variable que pueda ser introducida por el usuario
        number = int(input('Intenta un numero: '))

        #Se inicia una condicional diciendo que, si el numero introducido por el usuario es igual al numero random
        if number == random_number:
            print('Makia, encontro en numero chino.')
            #Cuando se encuentra el numero se reasigna la variable y se cambia a True
            number_found = True
        elif number > random_number:
            print('El numero es mas pequeño.')
        else:
            print('Te pasaste we')

#Primero el compilador lee todo el codigo y en este momento se llama a la funcion run()
if __name__ == '__main__':
    run()
