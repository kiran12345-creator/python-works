#positive even or odd , negetive even or odd
num=int(input("enter a number"))
if num > 0:
    if num % 2==0:
        print(num,'is positive even number')
    else:
        print(num, 'is positive odd number')
else:
    if num % 2 == 0:
        print(num, 'is negative even number')
    else:
        print(num, 'is negative odd number')