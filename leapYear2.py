
year=input("enter the year you want to taste:")
year=int(year)
if year%4==0 and year%100!=0:
    print(year,"is a leap year")
elif year%100==0 and year%400==0:
    print(year,"is a leap year")
else:
    print("no")
