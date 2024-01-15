from tkinter import *

root = Tk()
root.title('Hola mundo: checkbox')

root.geometry('500x500')

var = StringVar()
#con esta linea le seteo por defecto un valor al Checkbutton
var.set('si')

#con esta funcion me permite mostrar en la ventana lo que le especifique
#al Checkbutton
def mostrar():
    l = Label(root, text=var.get())
    l.pack()

c = Checkbutton(root, text='Soy un checkbox', variable=var, onvalue='si', offvalue='chanchito feliz')
c.pack()

btn = Button(root, text='Click', command=mostrar)
btn.pack()

root.mainloop()
