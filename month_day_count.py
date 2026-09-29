l1=['January','March','may','july','august','October','December']
l2=['April','June','September','November']
l3=['February']
month=input("enter a month")
if month in l1:
    print(f"{month} has 31 days")
elif month in l2:
    print(f"{month} has 30 days")
else:
    print(f"{month} has 28/29 days")

