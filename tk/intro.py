from tkinter import *


root = Tk()
root.title('hola mundo')
root.geometry('500x500')

label = Label(root, text="Hola mundo mi primera etiqueta")
#Label(root, text="Hola mundo mi primera etiqueta").pack()

label.pack()

root.mainloop()
