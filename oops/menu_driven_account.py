class Account:
    def __init__(self):
        self.acc_num=int(input("enter account number"))
        self.acc_name=(input('enter account name'))
        self.balance=int(input('enter bank balance'))
    def show_balance(self):
        print(self.balance)
    def wthdraw(self):
        amount=int(input('enter amount to be withdrawn'))
        if amount < self.balance:
            self.balance=self.balance-amount
            self.show_balance()
        else:
            print("insufficent balance")
    def deposit(self):
        amount=int(input('enter amount to be deposited'))
        self.balance+=amount
        self.show_balance()

l=[]
while(True):
     print('CLASS OPERATIONS')
     print('1. create new account')
     print("2. deposit")
     print('3.withdraw')
     print('4,show balance')
     print('5.exit')

     ch=int(input('enter your choice'))


     if ch==1:
         a=Account()
         l.append(a)
         print(l)
     elif ch==2:
         deposit=int(input('enter acc num '))
         for i in l:
             if i.acc_num==deposit:
                 i.deposit()
                 break
         else:
             print('account not found')
     elif ch==3:
         withdraw=int(input('enter acc num'))
         for i in l:
             if withdraw==i.acc_name:
                 i.withdraw()
                 break
         else:
             print('account not found')






