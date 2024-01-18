from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

root = Tk()
root.title('Hola Mundo: CRM')

#creacion de la conexion 
conn = sqlite3.connect('crm.db')

c = conn.cursor()

#defino como va a ser la tabla para poder despues persistir los datos
c.execute("""
        CREATE TABLE if not exists cliente(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            empresa TEXT NOT NULL
        );
""")

#Con esta funcion renderizo constantemente los clientes en pantlla para que me refresque el contenido
def render_clientes():
    rows = c.execute("SELECT * FROM cliente").fetchall()

    tree.delete(*tree.get_children())

    for row in rows:
        tree.insert('', END, row[0], values=(row[1], row[2], row[3]))

#Aca se define los metodos de la funcio para poder hacer la insercion en la BDD
def insertar(cliente):
    c.execute("""
            INSERT INTO cliente(nombre, telefono, empresa) VALUES (?, ?, ?)
            """, (cliente['nombre'], cliente['telefono'], cliente['empresa']))
    conn.commit()
    render_clientes()

#Pasos previos y validaciones para cuando hago la carga de datos
def nuevo_cliente():
    def guardar():
        if not nombre.get():
            messagebox.showerror('Error','El nombre es obligatorio')
            return

        if not telefono.get():
            messagebox.showerror('Error','El telefono es obligatorio')
            return

        if not empresa.get():
            messagebox.showerror('Error','El campo Empresa es obligatorio')
            return

        cliente = {
            'nombre': nombre.get() ,
            'telefono': telefono.get() ,
            'empresa': empresa.get()
        }
        insertar(cliente)
        top.destroy()

    top = Toplevel()
    top.title('Nuevo cliente')
    
    lnombre = Label(top,text='Nombre')
    nombre = Entry(top, width=40)
    lnombre.grid(row=0, column=0)
    nombre.grid(row=0, column=1)

    ltelefono = Label(top,text='Telefono')
    telefono = Entry(top, width=40)
    ltelefono.grid(row=1, column=0)
    telefono.grid(row=1, column=1)

    lempresa = Label(top,text='Empresa')
    empresa = Entry(top, width=40)
    lempresa.grid(row=2, column=0)
    empresa.grid(row=2, column=1)

    guardar = Button(top, text='Guardar', command=guardar)
    guardar.grid(row=3, column=1)

    top.mainloop()
    
#Para poder buscar en la BDD y que me elimine los datos que seleccione y no otros
def eliminar_cliente():
    id = tree.selection()[0]

    cliente = c.execute("SELECT * FROM cliente WHERE id = ?",(id, )).fetchone()
    respuesta = messagebox.askokcancel('Seguro?','Estas seguro de querer eliminar el cliente '+ cliente[1] +' ?')
    if respuesta:
        c.execute("DELETE FROM cliente WHERE id = ?", (id, ))
        conn.commit()
        render_clientes()
    else:
        pass

#Aca hago la definicion de todo el entorno con el que se inicia la App
btn = Button(root, text='Nuevo Cliente', command=nuevo_cliente)
btn.grid(column=0, row=0)


btn = Button(root, text='Eliminar Cliente', command=eliminar_cliente)
btn.grid(column=1, row=0)

tree = ttk.Treeview(root)
tree['columns'] = ('Nombre', 'Telefono', 'Empresa')
tree.column('#0', width=0, stretch=NO)
tree.column('Nombre')
tree.column('Telefono')
tree.column('Empresa')

tree.heading('Nombre', text='Nombre')
tree.heading('Telefono', text='Telefono')
tree.heading('Empresa', text='Empresa')
tree.grid(column=0, row=1, columnspan=2)

render_clientes()

root.mainloop()
