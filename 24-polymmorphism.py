class Car:
    def start_engine(self):
        print("The car's engine is starting.")

class SportsCar(Car):
    def start_engine(self):
        print("The sports car's engine starts with a roar!")

class ElectricCar(Car):
    def start_engine(self):
        print("The electric car's engine starts silently.")

class Sedan(Car):
    def start_engine(self):
        print("The sedan's engine starts smoothly.")

def start_car_engine(car):
    car.start_engine()

sports_car = SportsCar()
electric_car = ElectricCar()
sedan = Sedan()

start_car_engine(sports_car)   
start_car_engine(electric_car) 
start_car_engine(sedan)        
