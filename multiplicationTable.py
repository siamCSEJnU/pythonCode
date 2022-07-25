#namta in bengali
print("enter the number of which the multiplication table will be built:")
n=input()                       #n=input("enter the number of which the multiplication table will be built:")
n=int(n)
i=1
while i<=10:
    print(n,"*",i,"=",n*i)
    i+=1
print("the multiplication table of ",n+1,"is")
for j in range(1,11,):
    print(n+1,"*",j,"=",(n+1)*j)
    j+=1