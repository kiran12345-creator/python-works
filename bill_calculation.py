#write a program to calculate electricity bill based on the following criteria
#units consumed per unit
#0-100        0 rs/units
#100-200      5rs/ units
# 200-300     10rs/units
#above 300    15rs/units

#_____________example___________________________________________________________
# if consumed unit is 325 then
# 0-100 =0rs/unit
#100-200= 5*100=500 rs
#200-300=10*100=1000rs
# 25*15=475
# total=1975

unit=int(input("consumed unit"))
if 0<=unit<=100:
    bill=0
elif 100<unit<=200:
    bill=0+(unit-100)*5
elif 200<unit<=300:
    bill=0+500+(unit-100)*10
elif unit>300:
    bill=0+500+1000+(unit-100)*15
else:
    print("invalid input")
print("bill is",bill)





