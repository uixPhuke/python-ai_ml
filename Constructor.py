class Employee:
    def __init__(self):  #Self is current instance of the class #Current Object
        print("This is a constructor")

emp1=Employee()#first perameter is by default self

class Student:
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa

student1=Student("Phuke",8.5)
student2=Student("Martin",9.5)
student3=Student("Mia",9)
print(student1.name)
print(student2.cgpa)
print(student3.name)