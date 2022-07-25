#find the value of sum from 1 to n
result=0
n=input("enter the value of n:")
n=int(n)
for i in range(1,n+1):
    result=result+i
print("the sum from 1 to",n,"is",result)
