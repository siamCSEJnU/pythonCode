year=input("enter the year you want to taste:")
year=int(year)
print(year,"is to justify whether it is leap year or not")
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("yes",year,"is a leap yaer")
        else:
            ("not the leap year")
    else:
        ("yes",year,"is a leap year")  
else:
    print("not the leap year")        
      
