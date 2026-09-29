try:
    num1=int(input('enter a number'))
    num2=int(input('enter second number'))
    s=num1/num2
except ZeroDivisionError:
    print('cannot divide by zero')
except NameError:
    print(' check name')
except ValueError:
    print('value error')
else:
    print('sum is :',s)
finally:
    print('finished execution')
