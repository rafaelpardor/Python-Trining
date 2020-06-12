#!/usr/bin/python3

import random

def lineal_search(numbs, obj):
	match = False
	count = 0

	for element in numbs: #O(n)
		count+=1
		if element == objective:
			match = True
			break

	print('Se hacern estos movimientos', count)
	return match

if __name__ == '__main__':
	len_list = int(input('Length of your list?\n-> '))
	objective = int(input('What number you want to find?\n->'))

	nums = [random.randint(0, 100) for i in range(len_list)]

	matched = lineal_search(nums, objective)
	print(nums)
	print(f'El elemento {objective} {"esta en la lista" if matched else "no esta en la lista"}')
