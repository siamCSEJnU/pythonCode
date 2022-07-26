#write a code to get square of any number except to 0
#we will use break and continue

"""while True:
    n=input("enter a number:")
    n=int(n)
    if n==0:
        print("invalid")
        break
    print("the square of the number",n,"is",n*n)"""

#write a code to get the square of any numbers except to negative numbers

while True:
    n=input("enter just positive number:")
    n=int(n)
    if n<0:
        print("this is invalid")
        continue
    if n==0:
        print("this is invalid")
        break
    print("the square of the number",n,"is",n*n)
