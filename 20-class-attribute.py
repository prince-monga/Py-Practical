class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def display_info(self):
        print(f"Car Details: {self.year} {self.color} {self.make} {self.model}")

    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine is now running!")

car1 = Car("Toyota", "Corolla", 2020, "Red")
car1.display_info()
car1.start_engine()
