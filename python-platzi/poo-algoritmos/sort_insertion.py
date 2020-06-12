#!/usr/bin/python3

import random

def insertion_sort(num_list):
	for index in range (1, len(num_list)):
		actual_value = num_list[index]
		actual_position = index

		while actual_position > 0 and num_list[actual_position - 1] > actual_value:
			num_list[actual_position] = num_list[actual_position - 1]
			actual_position -= 1

		num_list[actual_position] = actual_value

	return num_list

if __name__ == '__main__':
	tamano_lista = int(input('De que tamano es la lista? '))

	lista = [random.randint(0, 100) for i in range(tamano_lista)]
	print(lista)

	order_list = insertion_sort(lista)
	print(order_list)
