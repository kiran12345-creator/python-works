class Parent:
    def m1(self):
        print("parent method 1")
    def m2(self):
        print('parent method 2')
class Child(Parent)   :
    def m1(self):
        super().m1()
        print('in child m3')
    pass
c1=Child()
c1.m1()
c1.m2()
