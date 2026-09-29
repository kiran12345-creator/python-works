# # Q.Write Python Programs Using map(), filter(), or reduce()
#
# # 1.Capitalize all names in a list
# # names = ['alin', 'arun', 'anu']
# # print(list(map(lambda x:x.capitalize(),names)))
# #======================================================================================
#
# #
# # 2.Append "@gmail.com" to a list of usernames
# # users = ['user1', 'user2']
# # print(list(map(lambda x:x +"@gmail.com",users)))
# #=====================================================================================
#
# # 3.Filter out all empty strings from a list
# # words = ['hello', ' ', 'world', ' ', 'python']
# # print(list(filter(lambda x:x!=" " ,words)))
# #=====================================================================================
#
#
# # 4.Filter names that start with the letter 'A'
# # names = ['Anu', 'Neenu', 'Arun', 'Ravi']
# # print(list(filter(lambda x:x.startswith('A'),names)))
# #=====================================================================================
#
#
# # 5.Concatenate all strings in a list
# # words = ['Python', 'is', 'fun']
# # import functools
# # print(functools.reduce(lambda a,b:a+b,words))
# #=======================================================================================
#
#
# # 6.Multiply all numbers in a list
# # nums = [2, 3, 4]
# # import functools
# # print(functools.reduce(lambda a,b:a*b,nums,1))
# #======================================================================================
#
#
# # 7.Extract First Character of Each Word
# # words = ["apple", "banana", "cherry"]
# # print(list(map(lambda x:x[0],words )))
# #=======================================================================================
#
#
# # 8.Add 10 to Each Number
# # nums = [5, 10, 15]
# # print(list(map(lambda x:x+10,nums)))
# #=======================================================================================
#
#
# # 9.Given a list
# # l=[12,-4,78,-34,90,45,16,26,-2,-11,3]
# # import functools
# #     # #Sum of positive even numbers
# # print(functools.reduce(lambda a,b:a+b if b%2==0 and b>0 else a,l,0 ))
# #
# #     # #Sum of Positive Odd numbers
# # print(functools.reduce(lambda a,b:a+b if b%2==1 and b>0 else a,l,0 ))
# #
# #     # #Sum of Negative  odd numbers
# # print(functools.reduce(lambda x,y:x+y if y%2==1 and y<0 else x,l,0))
# #
# #     # #Sum of Negative Even numbers
# # print(functools.reduce(lambda x,y:x+y if y%2==0 and y<0 else x,l,0))
# #
# #     # #Count of Positive numbers
# # print(functools.reduce(lambda x,y:x+1 if y>0 else x,l,0))      # x acts like a counter
# #
# #     # #Count of negative numbers
# # print(functools.reduce(lambda x,y:x+1 if y<0 else x , l,0))
#
#
# #============================================================================================
# # 10.Given a list
# # Convert all Strings to Integers [1,2,3,4]
# # nums = ["1", "2", "3", "4"]
# # print(list(map(lambda x:int(x),nums)))
# #============================================================================================
#
# # 11.
# p= [{'name':'laptop','price':50000},
#     {'name':'phone','price':20000},
#     {'name':'watch','price':3000},
#     {'name':'Tablet','price':25000}]
#
# #print list of product names in Uppercase
# # print(list(map(lambda x:x['name'].upper() ,p)))
#
# #print products with price greater than 10000
# result=(list(filter(lambda x: x['price']> 10000,p)))  #filters the list above 10000
# print(list(map(lambda x:x['name'],result)))           #return the filtered names
#
# #Find the total price of all products
# import functools
# print(functools.reduce(lambda x,y:x+y['price'],p,0))

# p= [{'name':'laptop','price':50000},
#      {'name':'phone','price':20000},
#      {'name':'watch','price':3000},
#      {'name':'Tablet','price':25000}]
# result=list(filter(lambda x:x['price'] > 10000 ,p))
# print(result)
# print(list(map(lambda x:x['name'],result)))