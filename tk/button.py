from tkinter import *

root = Tk()
root.title("Hola Mundo!")

def click():
    l = Label(root, text="Hola Mundo")
    l.pack()

btn = Button(root, text="Clickeame", command= click)
btn.pack()

root.mainloop()
