#!/usr/bin/python3

class VotationSite:
    def __init__(self, Id, country):
        self._Id = Id
        self._country = country
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def set_region(self, region):
        if region in self.country:
            self._region = region

        raise ValueError(f'The region {region} is not valid in {self._country}')

if __name__ == "__main__":
    casilla = VotationSite(123, ["Bogota", "Soacha"])
    print(casilla.region)
    casilla.region = "Bogota"
    print(casilla.region)
