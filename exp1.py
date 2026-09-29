#check whether a number is divisible by 2 and 3 , and divisible by 2 and not by 3 divisible by 3 and not by 2
 #not divisible by 2 and 3
num=int(input("enter a number"))
if num % 2==0 :
    if num % 3==0:
        print("divisible by 2 and 3")
    else:
        print("divisible by 2 and not by 3")
elif num % 3==0 :
    if num % 2==0:
        print("divisible by 2 and 3")
    else:
        print("divisible by 3 and not by 2")
else:
    print("not divisible by 3 and 2")


