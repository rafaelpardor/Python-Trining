print("""
Any sequence can be unpacked into variables using assigment operation.
        """)
p = (4, 5)
x, y = p

print('X: ',x)
print('Y: ', y)


data = ['ACME','Nuclear bomb', 50, 91.1, (2012,12,21)]
name, product, ammount, _, date = data

print("Data: ", data)
print(name, product)

print("""
        Unpacking works with any object that hapens to be iterable,
        not just tuples or list.
        Includes strings, iterators and generators
        """)

