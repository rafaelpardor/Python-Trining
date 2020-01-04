#!/usr/bin/python3

import random 

def bubble_sort(lista):
	n = len(lista)

	for i in range(n):
		for j in range(0, n - i - 1):
			if lista[j] > lista[j + 1]:
				lista[j], lista[j + 1] = lista[j + 1], lista[j]

	return lista

if __name__ == '__main__':
	tamano_lista = int(input('De que tamano es la lista? '))

	lista = [random.randint(0, 100) for i in range(tamano_lista)]
	print(lista)

	order_list = bubble_sort(lista)
	print(order_list)
