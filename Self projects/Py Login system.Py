username = "admin"
password = "1234"
print("==== Login-System ====")
print("1. Login")
print("2. Exit")
s1 = int(input(""))
if s1 == 1:
    s2 = input("Username:")
    s3 = input("Password")
    if s2 == "admin" and s3 == "1234":
        print("You're Authorized")
    else:
        print("You're Unauthorized")
elif s1 == 2:
    print("Thanks for using this program")
else:
    print("Wrong Option")