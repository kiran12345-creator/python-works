while(True):
    try:
       print('1.Addition')
       print('2.subtraction')
       print('3.multiplication')
       print('4.division')
       print('5.exit')


       ch = int(input('enter your choice'))
       if ch in [1,2,3,4,]:
           num1 = int(input('enter first number'))
           num2 = int(input('enter second number'))
           p=num1+num2
           q=num1-num2
           r=num1*num2
           s=num1/num2

    except ZeroDivisionError:
        print('cannot divide by zero')
    except ValueError:
        print('input error')
    else:
        if ch == 1:
            print(p)
        elif ch == 2:
            print(q)
        elif ch == 3:
            print(r)
        elif ch == 4:
            print(s)
        elif ch == 5:
            exit()






