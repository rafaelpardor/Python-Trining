#!/usr/bin/python3

import time

def factorial(n):
    response = 1

    while n > 1:
        response *= n
        n -= 1

    return response

def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial(n-1)

if __name__ == "__main__":
    n = 10000

    start_1 = time.time()
    factorial(n)
    final_1 = time.time()
    print(final_1-start_1)


    start_2 = time.time()
    factorial(n)
    final_2 = time.time()
    print(final_2-start_2)
