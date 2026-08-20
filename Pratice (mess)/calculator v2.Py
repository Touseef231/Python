def addition(a,b):
    return a + b
def subtraction (a,b):
    return a - b
def multiplication(a,b):
    return a * b
def division (a,b):
    return a / b
option =6
while option != 5:
    print("===== Calculator V2=====",
    "1.Addition",
    "2.Subtraction",
    "3.Multiplication",
    "4.Division",
    "5.Exit",
    sep = "\n")
    option = int(input())
    if option >=1 and option <=4:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
    if option == 1:
        print(f"{num1} + {num2} = {addition(num1,num2)}")
    elif option ==2:
        print(f"{num1} - {num2} = {subtraction(num1,num2)}")
    elif option ==3:
        print(f"{num1} * {num2} = {multiplication(num1,num2)}")
    elif option ==4:
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print(f"{num1} / {num2} = {division(num1,num2)}")
    elif option ==5:
        print("Thanks for using this calculator, Bye!")
    else:
        print("Invalid option")