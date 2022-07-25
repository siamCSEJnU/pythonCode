#write the code to find the greatest number
from email.errors import NonPrintableDefect


numbers = [6,1,3,0,9,3,2,5]
max=numbers[0]
for n in  numbers:
    if n>max:
        max=n
print(max)                
