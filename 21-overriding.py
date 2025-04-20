class Vehicle:
    def start_engine(self):
        print("The vehicle's engine is starting.")

class Car(Vehicle):
    def start_engine(self):
        print("The car's engine is starting with a roar.")

class ElectricCar(Car):
    def start_engine(self):
        print("The electric car's engine is silently starting.")

vehicle = Vehicle()
car = Car()
electric_car = ElectricCar()

vehicle.start_engine()       
car.start_engine()           
electric_car.start_engine()  
