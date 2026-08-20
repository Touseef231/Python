username = input("Enter your desired username: ")
password = input("Set your account password: ")
while len(password) < 6:
    print("Weak password")
    username = input("Enter your desired username: ")
    password = input("Set your account password: ")
if 6 <= len(password) <= 10:
    print("Good password")
else:
    print("Absolute security")
username1 = 0
password1 = 0
username1 = input("Enter you username: ")
password1 = input("Enter your password: ")
if username1 == username and password1 == password:
    print("You're authorized")
else:
    print("You're unauthorized wrong username or password!")