
# This program says hello to your name and to your age.

print('Hello, world!')

print('What is your name?')
my_name = input()
print('It is good to mmet you, {}'.format(my_name))
print('The length of four name is :: {}'.format(len(my_name)))

print('What is your age?')
my_age = input()
print('{} you will be {} in a year.'.format(my_name, int(my_age)+1))
# print('Your age is :: '+ str(int(my_age)))