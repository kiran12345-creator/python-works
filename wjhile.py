# # # # # # # # # # # # write a program to print first 10 integers
# # # # # # # # # # # # i=1
# # # # # # # # # # # # while i <= 10:
# # # # # # # # # # # #
# # # # # # # # # # # #     print(i,end=", ")
# # # # # # # # # # # #     i+=1
# # # # # # # # # # #    # write a program to print first 10 even numbers
# # # # # # # # # # i=1
# # # # # # # # # # while i<=16:
# # # # # # # # # #    print (i,end=", ")
# # # # # # # # # #    i+=3
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # i=10
# # # # # # # # # while i<=80:
# # # # # # # # #    print (i,end=", ")
# # # # # # # # #    i+=10
# # # # # # # # i=3
# # # # # # # # while i<=21:
# # # # # # # #    print (i,end=", ")
# # # # # # # #    i+=3
# # # # # # # i=5
# # # # # # # while i>0:
# # # # # # #    print (i,end=", ")
# # # # # # #    i-=1
# # # # # # i=8
# # # # # # while i>=0:
# # # # # #    print (i,end=", ")
# # # # # #    i-=2
# # # # # i=1000
# # # # # while(i < 10000):
# # # # #     print(i)
# # # # #     i+=1
# # # # i=1000
# # # # while i<9999:
# # # #     s=str(i)
# # # #     if "3" in s :
# # # #         print(s)
# # # #     i+=1
# # # #
# # # #
# # # i=1
# # # while i<=100:
# # #     if(i % 3==0 and i % 5==0):
# # #         print(i)
# # #     i+=1
# # #
# # i=1
# # while i <=10:
# #     print(i**2,end=" ")
# #     i+=1
# i=100
# s=str(i)
# while i < 1000:
#     if "3" in s:
#         print(s)
#     i+=1
count=0
i=1
while i<=50:
    if i%3==0:
        count+=1
    i+=1
print(count)
