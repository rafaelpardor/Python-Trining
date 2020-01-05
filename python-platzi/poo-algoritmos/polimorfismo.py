#!/usr/bin/python3

class Person:
    def __init__(self, name):
        self.name = name

    def forward(self):
        print(f'{self.name} is walking')

    def secret_person(self):
        print('Hello, this method is secret')

class Biker(Person):
    def __init__(self, name):
        super().__init__(name)

    def forward(self):
        print(f'{self.name} is moving on bike')


def main():
    person = Person('Rafael')
    person.forward()
    person.secret_person()

    biker = Biker('Juan')
    biker.forward()
    biker.secret_person()

if __name__ == "__main__":
    main()
