weight = (input("Tell you weight in kg: "))
if weight.isdigit() :
    weight=float(weight)
    weight_valid = True
else:
    print("Invalid weight")
    weight_valid = False
height = (input("Tell you height in meters: "))
if height.isdigit():
    height = float(height)
    height_valid = True
else:
    print("Invalid height")
    height_valid = False    

if height_valid and weight_valid:
    bmi = weight / (height ** 2)
    print(f"Your Body Mass Index is {bmi}")
    if bmi < 18.5:
        print("You're underweight")
    elif bmi <= 24.9:
        print("You're healthy")
    elif bmi >=25.0:
        print("You're overweight")
else:
    print("You enetered wrong height or weight or both")