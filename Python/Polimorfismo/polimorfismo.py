class Automovil():
    def desplazamiento(self):
        print("Desplazamiento usando 4 ruedas.")

class Motocicleta():
    def desplazamiento(self):
        print("Desplazamiento usando 2 ruedas.")

class TractoCamion():
    def desplazamiento(self):
        print("Desplazamiento usando 6 ruedas.")

# Esta función recibe como parámetro un objeto de tipo genérico
# No es necesario indicarle el tipo de dato que recibe
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


harley=Motocicleta()

tiida=Automovil()

daf=TractoCamion()

# Cuando llamamos a la función y le damos como parámetro un objeto
# Automáticamente esta detecta el tipo de objeto y llama al método de la clase correspondiente
desplazamientoVehiculo(daf)
desplazamientoVehiculo(tiida)
desplazamientoVehiculo(harley)