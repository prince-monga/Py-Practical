#inhertnce
#parent class
class student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age 
        self.course=course
    def display(self):
        print(f"Student Name is {self.name} and age {self.age}")
#Child Class
class passout(student):
    def __init__(self,name,age,course,passout_year):
        super().__init__(name,age,course)
        self.passout_year=passout_year
    
    def Pdisplay(self):
        print(f"Name:{self.name} complete {self.course} in {self.passout_year}")

s1=passout("prince",21,"BCA","2022")
s1.display()  #Parent class method call
s1.Pdisplay() #child class method 