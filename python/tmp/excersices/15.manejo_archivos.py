
def read():
    counter = 0
    with open('text.txt')as a:
        for line in a:
            counter += line.count('Beatriz')
    print('Beatriz se encuentra {} en el texto'.format (counter))
    
def write():
    with open('text.txt','w') as f:
        for i in range(10):
            f.write(str(i))
            f.write('Beatriz')

def leer():
    with open('text.txt') as f:
        print(f.readline())

if __name__ == '__main__':
    # read()
    # write()
    leer()