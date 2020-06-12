

def run():
    number = int(input('Escribe un nummero: '))
    result = isPrime(number)

    if result is True:
        print('Es primo')
    else:
        print('No es primo')

def isPrime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        False
    else:
        for i in range(3,number):
            if number % i == 0:
                return False

    return True

if __name__ == '__main__':
    run()