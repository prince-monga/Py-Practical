class Animal:
    def eat(self):
        print("This animal eats food.")

class Mammal(Animal):
    def sleep(self):
        print("This mammal sleeps.")

class Dog(Mammal):
    def bark(self):
        print("The dog barks.")

dog = Dog()
dog.eat()    
dog.sleep()  
dog.bark()   
