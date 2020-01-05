#!urs/bin/python3

import random

def busqueda_binaria(lista, start, final, objetivo):
	print(f'Buscando {objetivo} entre {lista[start]} y {lista[final-1]}')
	count = 0

	if start > final:
		return False
	
	mid = (start + final) // 2

	if lista[mid]==objetivo:
		print('Se hacen estos movimientos: ',count)
		count+=1
		return True
	elif lista[mid]< objetivo:
		return busqueda_binaria(lista, mid+1,final,objetivo)
	else:
		return busqueda_binaria(lista, start, mid-1, objetivo)


if __name__ == '__main__':
	tamano_lista = int(input('De que tamano es la lista? '))
	objetivo = int(input('Que numero quieres encontrar '))

	lista = sorted([random.randint(0, 100) for i in range(tamano_lista)])

	matched = busqueda_binaria(lista,0,len(lista), objetivo)
	print(lista)
	print(f'El elemento {objetivo} {"esta en la lista" if matched else "no esta en la lista"}')
