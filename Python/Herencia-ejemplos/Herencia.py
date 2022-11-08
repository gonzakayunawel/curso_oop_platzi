
# Creamos una superclase
class Vehiculos():
    # Método constructor
    
    def __init__(self, marca, modelo):
    # Definimos características y su valor de inicio
    
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
    # Definimos comportamientos de la superclase
    
    def arrancar(self):
        
        self.enmarcha = True
    
    def acelerar(self):
        
        self.acelera = True
    
    def frenar(self):
        
        self.frena = True
    
    def estado(self):
        print("Marca: ", self.marca,
              "\nModelo: ",self.modelo,
              "\nEn marcha: ",self.enmarcha,
              "\nAcelerando: ", self.acelera,
              "\nFrenando: ", self.frena)
        
        
# Declaramos un clase llamada Furgoneta

class Furgoneta(Vehiculos):
    
    def carga(self, cargar):
        self.cargado = cargar
        if(self.cargado):
            return "La Furgoneta está cargada"
        else:
            return "La Furgoneta no está cargada"

# Declaramos una clase y la hacemos heredar
# Ejemplo


class Moto(Vehiculos):
    wheelie=""
    def wheelie(self):
        self.wheelie="Voy parando rueda"

    def estado(self):
        print("Marca: ", self.marca,
              "\nModelo: ",self.modelo,
              "\nEn marcha: ",self.enmarcha,
              "\nAcelerando: ", self.acelera,
              "\nFrenando: ", self.frena,
              "\nWheelie: ", self.wheelie)
        
        
class VElectricos():
    
    def __init__(self):
        self.autonomia=100
    
    def cargarEnergia(self):
        
        self.cargando=True

# Instanciando un objeto Moto
# Como este objeto de clase hereda de Vehiculos sus caracteristicas
# Debemos declarar las 2 propiedades de inicio
# marca y modelo

miMoto=Moto("Honda", "CBR")

# Al crear el objeto  podemos llamar a los métodos de la clase

miMoto.wheelie()
miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))

# Clase para vehiculos electricos

class VElectricos():
    
    def __init__(self):
        self.autonomia=100
    
    def cargarEnergia(self):
        
        self.cargando=True

# Herencia múltiple
# Puedo heredar desde más de una clase
# Se indica al momento de crear la clase
# las clases desde las cuales se hereda


class BiciElectrica(VElectricos, Vehiculos):
    
    pass

# Si declaramos la clase y llamamos al método constructor de Vehiculos
# Nos dará error
miBici=BiciElectrica("Orbea", "HC1030")
    