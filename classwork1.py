  # question 1

s="I am learning python"
print("length of string is : ",len(s))
print("rev of string is  : ", s[::-1])
print("last char of string is : ",s[-1])
print("13th char of string is  : ",s[12])
print("string from index 2 to 15 is : ",s[2:16])
print(s + " programming")
#
#---------------------------------------------------------------------------------------------------------------#
#question2


s2="python is a programming language"
print(s2[10:])                                    #remove first 10 char
print("last 5 char in reverse ",s[-1:-6:-1])      #reverse
print("last 5 char ",s[-5:])                      #print last 5 char


#-----------------------------------------------------------------------------------------------------------------#
#question3

l=['Guitar','Piano','Violin','Drums','Flute']
l.append("veena")                #adding veena to the list
print(l)

#-----------------------------------------------------------------------------------------------------------------#
#question5

lis=["manthi","biryani","shwarma","noodles","sadya"]
lis.append("payasam")
print(lis)                        #list after adding payasam
lis[1]="burger"                   #replacing biryani with burger (index 2)
print(lis)
print(lis[-1])                    #last food item
print(len(lis))                   #number of food

#-----------------------------------------------------------------------------------------------------------------#
#question4
lis3=[10,56,23,67,19,70]
lis3[2],lis3[5]=lis3[5],lis3[2]     #using swap method to switch indexes(a,b=b,a)
print(lis3)

#-----------------------------------------------------------------------------------------------------------------#
#question6
sett={10,20,30,40}
sett.add(50)                       #adding 50 to set
print(sett)

