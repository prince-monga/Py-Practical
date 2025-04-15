#class and object
#class is a blueprint for creating objects.
class student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course

s1=student("prince",22,"BCA")
print(s1.__dict__)
#update data
s1.name="Arun"
print(s1.__dict__)
#delete attribute
del s1.course
print(s1.__dict__)

#delete object
del s1
print(s1.__dict__)
#"The user doesn’t know how this is being displayed 
# — this is an example of abstraction, which hides unnecessary details.
