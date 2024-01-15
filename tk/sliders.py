from tkinter import *

root = Tk()
root.title('Hola mundo: Sliders')

#con esto hago que se muestre la barra para ver donde estoy 
vertical = Scale(root, from_=0, to=200, command= lambda x:enviar())
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

#Esta funcion me permite imprimir en consola la posicion en la que estoy parado
def enviar():
    hor = horizontal.get()
    ver = vertical.get()
    print(str(hor) +' ' + str(ver))

btn = Button(root, text='Enviar', command=enviar)
btn.pack()

root.mainloop()
