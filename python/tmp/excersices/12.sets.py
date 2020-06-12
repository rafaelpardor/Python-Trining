
# NO PERMITEN ELEMENTOS REPETIDOS
a = set ([1,2,3,4,5]) 
b = set ([4,5,6,7,8,9])
print(a)
print(b)

print('Union between a and then b',a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))
print(type('a'))