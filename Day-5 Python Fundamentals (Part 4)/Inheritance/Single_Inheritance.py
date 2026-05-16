class Employee:
    start_time="10 AM"
    end_time="6 PM"

    def change_time(self,new_EndTime):
        self.end_time=new_EndTime

class Teacher(Employee):
    def __init__(self,subject):
        self.subject=subject

class Administrative(Employee):
    def __init__(self,role):
        self.role=role

t1=Teacher("DSA")
a1=Administrative("Food Manager")

print(t1.subject, t1.start_time, t1.end_time)
a1.change_time("5 PM")
print(a1.role, a1.start_time, a1.end_time)


        
