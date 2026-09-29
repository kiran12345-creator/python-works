from abc import ABC,abstractmethod
# class Shape(ABC):
#
#     @abstractmethod
#     def get_area(self):
#         pass
#     @abstractmethod
#     def get_perimeter(self):
#         pass
#
# class Rectangle(Shape):
#     def __init__(self):
#         self.length=int(input('enter length'))
#         self.breadth=int(input('enter breadth'))
#     def get_area(self):
#         print('area is :', self.length*self.breadth)
#
#     def get_perimeter(self):
#         print('perimeter is :' , 2*(self.length+self.breadth))
#
# class Square(Shape):
#     def __init__(self):
#         self.side=int(input('enter length'))
#
#     def get_area(self):
#         print('area is :', self.side**2)
#
#     def get_perimeter(self):
#         print('perimeter is :' , 4*self.side)
#
# r=Rectangle()
# r.get_area()
# r.get_perimeter()
# s=Square()
# s.get_area()
# s.get_perimeter()



#create an abstract cllass Employee with an abstracta method calculate_salary,
#create 2 subclas
#full_time_employee
#partime_employee
#each class should calculate class diffently
class Employee(ABC):

    def __init__(self):
        self.name=input('enter your name')
        self.age=input('enter age')

    @abstractmethod
    def calculate_salary(self):
        pass


class Partime_employee(Employee):
    def __init__(self):
        self.hour=int(input('enter number of hours worked'))
        self.rate=int(input('enter the rate per hour'))
        self.days=int(input('enter the number of days present'))
    def calculate_salary(self):
        print('thr salary is ',self.hour*self.rate*self.days)

class Fulltime_employee(Employee):
    def __init__(self):
        self.hour=int(input('enter number of hours worked'))
        self.rate=int(input('enter the rate per hour'))
        self.days=int(input('enter the number of days present'))


    def calculate_salary(self):
        print('thr salary is ',self.hour*self.rate*self.days)

        
p=Partime_employee()
p.calculate_salary()


