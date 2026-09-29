# #write a program to find BMI(Body Mass Index)
# #
# # BMI= weight in (kg)/ height**2 in (m)
# #
# #
# # BMI	                 Status
# # ≤ 18.4	             Underweight
# # 18.5 - 24.9	         Normal
# # 25.0 - 39.9	         Overweight
# # ≥ 40.0	             Obese
#
# #2.# A toy vendor supplies three types of toys:
#
# # Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.
#
# # The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.
#
# # On orders of more than Rs. 100 for key-based toys,a discount of 5% is given,
#
# # and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.
#
# # Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.
#
# # Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.
#
#
# #3 FIZZBUZZ PRoblem
#
# # if divisible by 3 only -print fizz
# # if divisible by 5 only -print buzz
# # if a number is divisible by 3 and 5
# #     print fizzbuzz#
# #-----------------------------------------------------------------------------------

#question 1


# # weight=int(input("enter the weight"))
# # if weight <=18.4:
# #     print("underweight")
# # elif 18.5<= weight <=24.9:
# #     print("Normal")
# # elif 25.0 <= weight <=39.9:
# #     print('Overweight')
# # elif weight>=40.0:
# #     print('Obese')
# # else:
# #     print("invalid input")
#
# #----------------------------------------------------------------------------------

#qn-2

# toy_code=int(input("enter toy code"))
# amount= int(input("enter the amount spend  "))
# offer_amount=0
# if toy_code==1:
#     if amount >=1000:
#        offer_amount=amount-(amount*10)/100
#        print(offer_amount)
#     else:
#         print('price is ', amount)
# elif toy_code == 2:
#     if amount >= 100:
#        offer_amount=amount-(amount*5)/100
#        print(offer_amount)
#     else:
#         print('price is ', amount)
# elif toy_code==3:
#     if amount >=500:
#        offer_amount=amount-(amount*10)/100
#        print(offer_amount)
#     else:
#         print('price is ', amount)
# else:
#     print("invalid input")
#
#
#
#
# ---------------------------------------------------------------------------------------

#question3

# num=int(input("enter a number"))
# if num %3==0 and num%5!=0:
#     print("Fizz")
# elif num%5==0 and num %3!=0:
#     print("Buzz")
# elif num%3==0 and num%5==0:
#     print('FizzBuzz')
# else:
#     print("invalid input")
