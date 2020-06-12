#!/usr/bin/python3

def strings1():
    print('--- Strings 1 ---')

    first_name = 'Rafael'
    last_name = 'Pardo Rodirugez'
    full_name = first_name + ' ' + last_name

    print(first_name, '\n', first_name * 8,
          '\n', last_name,
          '\nFull Name:', full_name,
          '\nLenght de la variable:', len(full_name),
          '\n', type(full_name))
    print(full_name[0], full_name[13],
          full_name[-1], full_name[len(full_name)-1])
    print(full_name[1:], '\n', full_name[0:12])


def strings2():
    print('\n--- Strings 2 ---')

    s = 'hola'
    r = 'l'
    print(s, r)

    r = 'l' + s[1:]
    print(s, r)

    palabra = 'Esternocleidomastoideo.'
    print(palabra)
    print(palabra[::-1])


def strings3():
    print('\n--- Strings 3 ---')

    S = 'Wello'
    print(S)
    L = list(S)
    L[0] = 'H'
    S = ''.join(L)
    print(S)


if __name__ == "__main__":
    strings1()
    strings2()
    strings3()
    print('Se puede cambiar un STRING a un INT, solo si es number:', int('12'))
