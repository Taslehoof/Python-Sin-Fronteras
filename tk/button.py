from tkinter import *

root = Tk()
root.title("Hola Mundo!")

l = Label(root, text="Hola Mundo")

def click():
    l.pack()

btn = Button(root, text="Clickeame", command= click, fg='red')
btn.pack()

root.mainloop()
