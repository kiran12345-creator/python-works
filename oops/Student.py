#define a class named student with attributes rollnum,name,mark1,mark2,mark3
#method display to display mark and rollnumber
class Student:
    def __init__(self):
        self.name=input('enter name ')
        self.roll=input("enter roll number ")
        self.mark1 = int(input('enter mark1 :'))
        self.mark2 = int(input('enter mark2 :'))
        self.mark3 = int(input('enter mark3 :'))
    def display(self):
        print(self.name,'\n','roll number:',self.roll)
        total=(self.mark1+self.mark2+self.mark3)
        print("total mark is ", total,  " out of 30", )
s1=Student()
s2=Student()
s1.display()