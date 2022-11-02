from car import Car
from account import Account


def run():
    print("Instanciando Objetos en Python...")
    
    car = Car("AMS234", Account("Andres Herrera", "ANDA876"))
    print(vars(car))
    print(vars(car.driver))
    
    # car2 = Car()
    # car2.license = "QWE567"
    # car2.driver = "Martha Erices"
    # print(vars(car2))

if __name__ == "__main__":
    run()