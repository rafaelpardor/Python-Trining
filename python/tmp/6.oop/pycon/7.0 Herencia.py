# -*- coding: utf-8 -*-

# Herencia
# Interfaz Padre e Hijo

class Padre:
    color_ojos = "azul"
    color_piel = "blanco"
    cabello = "calvo"

class Hijo(Padre):
    pass



#Instance la clas Hijo únicamente
nicolas = Hijo()

#Acceda a los atributos

print(nicolas.color_piel)
print(nicolas.cabello)
