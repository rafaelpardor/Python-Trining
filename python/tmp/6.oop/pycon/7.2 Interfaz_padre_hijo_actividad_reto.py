# Actividad y reto
# Output:
# De mi padre he heredado:
# 2 atributos
#
# De mi madre he heredado:
#2 atributos

# -*- coding: utf-8 -*-


class Padre:
    ojos = "Azules"
    piel = "Blanco"

class Madre:
    cabello = "liso"
    manos = "grandes"


class HijoPadre(Padre):
    def describir_herencia_padre(self):
        print("De mi padre he heredado: ")
        print("Color de ojos,", self.ojos)
        print("Color de piel,", Padre.piel)

class HijoMadre():
    def describir_herencia_madre():
        #imprima los dos atributos heredados de Madre
        pass


nicolas = HijoPadre()
nicolas.describir_herencia_padre()
