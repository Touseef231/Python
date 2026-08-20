tries = 5
import random
computer = random.randint(1,100)
user = int(input("Guess"))
if user > computer:
    print("It's less")
    tries = tries - 1
elif user < computer:
    print("It's more")
    tries = tries - 1
while user != computer and tries >= 1:
    user = int(input("Guess"))
    if user > computer:
        print("It's less")
        tries = tries - 1
    elif user < computer:
        print("It's more")
        tries = tries - 1
if tries == 0:
    print("You lost")
    print(computer)