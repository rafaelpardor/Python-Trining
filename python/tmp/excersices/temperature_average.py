
def average_temps(temps):
    sums_of_temps = 0

    for temp in temps:
        sums_of_temps += float(temp)

    return sums_of_temps / len(temps)

if __name__ == '__main__':
    temps = [10,27,14,22,2,23,24,2,5,6,83,37,8,100,3,7,83]

    avarage = average_temps(temps)

    print('La temperatura promedio es: {}'.format(avarage),'grados')