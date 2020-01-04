#!/usr/bin/python3

import random

def merge_sort(lista):
	if len(lista) > 1:
		mid = len(lista) // 2
		left = lista[:mid]
		right = lista[mid:]
		print(left, '*'*10, right)

		# Llamada recursiva en cada mitad
		merge_sort(left)
		merge_sort(right)

		# Iteradores para recorrer las dos sublistas
		i = 0
		j = 0

		# Iterador para lista principal
		k = 0

		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				lista[k] = left[i]
				i += 1
			else:
				lista[k] = right[j]
				j += 1

			k += 1

		while i < len(left):
			lista[k] = left[i]
			i += 1
			k += 1

		while j < len(right):
			lista[k] = right[j]
			j += 1
			k += 1

		print(f'izquierda {left}, derecha {right}')
		print(lista)
		print('*'*20)

	return lista

if __name__ == '__main__':
	tamanio_lista = int(input('Escriba el tamanio de la lista: '))

	lista = [random.randint(0, 100) for i in range(tamanio_lista)]
	print(lista)

	sorted_list = merge_sort(lista)
	print(sorted_list)
