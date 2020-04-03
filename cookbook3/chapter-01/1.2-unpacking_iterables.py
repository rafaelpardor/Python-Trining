#!/usr/bin/python3

# We need to unpacl N elements from an iterable, but the iterable has to many values
print("""
Python 'star expressions' can be used to recollect too many values to unpack.
Does not mather the length.
    """)

record = ('Rafael', 'rafael@example.com','312312312','31321312312', 21)
name, email, *phone_numbers, age= record

# The phone_numbers variable will always be a list, regardless of how many phone numbers are unpacked
print("record:", record)
print("phone number:", phone_numbers,"\n")

print("""
        Extended iterable unpacking is tailor-made for unpacking iterables of unknown or arbitrary length,
        Star unpacking lets the developer leverage those patterns easily instead of performing acrobatics
        to get at the relevant elements in the iterable.
        """)

foo_bar = [
        ('foo', 1, 2),
        ('bar', 'hello'),
        ('foo', 3, 4),
    ]

print(foo_bar)

def do_foo(x, y):
    print('this is foo ->', x, y)

def do_bar(s):
    print('this is bar ->', s)

for tag, *args in foo_bar:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

items = [1,2,3,4,5,6]
head, *tail = items
print("\n", head)
print(tail)

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum(items))

