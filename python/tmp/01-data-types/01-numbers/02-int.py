# !/usr/bin/python3

import math
import random


def numbers1():
    print('--- INT 1---')

    number_1 = 3
    number_2 = 32

    print('Number {} is a INT: {}' .format(number_1, type(number_1)))
    print('We can change a INT to a STRING: "{}"' .format(str(15)))
    print('We can change a INT to a FLOAT:', float(number_2))


def numbers2():
    print('\n--- INT 2 ---')

    number = 20
    numb_list = [1, 2, 3, 4, 5]

    print("PI:", math.pi)
    print("SQRT", int(math.sqrt(number)))
    print(random.random)
    print("Random between 0 and 1:", random.random())
    print("Getting a random nummber", random.choice(numb_list))


if __name__ == "__main__":
    numbers1()
    numbers2()
