#old method
student1={      
    "name":"prince",
    "age": 21,
    "course":"BCA",
}
student2={      
    "name":"Arun",
    "age": 21,
    "course":"BCOM",
}

print(f"Student Name:{student1["name"]} and Student Age:{student1["age"]} and Student Course:{student1["course"]}")
print(f"Student Name:{student2["name"]} and Student Age:{student2["age"]} and Student Course:{student2["course"]}")

#it is dictionary

#list
student1={"Prince",21,"BCA"}
student2={"Arun",21,"BCOM"}
#print(f"Student Name:{student[0]} and Student Age:{student1[1]} and Student Course:{student1[2]}")
#print(f"Student Name:{student2[0]} and Student Age:{student2[1]} and Student Course:{student2[2]}")

#it is very difficult to access the data in list and it is not easy to understand the data in list.

#and add more data in list is very difficult.
#and also remove the data in list is very difficult.
#and also update the data in list is very difficult.
#and also check the data in list is very difficult.
#and also check the data in list is very difficult.

#OOps
#class and object
#using class and object we can easily access the data.
#and also add more data in class is very easy.
print("Using class and object")
class student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course  
    
    def display(self):
        print(f"Student Name:{self.name} and Student Age:{self.age} and Student Course:{self.course}")
  

#creating object of class
student1=student("Prince",21,"BCA")
student2=student("Arun",21,"BCOM")

student1.display()
student2.display()
