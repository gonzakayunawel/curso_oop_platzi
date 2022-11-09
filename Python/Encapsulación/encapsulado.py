class Automovil():
    # metodo constructor
    def __init__(self):
        
        self.largoChasis =250
        self.anchoChasis =120
        # Para encapsular se hacen 2 guiones bajos al comenzar el nombre
		# de la variable
        # Ahora esta variable está encapsulada y no se puede cambiar
        # desde afuera
        self.__ruedas =4
        self.enmarcha=False

    def arrancar(self, arranque):
        self.enmarcha = arranque
        if(self.enmarcha):
            check=self.__car_conditions()
        
        if(self.enmarcha and check):
            return "El auto está en marcha."
        elif(self.enmarcha and check==False):
            return "Error de arranque, condiciones defectuosas. Auto detenido"
        else:
            return "El auto está parado."

    def estado(self):
        print("El auto tiene %s ruedas." % self.__ruedas,
              "\nUn ancho de %s cm." % self.anchoChasis,
              "\nY un largo de %s cm." % self.largoChasis)
    
    # Para encapsular el método de la clase agregamos 2 guiones bajos al inicio
    # Al igual que con las variables
    def __car_conditions(self):
        print("Realizando comprobación de condiciones.")
        
        self.combustible="ok"
        self.aceite="empty"
        self.puertas="cerradas"
        
        if(self.combustible=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False


miAuto=Automovil()
print(miAuto.arrancar(True))
miAuto.estado()

print("\n---------------------A continuación creamos el segundo objeto.---------------------")
print("\n")

miAuto2=Automovil()
miAuto2.__ruedas=2
print(miAuto2.arrancar(False))
miAuto2.estado()