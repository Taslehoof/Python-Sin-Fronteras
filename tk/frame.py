from tkinter import *

root = Tk()
root.title('Hola Mundo')

#Para hacer un Frame con texto para que aparezca en la ventana
#frame = LabelFrame(root, text='Login', padx=10, pady=10, borderwidth=10)

#El mismo Frame que arriba pero son el texto identificador
#frame = LabelFrame(root, padx=10, pady=10, borderwidth=10)

#El frame ahora no es visible pero lo que este dentro se movera como un objeto 
frame = Frame(root, padx=10, pady=10, borderwidth=10)
frame.pack(padx=50, pady=50)

l = Label(frame, text='Estoy dentro de un Frame')
btn = Button(frame, text='Salir', command=root.quit)
l.pack()
btn.pack()

root.mainloop()
