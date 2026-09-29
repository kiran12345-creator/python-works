# # # i=1
# # # product=1
# # # while i<=5:
# # #     product=product*i
# # #     i+=1
# # # print(product)
# # i=1
# # product = 1
# # while i <= 50:
# #     if i % 3==0:
# #         product=product*i
# #     i+=1
# # print(product)
# i=1
# product=1
# while i <=50:
#     s=str(i)
#     if '3' in s:
#         product=product*int(s)
#     i+=1
# print(product)
# fact=1
# num=int(input("enter a number"))
# i=1
# while i <= num:
#     fact*=i
#     i+=1
# print(fact)

#multiplication table of a number upto 10
num=int(input("enter a number"))
i=1
while i<=10:
    p=num*i
    #print(f"{num} x {i} = {num*i}")
    print(i,"x",num,'=',p)
    i+=1


