# !/usr/bin/python3

class Washer:

    def __init__(self):
        pass

    def wash(self, temperature='hot'):
        self._fill_tank_water(temperature)
        self._add_soap()
        self._wash()
        self._centrifugar()

    def _fill_tank_water(self, temperature):
        print(f'Llenando el tanque con agua {temperature}')

    def _add_soap(self):
        print('Adding soap')

    def _wash(self):
        print('Washing clothes')

    def _centrifugar(self):
        print('Centrifugando')

if __name__ == '__main__':
    washer = Washer()
    washer.wash()
