class Student:
    college="JIST" #class
    PI=3.14

    def __init__(self,name,cgpa):
        self.name=name #instance
        self.cgpa=cgpa
        self.PI=3.1415

stu1=Student("Sayan",9.5)
print(stu1.name,stu1.cgpa)

#Object has higher Priority than CLASS.
#THROUGH OBJECT WE CAN ACCESS BOTH CLASS AND INSTANCE


#INSTANCE HAS  higher priority
print(stu1.PI)#3.1415 will print 
#because instace contain unique value
print(Student.PI)