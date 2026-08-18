def greater(a,b):
    if a > b:
        print(f"{a} > {b}")
    elif a < b:
        print(f"{a} < {b}")
    else:
        print(f"{a} = {b}")

greater(int(input("Enter first number")), int(input("Enter second number")))
