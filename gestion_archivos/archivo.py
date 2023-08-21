#c = open('chanchito.txt', 'w')

#print(c.read())

#print(c.readline())

#c.write('\nagregamos una nueva linea a nuestro archivo')
#c.close()

#x = open('chanchito.txt')
#print(x.read())

import os

#os.remove('chanchito.txt')

if os.path.exists('chanchito.txt'):
    os.remove('chanchito.txt')
else:
    print('El archivo no existe')

os.rmdir('micarpeta')