class Animal:
    def speak(self):
        print("The animal makes a sound.")

class Bird:
    def fly(self):
        print("The bird flies.")

class Bat(Animal, Bird):
    def hang(self):
        print("The bat hangs upside down.")

bat = Bat()
bat.speak()  
bat.fly()    
bat.hang()   
