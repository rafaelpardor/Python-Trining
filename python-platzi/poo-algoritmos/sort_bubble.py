#!/usr/bin/python3

import random

def bubble_sort(num_list):
  n = len(num_list)

  for i in range(n): # O(n^2)
    for j in range(0, n - i - 1):
      if num_list[j] > num_list[j + 1]:
        num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

  return num_list

if __name__ == '__main__':
	tamano_num_list = int(input('De que tamano es la num_list? '))

	num_list = [random.randint(0, 100) for i in range(tamano_num_list)]
	print(num_list)
	order_list = bubble_sort(num_list)
	print(order_list)
