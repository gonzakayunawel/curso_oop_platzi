from car import Car


def run():
    print("Instanciando Objetos en Python...")
    
    car = Car()
    car.license = "AMS234"
    car.driver = "Andres Herrera"
    print(vars(car))
    
    car2 = Car()
    car2.license = "QWE567"
    car2.driver = "Martha Erices"
    print(vars(car2))

if __name__ == "__main__":
    run()