
calificaciones = {}
calificaciones['Algoritmos'] = 9
calificaciones['Sociales'] = 1
calificaciones['Matematicas'] = 5
calificaciones['Web'] = 2
calificaciones['Bases_de_datos'] = 4

for key in calificaciones:
    print(key)

for value in calificaciones.values():
    print(value)

for key, value in calificaciones.items():
    print('Llave: {}.\nValor: {}'.format(key,value))

# CALCULAR PROMEDIO

print('')
print('Primedio de notas ::')
print('--------------')

suma_de_calificaciones = 0
for value in calificaciones.values():
    suma_de_calificaciones += value

promedio = suma_de_calificaciones/len(calificaciones.values())

print('Promedio: {}'.format(promedio))
print('--------------')


# capitales = {
#     'Chile': 'Santiago',
#     'Peru': 'Lima',
#     'Ecuador': 'Quito',
#     'Colombia': 'Bogota'
# }

# for pais in capitales:
#     print ('La capital de',pais,'es',capitales[pais])

# print('')
    
# for capital in capitales.values():
#     print(capital, 'es una linda ciudad')

# print('')

# for p, c in capitales.items():
#     print(c, 'es la capital de', p)

# print('')

# patas = {
#     'humanos':2,
#     'pulpo':8,
#     'perro':4,
#     'gato':4,
#     'ciempies':100
# }
# print(patas)
# print(patas.keys())
# print(patas.values())
# print(patas.items())

# print('perro' in patas)
# print(8 in patas)
# print(len(patas()))




# d = {}
# d['llave1'] = 5
# d['llave2'] = 352
# d['llave3'] = 645
# print(d)

# Mientras que a las listas y tuplas se accede solo y únicamente por un número de índice, los diccionarios permiten utilizar una llave, ademas de que es un elemento inmutable, para declarar y acceder a un valor

# mi_diccionario = {
#     'Pepito': 2372202,
#     'Jaime': 5461236,
#     'clave_7': 8105617
# } 
# print (mi_diccionario['Jaime'])