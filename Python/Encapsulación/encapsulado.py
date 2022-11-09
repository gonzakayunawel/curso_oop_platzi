class Automovil():
    largoChasis =250
    anchoChasis =120
    ruedas =4
    enmarcha=False

    def arrancar(self, arranque):
        self.enmarcha = arranque
        
        if(self.enmarcha):
            return "El auto está en marcha."
        else:
            return "El auto está parado."

    def estado(self):
        print("El auto tiene %s ruedas." % self.ruedas,
              "\nUn ancho de %s cm." % self.anchoChasis,
              "\nY un largo de %s cm." % self.largoChasis)


miAuto=Automovil()
print(miAuto.arrancar(True))
miAuto.estado()

print("\n---------------------A continuación creamos el segundo objeto.---------------------")
print("\n")

miAuto2=Automovil()
print(miAuto2.arrancar(False))
miAuto2.estado()