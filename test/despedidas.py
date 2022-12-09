def despedir():
    print("Adios")
    print("Hasta luego")
    print("Hasta pronto")

class Despedida:
    def __init__(self, nombre):
        self.nombre = nombre

    def Despedir(self):
        print("Adios",self.nombre)
        print("Hasta luego",self.nombre)
        print("Hasta pronto",self.nombre)