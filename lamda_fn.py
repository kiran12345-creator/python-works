# # # # # sum of 2 num
# # # # # summ=lambda num1,num2:num1+num2
# # # # # print(summ(2,5))
# # # # #=============================================
# # # # # #product of two num
# # # # # product=lambda num1,num2:num1*num2
# # # # # print(product(2,3))
# # # # #==============================================
# # # # #length of a string
# # # # length=lambda strin:len(strin)
# # # # print(length('kiran'))
# # # #=================================================
# # # # # quare root of a number
# # # # square_root=lambda num:num**.5
# # # # print (int(square_root(36)))
# # # #================================================
# # # # #first letter of  a string
# # # # first=lambda string:string[0]
# # # # print(first('kiran'))
# # # #=================================================
# # # # #name value from dictionary
# # # # name=lambda dic:dic['name']
# # # # print(name({'name':'kiran'}))
# # # #==================================================
# # # # #salary value from dictionary
# # # d2={'name':'arun','salary':1200000}
# # # d={'name':'kiran','salary':1000000}
# # # s=lambda dic:dic['salary']
# # # s2=lambda dict:(dict['name'],dict['salary'])
# # # print(s(d))
# # # print(s2(d2))
# # # #==================================
# # # # #add 10 to a number
# # # # add=lambda num:num+10
# # # # print(add(10))
# #
# #
# # # l=[1,2,3,4]
# # # print(list(map(lambda x:x**2,l)))
# # #====================================================
# # #create a new list of cubes
# # l=[1,2,3,4]
# # print(list(map(lambda x:x**3,l)))
# # #================================================
# #square root
# l=[1,4,9,36,81,100]
# print(list(map(lambda x:x**.5,l)))


# #create a new list of cubes |=[1,2,3,4]
#
# #create a new list of square roots |=[25,36,81,100]
#
# #create a new list of lengths
# colors=['red','green','blue','yellow','black']
# print(list(map (lambda x:len(x),colors)))
#
# colors=['red',green',blue',yellow',black'] #create a new list of first characters #create a new list of last characters #create a new list of reverse of each
# colors=['red','green','blue','yellow','black']
# print(list(map( lambda x:x[0],colors)))
# elemnt
#
# #Given a list I=[23,78,12,56]
#
# #Add 10 to each element in the given sequence
# I = [23, 78, 12, 56]
# print(list(map(lambda x : x+10,I)))
#
# ##given a list of dictionaries
#
I=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
   {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
   {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}
    ]
print(list(map(lambda x:x['salary'],I)))
#
# #
#
# # # create a new list of emails