def list_comprenhesion1():
    print('List Comprenhension 1')

    N = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
    print(N)

    col1 = [row[1] for row in N]
    print(col1)

    col2 = [row[1]+1 for row in N]
    print(col2)

    col3 = [row[1] for row in N if row[1] % 2 == 0]
    print(col3)

    diag = [N[i][i] for i in [0, 1, 2]]
    print(diag)

    double = [c * 2 for c in "smap"]
    print(double)

    G = (sum(row)for row in N)
    print(next(G), next(G), next(G))

    H = list(map(sum, N))
    print(H)


def list_compremhesion2():
    print('\nList Comprenhension 2')

    list_comp1 = [[x ** 2, x ** 3] for x in range(4)]
    print(list_comp1)

    list_comp2 = [[x, x/2, x*2]for x in range(-6, 7, 2) if x > 0]
    print(list_comp2)


def list_compremhesion3():
    print('\nList Comprenhension 3')

    N = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

    D = {sum(row) for row in N}
    print(D, type(D))

    F = {i: sum(N[i])for i in range(3)}
    print(F, type(F))


def list_compremhesion4():
    print('\nList Comprenhension 4')

    list_comp = [ord(x)for x in "spaam"]
    print(list_comp, type(list_comp))

    set_comp = {ord(x) for x in "spaam"}
    print(set_comp, type(set_comp))

    dict_comp = {x: ord(x) for x in "spaam"}
    print(dict_comp, type(dict_comp))

    generator_comp = (ord(x) for x in "spaam")
    print(generator_comp, type(generator_comp))


if __name__ == "__main__":
    list_comprenhesion1()
    list_compremhesion2()
    list_compremhesion3()
    list_compremhesion4()
