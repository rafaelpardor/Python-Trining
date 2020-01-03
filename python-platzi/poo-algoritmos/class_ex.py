#!/urs/bin/python3

class Person:
    # Class initialitation
    def __init__(self, name, age):
        self.name= name
        self.age = age
    
    # Methods
    def cheer(self, otherPerson):
        return f'Hola {otherPerson.name}, me llamo {self.name}, tengo {self.age}.'

rafael = Person('Rafael', 21)
martha = Person('Martha', 30)

print(rafael.cheer(martha))

