# 1.Write a program that prints all numbers between 1 and 100 that are divisible by 3 or 5
# for i in range(1,101):
#     if i % 3 ==0 and i % 5==0:
#        print(i,end=" ")

#-----------------------------------------------------------------------------------------------
#2.Print the cumulative sum of a list.
# # Example: [1, 2, 3, 4] → Output: [1, 3, 6, 10]

# limit=int(input("enter the number of elemnts in the list"))
# l=[]
# for i in range(1,limit+1):
#     num=int(input("enter the element to be inserted"))
#     l.append(num)
# print(l)
# summ=0
# new=[]
# for i in l:
#      summ=summ+i
#      new.append(summ)
# print(new)
#-------------------------------------------------------------------------------------------------
# # 3.Given two numbers a and b, calculate the sum of all numbers between them (inclusive). Use a for loop.
# # Example: a = 3, b = 7 → Output: 25

# num1=int(input('enter first number'))
# num2=int(input('enter second number'))
# summ=0
# for i in range(num1,num2+1):
#     summ+=i
# print(summ)

#--------------------------------------------------------------------------------------------------
#4. SUM OF ELEMENTS AT EVEN POSITION IN A LIST

# limit=int(input("enter the number of elements in the list"))
# l=[]
# for i in range(1,limit+1):
#     num=int(input("enter the element to be inserted"))
#     l.append(num)
# print(l)
# summ=0
# new=[]
# for i in range(0,len(l),2):
#     summ=(summ+l[i])
# print(summ)

#--------------------------------------------------------------------------------------------------

#5. Given a list, sum the elements until a 0 is encountered (stop at 0).

# l=[4,9,1,0,6,7]
# summ=0
# for i in l:
#     if i==0:
#         break
#     else:
#         summ+=i
# print(summ)

#---------------------------------------------------------------------------------------------------

#6.Loop from 1 to 1000 and find the first number divisible by both 7 and 11. Use break to stop once found.

# for i in range(1,1001):
#     if i%7==0 and i%11==0:
#         print(i)
#         break
#-----------------------------------------------------------------------------------------------------

# 7.Given a list of strings, print only those with length ≥ 5. Use continue to skip shorter ones.

# l=['able','sherin','kiran','alphy','anu','amal']
# for i in l:
#     if len(i)>=5:
#         print(i,end=" ")
#     else:
#         continue

#--------------------------------------------------------------------------------------------------------

# 8.From a list of numbers, create a new list containing the squares of each element.
# Input: [1, 2, 3] → Output: [1, 4, 9]


#l=[1,2,3,4]
# new=[]
# for i in l:
#     new.append(i**2)
# print(new)

#----------------------------------------------------------------------------------------------------------

# 9.Given a string, construct a new string with all vowels removed using a loop.
# Input: "hello world" → Output: "hll wrld"

# s=input('enter anything')
# check="aeiouAEIOU"
# new=''
# for i in s:
#     if i in check:
#         continue
#     else:
#         new+=i
#
# print(new)

#--------------------------------------------------------------------------------------------------------
# # 10.Given a list of numbers, create a new list where each number is doubled, but stop if any doubled number is greater than 50 (use break).
# l=[5,1,2,48,50,8,6,2]
# new=[]
# for i in l:
#     if i*2 < 50:
#         new.append(i*2)
#     else:
#         continue
# print(new)
#--------------------------------------------------------------------------------------------------------

# 11.From a string containing mixed characters, create a new string containing only digits.
# Input: "abc123x7z" → Output: "1237"
# s=input("enter string")
# test="1234567890"
# new=""
# for i in s :
#     if i in test:
#         new=new+i
# print(new)

#-------------------------------------------------------------------------------------------------------

# 12.Given a list of strings, create a new list containing the length of each string.
# Input: ["cat", "banana", ""] → Output: [3, 6, 0]

# limit=int(input('enter the size of list'))
# l=[]
# for i in range(limit+1):
#     s=input("enter elemnts of the list")
#     l.append(s)
# print(l)
# new2=[]
# for ch in l:
#     new2.append(len(ch))
# print(new2)

#---------------------------------------------------------------------------------------------------------
# 13.Given a list of words, create a string made of the first letter of each word.
# Input: ["Python", "Is", "Great"] → Output: "PIG"

# l=["Python", "Is", "Great"]
# new=''
# for i in l:
#     print(i[0],end='')

#--------------------------------------------------------------------------------------------------------


# 14.Replace Negative Numbers with 0
# Given a list of integers, create a new list where all negative numbers are replaced with 0.
# # Input: [4, -3, 2, -1] → Output: [4, 0, 2, 0

# l=[4, -3, 2, -1]
# # for i in l:
# #     if i <0:
# #         l[i]=0
# # print(l)

#--------------------------------------------------------------------------------------------------------

# 15.
# d={101:['Arun',23,'ekm'],
#      102:['Amal',25,'tvm'],
#      103:['Anu',26,'tcr'],
#       104:['Kiran',27,'ekm']}
#
# #print all names of students

# d={101:['Arun',23,'ekm'],
#     102:['Amal',25,'tvm'],
#     103:['Anu',26,'tcr'],
#     104:['Kiran',27,'ekm']}
# for i in d.values():
#     print(i[0])

#-------------------------------------------------------------------------------------------------------
 #16.Write a program to print the numbers from 1 to 100.
# But for multiples of:
#
# 3, print “Fizz” instead of the number
#
# 5, print “Buzz” instead of the number
#
# Both 3 and 5, print “FizzBuzz”
#
# for i in range(1,101):
#     if 1%5==0 and i%3==0:
#         print('FizzBuzz')
#     elif i%5==0:
#         print('Buzz')
#     elif i%3==0:
#         print('Fizz')
#     else:
#         print(i)

#----------------------------------------------------------------------------------------------------
# 17.Write a Python program that prints numbers from 1 to 50:
#     Skip multiples of 5 using continue
#     Stop the loop if the number becomes greater than 40 using break

# for i in range(1,51):
#     if i%5==0:
#         continue
#     elif i>40:
#         break
#     else:
#         print(i)

#-------------------------------------------------------------------------------------------------------

# 18.Write a program to find
#     Reverse of a number(without[::-1])
#     count the number of digits in a given number
#     sum of digits in  a number

num=(input("enter a number"))
rev=''
summ=0
for i in num:
    rev=i+rev
    summ = summ + int(i)
print(f"reverse is {rev}")
print(f"number of digits is {len(num)}")

print(summ)
















