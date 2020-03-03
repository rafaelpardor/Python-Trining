# Variables.

print('')
var = 15

print('We create a new variable called "var" and with a value of {}'.format(var))
print(var)
# -------------------------------------

print('')
PI = 3.14
radio = 5
area = PI * (radio**2)

print('The area of a circle, with {} of radio.'.format(radio))
print (area)
# -------------------------------------

print('')
first_name = "ada"
last_name = "lovelace"
full_name = ('{} {}'.format(first_name,last_name))

message = "Hello, " + full_name.title() + "!"
print(message)

# -------------------------------------

print('')
name = str(input('What is your name?: '))    
age = int(input('how old are you?: '))

print('Hello, {}, you are {} years old!'.format(name,age))
# -------------------------------------
