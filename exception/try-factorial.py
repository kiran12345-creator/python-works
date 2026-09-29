try:
    from math import factorial as f
    num=int(input('enter a number'))
    result=f(num)
except ValueError:
    print('valur error')
except :
    print('invalid input')
else:
    print('factorial is',result)
finally:
    print('code finished')


