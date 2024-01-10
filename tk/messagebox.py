from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Hola mundo!')

##Mensaje de Advertencia con un Popup
#def click():
   #messagebox.showwarning('Popup', 'Hola Mundo!')

#Mensaje de informacion con un Popup
#def click():
   # messagebox.showinfo('Popup', 'Hola Mundo!')

#Mensaje de error con un Popup
#def click():
   # messagebox.showerror('Popup', 'Hola Mundo!')

#Mensaje de pregunta para el usuario  con un Popup
#def click():
#   respuesta = messagebox.askquestion('Popup', 'Hola Mundo! :(')
    #askquestion no me devvuelve un boolean asi que tengo que escribir codigo spaghetti
#   if respuesta == 'yes':
#        messagebox.showinfo('Respuesta',' la respuesta fue ' + respuesta)
#   else:
#        messagebox.showinfo('Respuesta', ':( la respuesta fue ' + respuesta)

#Mensaje de pregunta para el usuario  con un Popup
#def click():
#    respuesta = messagebox.askokcancel('Popup', 'Desea realizar la accion?')
    #askokcancel me devuelve un boolean asi que puedo hacer preguntas por VoF
#    if respuesta:
#        messagebox.showinfo('Respuesta',' la respuesta fue OK')
#    else:
#        messagebox.showinfo('Respuesta', 'La respuesta fue Cancelar')

#Mensaje de pregunta para el usuario  con un Popup
def click():
    respuesta = messagebox.askyesno('Popup', 'Desea realizar la accion?')
    #askokcancel me devuelve un boolean asi que puedo hacer preguntas por VoF
    if respuesta:
        messagebox.showinfo('Respuesta',' la respuesta fue Yes')
    else:
        messagebox.showinfo('Respuesta', 'La respuesta fue No')

btn = Button(root, text='Presioname', command=click)
btn.pack()

root.mainloop()
