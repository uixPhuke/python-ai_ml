#Class is a Blueprint(properties/attributes & Behaviour/methods) of an Object
#Object is instance of class
#

class Employee:
    Dept = "Technical"#properties of class
    Area="BBSR"
    Batch="2025A"

emp1=Employee()
print(type(emp1)) #Employee is a Class

print(emp1.Dept, emp1.Area, emp1.Batch)
#for eg:
s=set() #We are creating object S of Set Class