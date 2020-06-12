#!/usr/bin/python3

# Ley de multiplicacion

def f(n):
	for i in range(n):
		for j in range(n):
			print(i, j)

# O(n) * O(n) = O(n * n) = O(n * n)
# Hay un loop dentro de un loop, por ley de multiplicacion el algoritmo es cuadratica

def fibonacci(n):
	if n == 0 or n == 1:
		return 1

	return fibonacci(n - 1) + 

# O(2**n)
# Hace llamadas a su misma funcion varias veces, esto la convierte en  un algoritmo exponencial
