class Employee:
    def get_designation(self):
        print("Designation is Employee")

class Teacher(Employee):
    def get_designation(self):
        print("Designation is Teacher")

t1=Teacher()
t1.get_designation()
#get_designation function got overrided