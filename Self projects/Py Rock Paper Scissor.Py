print ("=== Rock Paper Scissor ===")
print("Choose Rock or Paper or Scissor")
def ccomputer():
    print("Computer Won")
def user():
    print("User Won")
User = input("")
import random
computer = random.choice(["Rock","Paper","Scissor"])
print(f"Computer chooses:{computer}")
if User == "Rock" and computer == "Scissor":
    user()
elif User == "Scissor" and computer == "Rock":
    ccomputer()
elif User == "Rock" and computer == "Paper":
    ccomputer()
elif User == "Paper" and computer == "Rock":
    user()
elif User == "Scissor" and computer == "Paper":
    user()
elif User == "Paper" and computer == "Scissor":
    ccomputer()
elif  User == "Rock" and computer == "Rock":
    print("Same choices")
elif  User == "Scissor" and computer == "Scissor":
    print("Same choices")
elif  User == "Paper" and computer == "Paper":
    print("Same choices")
else:
    print("Fix your typing noob")