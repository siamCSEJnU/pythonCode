#find the numbers from 1 to 100 which is divisible by 5 and find the sum
result=0
for i in range(1,101):
    if i%5==0:
        print(i)
        result=result+i
print("the summation is:",result)        
