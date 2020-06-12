
def chaos():
    print("Chaos")

    x = eval(input("Put a number between 0 and 1: "))
    n = eval(input("How many numbers should I print?: "))

    for _ in range(n):
        x = 3.9 * x * (1-x)
        print(x)


chaos()
