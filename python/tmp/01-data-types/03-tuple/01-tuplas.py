def tuplas1():
    T = (1, 1, 2, 3, 4)
    print(T)
    print(T[0])
    print(len(T))

    print(T + (5, 6))
    print(T.index(4))
    print(T.count(1))
    print(T)
    print(T.__len__())


if __name__ == "__main__":
    tuplas1()
