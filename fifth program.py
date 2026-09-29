# #qn1  write a pgm to display a number if the number is divisible by 3
# #qn2  write a pgm to display a number if the number is divisible by 7 and 5
# #qn3 write a pgm to display a name if name contains letter "n"
# #qn4 write a pgm to display a name if name starts with letter "A"
#
# #---------------------------------------------------------------------------------------------------------------
# #answer1
#
# # #num=int(input("enter a number"))
# # if num % 3 == 0:
# #     print(num)
#
# #---------------------------------------------------------------------------------------------------------------
# #answer2
# # num=int(input("enter a number"))
# # if (num % 7 == 0) and (num % 5==0):
# #     print(num)
#
# #---------------------------------------------------------------------------------------------------------------
# #answer3
# # name=input("enter your name : ")
# # if "n" in name:
# #     print(name)
#
# #---------------------------------------------------------------------------------------------------------------
# #answer4
#
# name=input("enter your name : ")
# if  name[0] in ("A" or "a"):
#    print(name)



num=int(input("enter a number : "))
if num>0:
   print("positive")
else:
    print("negative")