# #
# # def factor_num(num):
# #     for i in range(1,(num+1)):
# #         if num % i == 0:
# #             print(i)
# #     return(i)
# # #
# # factor_num(15)
#
# #ADD 2 NUMBERS FUNCTION  (function that takes 2 arguments and return sum)
# def sum_num(n1,n2):
#     s=0
#     s=n1+n2
#     print(s)
#     return(s)
# sum_num(23,34)
#-----------------------------------------------------------------------------------------------------------------

#SIMPLE INTEREST( insert 3 arguments and call a function dynamically)

# def simple_interest(n,p,r):
#     result=(n*p*r)/100
#     total=result+p
#     print(result)
#     print(f"the final amount after interest { total}")
#     return result
# p=int(input("enter the amount"))
# n=int(input("enter the time in years"))
# r=int(input("enter the rate"))
# simple_interest(n,p,r)

#------------------------------------------------------------------------------------------------------------------
#define a function that takes string and char as arguments and return the count of string and characters

def count_char(*args):
    count=0
    for i in a :
        if i==b:
            count+=1
    if count==0:
         return 'char not present'

    return count

a=input("ENTER A STRING  ")
b=input('enter the chr to be searched  ')
print(count_char(a,b))