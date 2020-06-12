
# Functions with parameters.

def show_name(name):
    print('Hi '+ name)
    print('Hola ', name)
    print('Hello {}'.format(name))
# -------------------------------------

def add(x, y):
    print(x + y)
# -------------------------------------

def excercise(a, b):
    print('You enter {} and {}.'.format(a,b))
    print('Suma: {}\nResta:{}\nMultiplicación: {}'.format(a+b,a-b,a*b))
# -------------------------------------

if __name__ == '__main__':
    print('')
    show_name('Alice')
    show_name('Rafael')

    print('')
    add(1,2)
    add(32,532)
    add(645,265345)

    print('')
    print("""
    -----------Exercise-----------
    Read two integers from STDIN and print three lines where:

    1. The first line contains the sum of the two numbers.
    2. The second line contains the difference of the two numbers (first - second).
    3. The third line contains the product of the two numbers.
    """)
    print('Enter 2 numbers: ')
    a = int(input())
    b = int(input())
    excercise(a,b)

