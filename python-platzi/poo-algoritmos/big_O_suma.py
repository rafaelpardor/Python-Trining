#!/usr/bin/python3

# Ley de suma

def f1(n):
	for i in range(n):
		print(i)

	for i in range(n):
			print(i)

# O(n) + O(n) = O(n + b) = O(2n) = O(n)
# El algoritmo crece de forma lineal


def f2(n):
	for i in range(n):
		print(i)

	for i in range(n * n):
			print(i)

# O(n) + O(n * n) = O(n + n*n) = O(n*n)
# El algoritmo crece de forma cuadratica, porque importa el input mas grande, mientras mas
# nos acercamos a infinito