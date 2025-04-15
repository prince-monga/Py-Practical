#abstraction
#Hidding Unnessary Details  from user through class method 

class student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def display(self):
        print(f"Student Name is {self.name} and age {self.age}")

s1=student("Prince",21,"BCA")
s1.display() #"The user doesn’t know how this is being displayed 
# — this is an example of abstraction, which hides unnecessary details.
