from tkinter import *

root = Tk()
root.title('Hola mundooooo!!!!')

r = IntVar()
r.set('2')

#Los clasicos Radiobutton de toda la vida
#Radiobutton(root, text='Opcion 1', variable=r, value=1).pack()
#Radiobutton(root, text='Opcion 2', variable=r, value=2).pack()

#De esta forma estoy definiendo los valores de los Radiobutton de manera 
#dinamica para poder cambiarlos facilmente
CHANCHITOS = [
    ('Feliz','Feliz'),
    ('Triste','Triste'),
    ('Amargado','Amargado'),
    ('Wolfgang','Wolfgang')
]

chanchito = StringVar()
chanchito.set('Wolfgang')

for text, chancho in CHANCHITOS:
    Radiobutton(root, text=text, variable=chanchito, value=chancho).pack()


l = Label(root, textvariable=chanchito)
l.pack()

root.mainloop()
