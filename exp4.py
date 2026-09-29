num=int(input('enter a number'))
for i in range(2,num):
    countt=1
    if num%i==0:
        break
    else:
        countt+=1
if countt==2:
    print(' prime')
else:
    print('not prime')
