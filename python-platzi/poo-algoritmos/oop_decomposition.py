# !/usr/bin/python3

class Car:
    def __init__(self, model, brand, doors, color):
        self.model = model
        self.brand = brand
        self.doors = doors
        self.color = color
        self.state = 'resting'
        self._engine = Engine(cylinders=4)

    def speeding(self, speed='despacio'):
        if speed == 'fast':
            self._engine.pump_gas(10)
        else:
            self._engine.pump_gas(3)

        self._state = 'movement'

class Engine:
    def __init__(self, cylinders, gas='ordinary'):
        self.cylinders = cylinders
        self.gas = gas
        self.temperature = 0

    def pump_gas(self, ammount):
        pass

if __name__ == "__main__":
    car_1=Car('MODEL', 'BRAND', 'DOORS', 'COLOR')
    print(car_1.speeding())
