class Employee:
    start_time="10 AM"
    end_time="6 PM"


class Administrative(Employee):
    def __init__(self,role):
        self.role=role

class AccountStaff(Administrative):
    def __init__(self,salary,role):
        super().__init__(role)
        self.salary=salary


acc1=AccountStaff(50_000,"MANAGER")

print(f"Role: {acc1.role}")
print(f"Salary: {acc1.salary}")
print(f"Working Hours: {acc1.start_time} to {acc1.end_time}")



