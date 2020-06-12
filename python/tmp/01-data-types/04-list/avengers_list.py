def avengers():
    avengers = ['Iron Man', 'Captain America', 'Black Widow',
                'The Hulk', 'Hawkeye', 'Thor', 'Falcon']
    print(avengers)

    print('\nAppend example:')
    avengers.append('Black Panther')
    for x in avengers:
        print(x)

    print('\nPop example:')
    avengers.pop()
    for x in avengers:
        print(x)

    print('\nRemove exampe: ')
    avengers.remove('Captain America')
    for x in avengers:
        print(x)

    print("\nInsert example: ")
    avengers.insert(0, 'Spider Man')
    for x in avengers:
        print(x)

    print("\nCount Example: How Manny Spider Men are there?")
    how_many_spider_mans = avengers.count('Spider Man')
    print(how_many_spider_mans)

    print("\nAppend Nested List Example: ")
    gotg = ['Star Lord', 'Rocket', 'Groot', 'Drax', 'Gamora']
    avengers.append(gotg)
    for x in avengers:
        print(x)

    print('\nClear example:')
    avengers.clear()
    print(avengers)


if __name__ == "__main__":
    print('LISTAS EXPLICADAS CON LOS AVENGERS.\n')

    avengers()
