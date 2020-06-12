#!/usr/bin/python3

class Person:
    # Class init
    def __init__(self, name, age):
        self.name= name
        self.age = age

    # Methods
    def my_name(self):
	return f'Hello, my name is {self.name}, and I have {self.age} years old'

    def greeting(self, otherPerson):
        return f'Hola {otherPerson.name}, me llamo {self.name}.'

def main():
    # Class initialitation
    rafael = Person('Rafael', 21)
    martha = Person('Martha', 30)

    print(rafael.my_name())
    print(rafael.greeting(martha))

if __name__ == '__main__':
	main()
