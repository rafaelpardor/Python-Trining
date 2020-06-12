
# While loop.

def first_while(a,b):
    while a <= b:
        print(a)
        a += 1
# -------------------------------------

def brak_while():    
    b = 0
    for b in range (10):
        while b <= 5:
            print(b)
            break
# -------------------------------------

def annoying_wile():
    name = ''
    while name != 'your name':
        print('Plase type your name: ')
        name = input()
    print('Thx')

if __name__ == '__main__':
    print('')
    first_while(1,30)
    print('')
    brak_while()
    print('')
    annoying_wile()