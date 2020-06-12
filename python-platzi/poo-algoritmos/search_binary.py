#!usr/bin/python3

import random

def binary_search(num_list, start, final, objective):
	print(f'Buscando {objective} entre {num_list[start]} y {num_list[final-1]}')
	count = 0

	if start > final:
		return False

	mid = (start + final) // 2
	if num_list[mid]==objective:
		print('Cantidad de movimientos: ', count)
		count+=1
		return True
	elif num_list[mid]< objective:
		return binary_search(num_list, mid+1, final, objective)
	else:
		return binary_search(num_list, start, mid-1, objective)


if __name__ == '__main__':
	len_list = int(input('De que tamano es la lista? '))
	objective = int(input('Que numero quieres encontrar '))

	num_list = sorted([random.randint(0, 100) for i in range(len_list)])

	matched = binary_search(num_list, 0, len(num_list), objective)
	print(num_list)
	print(f'El elemento {objective} {"esta en la lista" if matched else "no esta en la lista"}')

