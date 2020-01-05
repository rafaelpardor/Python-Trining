#!usr/bin/python3

import random

def busqueda_lineal(lista, objetivo):
	match = False
	count = 0

	for element in lista:
		count+=1
		if element == objetivo:
			match = True
			break

	print('Se hacern estos movimientos', count)
	return match

if __name__ == '__main__':
	tamano_lista = int(input('De que tamano es la lista? '))
	objetivo = int(input('Que numero quieres encontrar '))

	lista = [random.randint(0, 100) for i in range(tamano_lista)]

	matched = busqueda_lineal(lista, objetivo)
	print(lista)
	print(f'El elemento {objetivo} {"esta en la lista" if matched else "no esta en la lista"}')
