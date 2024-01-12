from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hola mundoooooouuu!!!!!')

#solucion 1
#def open():
#    img = ImageTk.PhotoImage(Image.open('Sabaton.jpg'))
#    top = Toplevel()
#    top.title('Hola mundo, nueva ventana')
#    l = Label(top, text='Soy un texto en una segunda ventana')
#    l2 = Label(top, image=img)
#    l.pack()
#    l2.pack()
#    top.mainloop()

#solucion 2
def open():
    global img
    img = ImageTk.PhotoImage(Image.open('Sabaton.jpg'))
    top = Toplevel()
    top.title('Hola mundo, nueva ventana')
    l = Label(top, text='Soy un texto en una segunda ventana')
    l2 = Label(top, image=img)
    l.pack()
    l2.pack()

btn = Button(root, text='Click', command=open).pack()

root.mainloop()
