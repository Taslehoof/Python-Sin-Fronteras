class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print('Hola!, mi nombre es ', self.nombre, self.apellido)

usuario = Usuario('Felipe', 'Feliz')
usuario2 = Usuario('Chanchito', 'Feliz')


#usuario.saludo()
#usuario2.saludo()
