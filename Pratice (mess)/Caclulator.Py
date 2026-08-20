print("Enter first number")
number1 = int(input())
print("Enter second number")
number2 = int(input())
print("Enter action you want to perform")
action = input()
def addition(a,b):
    return a + b
def substraction(a,b):
    return a - b
def multiplication(a,b):
    return a * b
def divide(a,b):
    return a / b
if action == "+":
    print(f" {number1} + {number2} = {addition(number1,number2)}")
elif action == "-":
    print(f" {number1} - {number2} = {substraction(number1,number2)}")
elif action == "*": 
    print(f"{number1} * {number2} = {multiplication(number1,number2)}")
elif action == "/":
    print(f"{number1} / {number2} = {divide(number1,number2)}")