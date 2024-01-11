from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Carrusel')

img1 = ImageTk.PhotoImage(Image.open('imagenes/1.jpg'))
img2 = ImageTk.PhotoImage(Image.open('imagenes/2.jpg'))
img3 = ImageTk.PhotoImage(Image.open('imagenes/3.jpg'))
img4 = ImageTk.PhotoImage(Image.open('imagenes/4.jpg'))

lista = [img1, img2, img3, img4]

def adelante(img_num):
    pass

l = Label(root, image = img1)
l.grid(row=0, column=0, columnspan=3)


btn_atras = Button(root, text='N/A', state=DISABLED)
btn_adelante = Button(root, text='-->', command= lambda: adelante(1))

btn_atras.grid(row=1, column=0)
btn_adelante.grid(row=1, column=2)


















root.mainloop()
