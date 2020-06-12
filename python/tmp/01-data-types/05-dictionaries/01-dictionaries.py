def dictionaries1():
    print('--- Diccionarios 1 ---')

    D1 = {
        'food': 'smap',
        'quantity': 5,
        'color': 'red'
    }
    print(D1)

    print(D1['food'])
    D1['quantity'] += 1
    print(D1)

    D2 = {}
    D2['first_name'] = 'Bob'
    D2['last_name'] = 'Spidha'
    D2['age'] = 20
    print(D2)


def dictionaries2():
    print('\n--- Diccionarios 2 ---')

    bob1 = dict(first_name='Bob', last_name='Markus', age=20)
    print(bob1)

    bob2 = dict(zip(
        ['name', 'job', 'age'],
        ['Bob', 'Python developer', 20]
    ))
    print(bob2)

    rec = {
        'name': {'first_name': 'Rafael', 'last_name': 'Pardo R'},
        'jobs': ['Software Engeneer', 'DevOps', 'CyberPunk'],
        'age': 20
    }
    print(rec)
    print(rec['name'])
    print(rec['jobs'])
    print(rec['jobs'][2])
    rec['jobs'].append('Pizza lover')
    print(rec)


def dictionaries3():
    print('\n--- Diccionarios 3 ---')

    D = {'a': 1, 'b': 2, 'c': 3, 'f': 6}
    print(D)

    D['d'] = 4
    print(D)

    letter1 = 'g'
    if not letter1 in D:
        print('missing ->', letter1)
        print('Nothing around here')

    letter2 = 'az'
    value1 = D.get(letter2, 0)
    print(value1)

    letter3 = 'f'
    value2 = D[letter3] if letter3 in D else 0
    print(value2)


def dictionaries4():
    print('\n--- Diccionarios 4 ---')

    D = {'a': 1, 'b': 2, 'c': 3}
    print(D)

    KD = list(D.keys())
    print(KD)

    for key in KD:
        print(key, '->', D[key])
    print('')
    for key in sorted(D):
        print(key, '=>', D[key])


def dictionaries5():
    print('\n--- Diccionarios 5 ---')

    calificaciones = {
        'Algoritmos': 9,
        'Sociales': 9,
        'Matematicas': 5,
        'Web': 1,
        'Bases de Datos': 4
    }

    for key, value in calificaciones.items():
        print('Materia: {}, Nota: {}'.format(key, value))

    # CALCULAR PROMEDIO
    print('Primedio de notas')
    print('--------------')

    suma_de_calificaciones = 0
    for value in calificaciones.values():
        suma_de_calificaciones += value

    promedio = suma_de_calificaciones/len(calificaciones.values())

    print('Promedio: {}'.format(promedio))


def dictionaries6():
    print('\n--- Diccionarios 6 ---')

    patas = {
        'humanos': 2,
        'pulpo': 8,
        'perro': 4,
        'gato': 4,
        'ciempies': 100
    }
    print(patas)

    print(patas.keys())
    print(patas.values())
    print(patas.items())

    print('perro' in patas)
    print(8 in patas)
    print(len(patas))


def dictionaries7():
    pares = []
    for num in range(1, 31):
        if num % 2 == 0:
            pares.append(num)

    even = [num for num in range(1, 31) if num % 2 == 0]
    print(pares)
    print(even)

    cuadrados = {}
    for num in range(1, 11):
        cuadrados[num] = num ** 2
    print(cuadrados)

    squares = {num: num**2 for num in range(1, 11)}
    print(squares)


if __name__ == "__main__":
    dictionaries1()
    dictionaries2()
    dictionaries3()
    dictionaries4()
    dictionaries5()
    dictionaries6()
    dictionaries7()
