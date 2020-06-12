def strings1():
    """
    Strings types, binary and unicodes
    """

    S = ''  # Empty string
    print(S)

    S = "spam's"  # Double quotes, same as single
    print(S)

    S = 's\np\ta\x00m'  # Escape sequence
    print(S)

    S = """...multiline..."""  # Triple quoted block string
    print(S)

    mantra = """The meaning
        of life,
    is pure programming.
    """
    print(mantra)

    S = r'\temp\spam'  # Raw strings (no escapes)
    print(S)

    B = b'sp\xc4m'  # Byte strings
    print(B)

    U = u'sp\u00c4m'  # Unicode strings
    print(U)


def strings2():
    """
    String manipulation.
    """

    S1 = 'Hello'
    S2 = 'World'
    print(S1+' '+S2)  # String concatenation

    print(S1*3)  # String multiplication

    print(S1[0])  # String index

    print(S2[1::])  # String slicing

    print(len(S2))

    myjob = 'hacker'
    for c in myjob:
        print(c, end=' ')
    print('')


def strings3():
    """
    Formating
    """

    kind = 'kind'

    print("a %s of parrot" % kind)
    print("a {} of parrot".format(kind))
    print("a {0} of parrot".format(kind))


def strings4():
    """
    Strings methods
    """

    name = 'rafael'

    print(name.title())
    print(name.upper())
    print(name.startswith('r'))
    print(name.startswith('R'))
    print(name.endswith('l'))
    print(name.endswith('z'))


if __name__ == "__main__":
    strings1()
    strings2()
    strings3()
    strings4()
