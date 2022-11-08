class Persona():
    
    def __init__(self, nombre, edad, residencia):
        
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia
        
    def descripcion(self):
        
        print("Nombre: %s" % self.nombre,
              "\nEdad: %s" % self.edad,
              "\nResidencia: %s" % self.residencia)

class Funcionario(Persona):
    
    def __init__(self, nombre, edad, residencia, sueldo, antiguedad):
        super().__init__(nombre, edad, residencia)
        self.sueldo= sueldo
        self.antiguedad=antiguedad
        
    def descripcion(self):
        super().descripcion()
        
        print("Sueldo: %s" % self.sueldo,
              "\nAntigüedad: %s" % self.antiguedad)

funcionario1 = Funcionario("Johannes", 33, "Puente Alto", 1_500_000, 22)

funcionario1.descripcion()
persona1 = Persona("Diego", 54, "Tijuana")

print(isinstance(funcionario1, Funcionario))
print(isinstance(persona1, Persona))
print(isinstance(persona1, Funcionario))