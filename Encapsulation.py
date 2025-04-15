#Encapsulation
# Restrict access to certain attribute or method to protect data and enforce controlled access 
#Encapsulation is the concept of wrapping data and code together into a single unit and 
# restricting direct access to some of the object's components.
class student:
    def __init__(self,name,age,course):
        self.name=name
        self.__age=age  #dobule underscore ka use krte h data Encapsulation k liye
        self.course=course
    def get_age(self):
        return self.__age
    #def display(self):
        #print(f"Student Name is {self.name} and age {self.age}")

s1=student("Prince",21,"BCA")
#s1.display() #"The user doesn’t know how this is being displayed 
# — this is an example of abstraction, which hides unnecessary details.

#print(s1.age) #error
print(s1.get_age())  #new method bna kr he Encapsulate data ko access kr skte h 
#Encapsulation allows us to protect an object's internal state by making variables private. 
#To access or update them, we define public methods. 
#This ensures that the data is used safely and only in intended ways.