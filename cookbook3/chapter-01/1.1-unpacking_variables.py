#!/usr/bin/python3

# You have an N-element tuple or sequence that you would like to unpack into collection of N varialbes
print("""
Any sequence can be unpacked into variables using assigment operation.
The only req. is that the number of variables and structure match the sequence.
        """)
p = (4, 5)
x, y = p

print("var x: {}".format(x))
print("var y: {}".format(y))


# When unpacking, yoou may sometins want to discard certain values.
# Python has no speacial syntax for this.
data = ['ACME','Nuclear bomb', 50, 91.1, (2012,12,21)]
name, product, *_, (*_, day) = data

print("Data values: {}".format(data))
print("Name: ",name,"\nProduct: ", product, "\nDay: ", day)

print("""
        Unpacking works with any object that hapens to be iterable,
        not just tuples or list.
        Includes strings, iterators and generators
        """)

