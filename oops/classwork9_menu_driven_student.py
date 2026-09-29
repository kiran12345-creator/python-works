class Student:
    def __init__(self):
        self.name = input('enter name')
        self.roll_no=int(input('enter roll number :'))
        self.mark=int(input('enter mark'))
    def update_mark(self):
        new=int(input('enter new mark'))
        self.mark=new
        print('updated mark is ',self.mark)
    def display_details(self):
        print('roll no: ',self.roll_no)
        print('name: ',self.name)
        print('mark',self.mark)


l=[]
while(True):
    print('1.add student ')
    print('2.update marks')
    print('3.display all student details')
    print('4.search by roll  number')
    print('5.delete student')
    print('6.exit')

    ch = int(input('enter your choice'))

    if ch==1:
        a=Student()
        l.append(a)
        print(l)
    elif ch==2:
        new=int(input('enter roll number of student whose mark need to be updated'))
        for i in l:
            if i.roll_no == new:
                i.update_mark()
                break
        else:
            print('student not found')
    elif ch==3:
        for i in l:
            i.display_details()
    elif ch==4:
        key=int(input('enter roll number to be searched'))
        for i in l:
            if i.roll_no==key:
                print(i.name)
        else:
             print('student not found')
    elif ch==5 :
        num=int(input('enter roll number tobe deleted'))
        for i in l:
            if i.roll_no==num:
                l.remove(i)
                break
        else:
            print('invalid request')
    elif ch==6:
        exit()









