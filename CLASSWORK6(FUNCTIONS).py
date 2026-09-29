# Q1.Define a function that takes 2 numbers and returns their product

# def product(n1,n2):
#     p=n1*n2
#     return p
# n1=int(input('enter a number'))
# n2=int(input('enter a number'))
# print(product(n1,n2))#
#---------------------------------------------------------

#Q2.Define a function that takes a string and returns number of vowels

# def count_vowel(text):
#     test='aeiouAEIOU'
#     count=0
#     for ch in text:
#         if ch in test:
#             count+=1
#     if count == 0:
#         return 'no vowel found'
#     return count
# text=input('enter a string')
# print(count_vowel(text))
#-------------------------------------------------------------

 # Q3.Define a function that takes length and breadth and returns area of rectangle

# def area():
#      l=int(input('enter the length'))
#      b=int(input('enter the breadth'))
#      area=l*b
#      return area
# print(area())

#--------------------------------------------------------------


# # Q4.Define a function that takes a list of numbers and creates a new list
# # with even numbers and returns the new list
# l=[45,78,90,12,35]

# def even_list():
#     l=[]
#     l2=[]
#     limit=int(input("enter limit"))                           #to get size of list
#     for i in range(limit):
#         element=int(input("enter the elemnt of list"))        #inserting elements into list
#         l.append(element)
#     for num in l :
#         if num %2 ==0:                                         #checking whether even
#             l2.append(num)
#     return l2
# print(even_list())
#

#-----------------------------------------------------------------------------------
# #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]


# def sum_digit_list():
#     l=[]
#     l2=[]
#
#     limit=int(input("enter limit"))                           #to get size of list
#     for i in range(limit):
#         element=int(input("enter the elemnt of list"))        #inserting elements into list
#         l.append(element)
#     for num in l:
#         summ = 0
#         while num != 0:                                  ##    sum
#             digit=num%10                                 #     of
#             summ+=digit                                  #     digits
#             num//=10                                     #     logic
#         l2.append(summ)
#     return l2
# print(sum_digit_list())


#--------------------------------------------------------------------------------------------
#Q6.Define a function that takes a list and returns a new list containing unique elemnets from the given
# list
# l=[12,34,78,12,67,34,90,23]


#




#def unique_list(l):
#     l2 = []
#     for num in l:
#         if num not in l2:
#              l2.append(num)
#         else:
#             continue
#     return l2
# l=[12,34,78,12,67,34,90,23]
# print(unique_list(l))

#-----------------------------------------------------------------------------------------------------------
#Q7.Define a function that takes 2 list as arguments and returns a new list containing common elements
# list1=[12,34,56,78,90]
# list2=[90,34,11,57,45]


# def common_list(list1,list2):
#     new=[]
#     for i in list1:
#         if i in list2:
#             new.append(i)
#
#     return new
# list1=[12,34,56,78,90]
# list2=[90,34,11,57,45]
# print(common_list(list1,list2))
