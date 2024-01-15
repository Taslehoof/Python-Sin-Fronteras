from tkinter import * 

root = Tk()
root.title('Hola mundo: Option Menu')
root.geometry('500x500')

def enviar():
    l = Label(root, text=value.get())
    l.pack()

lista = [
    'Chanchito Feliz',
    'Chancito triste',
    'Chanchito emocionado'
]

value = StringVar()
value.set(lista[1])

#Con estas opciones defino el OptionMenu de manera statica 
#drop = OptionMenu(root, value, 'Chanchito Feliz', 'Chancito triste', 'Chanchito emocionado')

#De esta manera puedo hacer que se muestre la lista de manera dinamica
drop = OptionMenu(root, value, *lista)

drop.pack()

btn = Button(root, text='Enviar', command=enviar)
btn.pack()

root.mainloop()
