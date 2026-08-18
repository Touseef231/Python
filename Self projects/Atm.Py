Balance = 1000
Choice = 0
attempt = 3
code = int(input("Enter code:"))
if code <= 99:
    print("Too short")
elif code != 872:
    print("Wrong code")
while code != 872:
    print ( f"Try again:", sep = "\n")
    code = int(input(""))
    if code <= 99:
        print("Too short")
    elif code != 872:
        print("Wrong code")
while Choice != 4:
    print(f"Welcome to ATM",
    f"What's your choice Sir!",
    f"1. Check Balance",
    f"2. Deposit money",
    f"3. Withdraw money",
    f"4. Exit", sep="\n")
    Choice = int(input(f"Your choice?:"))
    if Choice == 1:
        print (f"Your Balance is {Balance}")
        print (f"Thanks for using this ATM")
    elif Choice == 2:
        print("How much you want to Deposit?")
        dd = int(input(""))
        if dd <= 0:
            print("invalid amount")
        else:
            print(f"Deposit Successful!",
            f"Your Balance is now {Balance + dd}",
            sep ="\n")
            Balance = Balance + dd
    elif Choice == 3:
        print(f"How much you want to Withdraw",)
        wt = int(input(""))
        if wt > Balance:
            print("Insufficent balance")
        else:
            print(f"Withdraw Successful!",
            f"Your balance is now {Balance - wt}",
            f"Thanks for using this ATM",
            sep ="\n")
            Balance = Balance - wt
    elif Choice == 4:
        print("Thanks for coming ")
    else:
            print("Wrong Choice!")