# # # # # # # # #1 write a program to find the position of a specific character in a string
# # # # # # # #
# # # # # # # # # s=input('enter a string')
# # # # # # # # # key=input('enter character to be searched')
# # # # # # # # # if key in s:
# # # # # # # # #     print(f'the position of {key} is {s.index(key)}')
# # # # # # # # # else:
# # # # # # # # #     print(f'{key} is not in the given string')
# # # # # # # # #----------------------------------------------------------------------------------------------------
# # # # # # # # #2 write a program to find the count of specific character in the string
# # # # # # # # # s=input('enter a string')
# # # # # # # # # key=input('enter character to be counted')
# # # # # # # # # if key in s:
# # # # # # # # #     print(f'the count of {key} is {s.count(key)}')
# # # # # # # # # else:
# # # # # # # # #     print(f'{key} is not in the given string')
# # # # # # # # #------------------------------------------------------------------------------------------
# # # # # # # # #3 write a program to create a new dictionary where keys are letters and values are count of each other
# # # # # # # # # s=input('enter a string')
# # # # # # # # # new={}
# # # # # # # # # for ch in s:
# # # # # # # # #     new[ch]=s.count(ch)
# # # # # # # # # print(new)
# # # # # # # # # #---------------------------------------------------------------------------------------
# # # # # # # #
# # # # # # # # #4 program to create a new list with 5 random 3 digit number
# # # # # # # # # import random
# # # # # # # # # new=[]
# # # # # # # # # num=0
# # # # # # # # # for i in range (1,6):
# # # # # # # # #     num=random.randint(100,999)
# # # # # # # # #     new.append(num)
# # # # # # # # # print(new)
# # # # # # # # #-----------------------------------------------------------------------------------------
# # # # # # # #
# # # # # # # #
# # # # # # # # #5  program to create 5 digit otp number
# # # # # # # # # import random
# # # # # # # # # num=random.randint(10000,99999)
# # # # # # # # # print(num)
# # # # # # # # #-----------------------------------------------------------------------------------------
# # # # # # # #
# # # # # # # # #6 count of letters,spaces,digits and a string
# # # # # # # # # s=input('enter anything')
# # # # # # # # # letter_count=0
# # # # # # # # # space_count=0
# # # # # # # # # digit_count=0
# # # # # # # # # for ch in s:
# # # # # # # # #     if ch.isalpha():
# # # # # # # # #         letter_count+=1
# # # # # # # # #     elif ch.isdigit():
# # # # # # # # #         digit_count+=1
# # # # # # # # #     elif ch.isspace():
# # # # # # # # #         space_count += 1
# # # # # # # # # print(f'letter count is {letter_count}')
# # # # # # # # # print(f"digit count is {digit_count}")
# # # # # # # # # print(f"space count is {space_count}")
# # # # # # # # #------------------------------------------------------------------------------------------
# # # # # # # # #program to create a new dictionary where keys are words and values are length of words
# # # # # # # # s="python coding is easy and fun"
# # # # # # # # new=s.split()
# # # # # # # # new_dic={}
# # # # # # # # for words in new:
# # # # # # # #     new_dic[words]=len(words)
# # # # # # # # print(new_dic)
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # # given a list
# # # # # # # l=[1,1,2,3,4,5,5,5,6,7]
# # # # # # # #create a dictionary where keys are numbers and values are count of each nmber
# # # # # # # d={}
# # # # # # # for i in l:
# # # # # # #     d[i]=l.count(i)
# # # # # # # print(d)
# # # # # # l=[34,12,56,89,90,11]
# # # # # # #largest,2nd largest,smallest,2nd smallest
# # # # # # largest=max(l)
# # # # # # smallest=min(l)
# # # # # # l.sort()
# # # # # # l2=l.copy()
# # # # # # second_smallest=l2[1]
# # # # # # second_largest=l2[-2]
# # # # # # print(largest,smallest,second_smallest,second_largest)
# # # # #
# # # # # l=[['arun',23,40000],['amal',24,50000],['anu',27,30000]]
# # # # # name=[]
# # # # # age=[]
# # # # # salary=[]
# # # # # for i in l:
# # # # #       name.append(i[0])
# # # # #       age.append(i[1])
# # # # #       salary.append(i[2])
# # # # # print(max(salary))
# # # # # print(min(age))
# # # # #
# # # # #
# # # # #given a list 1: remove duplicates with set and without set
# # # # l=[1,1,1,2,3,3,4,5,]
# # # # print(set(l))
# # # # new=[]
# # # # for i in l:
# # # #     if i not in new :
# # # #         new.append(i)
# # # # print(new)
# # # #
# # # #
# # # # # given list find common elements
# # # # l1=[23,45,78,90,12,74]
# # # # l2=[45,89,23,56,34]
# # # # l1=set(l1)
# # # # l2=set(l2)
# # # # print(l1.intersection(l2))
# # # #
# # # # define a function that takes a list of numbers  as arguments and print the count of even numbers , odd numbers whose value is grater than 50
# # # def count_sum(l):
# # #     count_odd=0
# # #     count=0
# # #     count_50=0
# # #     for i in l:
# # #         if i%2==0 :
# # #             count+=1
# # #         elif i%2==1 :
# # #             count_odd+=1
# # #         if i>50:
# # #             count_50+=1
# # #     else:
# # #         pass
# # #     return count,count_odd,count_50
# # # # l=[23,56,12,78,98,89,31,67]
# # # print(count_sum(l))
# # #-----------------------------------------------------------------------------------------------------------------
# #
# #
# # # define a function that takes a list of numbers  as arguments and return a new list of lengths
# #
# # def len_list(*args):
# #     new=[]
# #     for ch in l:
# #         new.append(len(ch))
# #     return new
# # l=['red','green','yellow','orange','blue']
# # print(len_list(l))
# #----------------------------------------------------------------
# #define a function that takes a number as argument and eturn its square
#
# s=lambda num : num**2
# print(s(9))
#====================================================================================================
# lamda fn to find  cube of a number
cube=lambda num:num**3
print(cube(3))