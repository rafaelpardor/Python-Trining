#!/usr/bin/python3

import random

def insertion_sort(lista):
	for index in range (1, len(lista)):
		actual_value = lista[index]
		actual_position = index

		while actual_position > 0 and lista[actual_position - 1] > actual_value:
			lista[actual_position] = lista[actual_position - 1]
			actual_position -= 1

		lista[actual_position] = actual_value

	return lista

if __name__ == '__main__':
	tamano_lista = int(input('De que tamano es la lista? '))

	lista = [random.randint(0, 100) for i in range(tamano_lista)]
	print(lista)

	order_list = insertion_sort(lista)
	print(order_list)
