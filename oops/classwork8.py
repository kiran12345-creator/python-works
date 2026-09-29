#Create a class named Circle with an attribute radius. Use a constructor to initialize the radius by
# accepting input from the user. Define the following methods:
# getarea() – to calculate and display the area of the circle.
# getperimeter() – to calculate and display the perimeter (circumference) of the circle.
# Create an object of the Circle class and call both methods to display the results.
# class Circle:
#     def __init__(self):
#         self.r=int(input('enter the radius'))
#     def get_area(self):
#         area = (3.14 * self.r *self.r)
#         print("area is",area)
#     def perimeter(self):
#         perimeter= 2*3.14*self.r
#         print("perimeter is",perimeter)
# c1=Circle()
# c1.get_area()
# c1.perimeter()
# #
# 2.Create a class named Account with attributes acctnumber, acctname, and balance.
# Initialize these values using a constructor by taking input from the user. Define the following methods:
#
# withdraw() – to withdraw an amount from the account and update the balance.
# deposit() – to deposit an amount into the account and update the balance.
# showbalance() – to display the current balance of the account.
#
# Create an object of the class and call the methods to perform withdrawal and deposit operations and display the updated balance.
class Account:
    def __init__(self):
        self.acc_num=int(input("enter account number"))
        self.acc_name=(input('enter account name'))
        self.balance=int(input('enter bank balance'))
    def show_balance(self):
        print('remaining balance is : ',self.balance)
    def withdraw(self):
        amount=int(input('enter amount to be withdrawn : '))
        if amount < self.balance:
            self.balance=self.balance-amount
            self.show_balance()
        else:
            print("insufficent balance")
    def deposit(self):
        amount=int(input('enter amount to be deposited : '))
        self.balance+=amount
        self.show_balance()
a1=Account()
a1.show_balance()
a1.deposit()
a1.withdraw()


