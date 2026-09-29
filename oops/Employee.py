#class named employee attributes empid,name,age,salary,designation,
# #methods getsalary(),personaldetails()
#create an employee objects and call methods
class Employee:
    def __init__(self):
        self.name=input("enter name")
        self.id = input("enter id")
        self.age = input("enter age")
        self.salary = input("enter salary")
        self.role = input("enter designation")
    def get_salary(self):
        print(self.salary)
    def employee_details(self):
        print(self.name,self.role ,end="" )
        print(self.id)
        print(self.age)
e1=Employee()
e2=Employee()
e1.get_salary()
e1.employee_details()
e2.get_salary()
e2.employee_details()
