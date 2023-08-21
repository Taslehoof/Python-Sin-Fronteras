"""i = 0

while i < 5:
    print(i)
    if i ==3:
        break
    i += 1

while i < 5:
    i += 1
    if i ==3:
       continue
    print(i)

usuarios = ['chanchito feliz', 'felipe', 'roberto', 'nicolas']

for usuario in usuarios:
    print(usuario)

usuario = 'Chanchito feliz'

for c in usuario:
    print(c)


usuarios = ['chanchito feliz', 'felipe', 'roberto', 'nicolas']

for usuario in usuarios:
    if usuario == 'roberto':
        break
    print(usuario)

usuarios = ['chanchito feliz', 'felipe', 'roberto', 'nicolas']

for usuario in usuarios:
    if usuario == 'roberto':
        continue
    print(usuario)

for x in range(3, 30, 5):
    print(x)
else:
    print('Hemos terminado!!')"""

usuarios = ['Chanchito feliz', 'felipe', 'roberto', 'nicolas']

edades = [24,25, 26, 35]

for usuario in usuarios:
   for edad in edades:
       print(usuario, edad)
