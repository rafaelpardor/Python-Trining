def list1():
    print('--- Lists 1 ---')

    L = ["spam", 123, 3.14, True]
    print(L)

    print(len(L), L[0], L[3], type(L[3]))
    print(L + [4, 5, 6])
    print(L * 2)


def list2():
    print('\n--- Lists 2 ---')

    L = ["spam", 123]
    L + [4, 5, 6]
    L.append('True')
    print(L)

    L.pop(0)
    print(L)


def list3():
    print('\n--- Lists 3 ---')

    L = [1, 5, 3, 6, 87, 5, 4, 6]
    print(L)

    L.sort()
    print(L)


def list4():
    print('\nList 4')

    list_range1 = list(range(4))
    print(list_range1)

    list_range2 = list(range(0, 7, 2))
    print(list_range2)

    list_range2 = list(range(-6, 7, 2))
    print(list_range2)


def list5():
    print('\nList 5')

    bicycles = ['trek', 'cannondale', 'redline', 'specialized']

    for bicycle in bicycles:
        print(bicycle.title())


if __name__ == "__main__":
    list1()
    list2()
    list3()
    list4()
    list5()
