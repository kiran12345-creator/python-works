class Person:
    def __init__(self):
        self.name=input("enter name")
        self.age=input('enter age')
        self.place=input('place')
    def show(self):
        print(self.name,self.age)
p1=Person()
p2=Person()
p3=Person()
p1.show()
p2.show()