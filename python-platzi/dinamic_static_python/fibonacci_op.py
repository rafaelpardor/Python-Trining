#!/usb/bin/python3

def fibonacci_recurssion(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci_recurssion(n - 1) + fibonacci_recurssion(n - 2)

def fibonacci_dinamico(n, memo = {}):
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    except KeyError:
        resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
        memo[n] = resultado

        return resultado

if __name__ == '__main__':
    n = int(input('Insert a number:'))
    resultado = fibonacci_dinamico(n)

    print(resultado)
