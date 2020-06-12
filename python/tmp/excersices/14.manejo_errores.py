
countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}

print('La lista de paises disponibles son:')
for key in countries:
    print(key)



while True:
    country = str(input('\n Escriba nombre del pais: ')).lower()
    try:
        print('La poblacion de {} es de {} millones'.format(country, countries[country]))
    except KeyError:
        print('Pinche bato, este men >:v "{}" no existe en el diccionario'.format(country))
