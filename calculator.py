num1=int(input("enter first number"))
num2=int(input("enter second number"))
op=input("enter an operator")
if op=="+":
    print("result is",num1+num2)
elif op=="-":
    print("result is",num1 - num2)
elif op =="/":
    print("result is",num1 / num2)
elif op=="*":
    print("result is",num1 * num2)
elif op=="//":
    print("result is",num1 // num2)
elif op == "%":
    print("result is", num1 % num2)
else:
    print("invalid input")
