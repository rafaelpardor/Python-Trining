# !/usr/bin/python3

class Washer:
    def __init__(self):
        pass

    def wash(self, temperature='hot'):
        self._fill_tank_water(temperature)
        self._add_soap()
        self._wash()
        self._finish()

    def _fill_tank_water(self, temperature):
        print(f'filling water: {temperature}')

    def _add_soap(self):
        print('Adding soap')

    def _wash(self):
        print('Washing clothes')

    def _finish(self):
        print('Wahser has been terminated')


if __name__ == '__main__':
    washer = Washer()
    washer.wash()
