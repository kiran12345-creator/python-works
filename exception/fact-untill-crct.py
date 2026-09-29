from math import factorial as f
while(True):
    try:
        num=int(input('enter a number'))
        result=f(num)
        print('factorial',result)
        break
    except:
        print("invalid input")
