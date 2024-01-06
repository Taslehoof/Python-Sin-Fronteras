from tkinter import *

root = Tk()
root.title('Hola mundo!')
root.geometry('500x500')

#input para ingresar cualquier tipo de texto en la ventana
e = Entry(root, width=40)
e.pack()
e.insert(0, 'Ingresa texto: ')

#Funcion que me permite borrar el texto y pegarlo abajo del boton
def click():
    texto = e.get()
    textvariable.set(texto)
    valor = textvariable.get()
    print(valor)
    #l = Label(root, text=texto)
    #l.pack()
    e.delete(0, END)
    #l.configure(text=texto)

#boton con leyenda que dispara la funcion 
btn = Button(root, text='click', command=click)
btn.pack()

textvariable = StringVar()

l = Label(root, textvariable=textvariable)
l.pack()

#elemento que queda a la espera de cualquier evento
root.mainloop()
