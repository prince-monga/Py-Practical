class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        print(f"{self.year} {self.make} {self.model} is created.")

    def __del__(self):
        print(f"{self.year} {self.make} {self.model} is destroyed.")


car1 = Car("Toyota", "Corolla", 2020)

del car1
