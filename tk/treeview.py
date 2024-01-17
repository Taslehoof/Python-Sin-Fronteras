from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Hola Mundo: Treeview')

tree = ttk.Treeview(root)
tree['columns'] = ('Nombre', 'Telefono', 'Empresa')
