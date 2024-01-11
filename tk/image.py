from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hola Mundo!!!')

#Con esto me abre la foto en una ventana aparte
#imagen = Image.open('debian_retro.jpg')
#imagen.show()

#Con esto me abre la imagen en la misma ventana
img = ImageTk.PhotoImage(Image.open('debian_retro.jpg'))
l = Label(image=img)
l.pack()


root.mainloop()
