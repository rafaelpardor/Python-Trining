# -*- coding: utf-8 -*-

# Class exercises
# Primer interfaz de Perro solo con atributos
#class keyword para python, en este caso s, PEP 8 va a llamar perro

class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edad = 3
        self.color = "Blanco con manchas negras"

    def ladrar(self):
        print("guuuau")

    def sentarse(self):
        print(self.nombre,"se esta sentado!")

    def dormir(self):
        print("El perro es va a dormir ya mismo")

# Instanciemos
maya = Perro("Luna")


# Accedamos al atributo usando la notación de punto

print("Nombre: "+ maya.nombre)
print("Edad :", maya.edad)
print("Color: "+ maya.color)
maya.ladrar()
maya.sentarse()
