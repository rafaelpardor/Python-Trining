
# For loop.

print('')
print('Usamos for para crear una iteración, de números por ejemplo.')
for i in range(10):
    print (i)
# ----------------------------------------------------

print('')
print('Podemos usar el ciclo "for" para imprimir cada letra de una palabra.')
r = 'ferrocarril'
print(r ,"\n||")

for letter in r:
    print(letter)
# ----------------------------------------------------

print('')
for a in range(10):
    print (a,'HOLA')
# ----------------------------------------------------

print('')
for i in range(30):
    if i % 3 == 0:
        print(i)
    elif i == 26:
        break
# ----------------------------------------------------

print('')
for i in range (30):
    if i % 3 == 0:
        print(i,i**2)
    elif i == 22:
        break
# ----------------------------------------------------

print('')
for i in range (30):
    if i % 3 != 0:
        continue
    else:
        print(i, i**2)
# ----------------------------------------------------

print('')
print(range(5))
print(list(range(10)))
# ----------------------------------------------------

print('')
if __name__ == '__main__':
    print('Enter a number: ')
    n = int(input())
    [print(i**2) for i in range(n)]