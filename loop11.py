terminate=True
while terminate:
    number1=input("enter the first number:")
    n1=int(number1)
    number2=input("enter the second number:")
    n2=int(number2)

    while True:
        command=input("enter the command add/sub or quit :")
        if command == "quit":
            terminate=False
            break
        if command in "add":
            print("the sum is:",n1+n2)
            terminate=False
            break
        if  command == "sub":
            print("the subtraction is:",n1-n2)
            terminate=False
            break
        if command not in ["add","sub"]:
            print("invalid operation or command and enter the valid command again")
            continue
              
