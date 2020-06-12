
# Elif statement.

def hello(age):
    if (age < 12):
        return'Hello Child'
    elif((age >= 12) and (age <= 16)):
        return'Hello Teen'
    elif((age >= 17) and (age <= 21)):
        return'Hello Young'
    else:
        return'Hello Senior'

age = int(input('Enter your age: '))
show = hello(age)
print(show)

if __name__=='__main__':
    print('')
    hello(age)
