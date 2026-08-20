option = 100
player = {
    "name": "Touseef",
    "level": 1,
    "health": 10,
    "coins": 50
}
while option != 5 and player["health"] > 0:
    print("====== Player Manager ======",

"1. View Profile",
"2. Change Name",
"3. Add Coins",
"4. Take Damage",
"5. Exit",sep ="\n")
    print("What you want to do?")
    option = int(input())
    if option == 1:
        print(f"==== Player-Stats ====",f"Name: {player["name"]}",f"Level: {player["level"]}",f"Health: {player["health"]}",f"Coins: {player["coins"]}",sep ="\n")
    elif option == 2:
        print("Enter new name")
        newname = input()
        player["name"] = newname
        print("Name changed!")
    elif option == 3:
        print("How much coins you want to deposit")
        coinsdeposit = int(input())
        player["coins"] = player["coins"] + coinsdeposit
        print("Coins added successfuly")
    elif option == 4:
        print(f"From which thing you wanna take damage",f"1.Sword",f"2.Stick",f"3.Hand",sep = "\n")
        damagetool = int(input())
        if damagetool == 1:
            player["health"] = player["health"] - 5
            print("Boom! You got massive damage")
        elif damagetool == 2:
            player["health"] = player["health"] - 2
            print("Boom! but that was not bad as Sword")
        elif damagetool == 3:
            player["health"] = player["health"] - 0.5
            print("I don't even know if that was a damage")
        else:
            print("You're not even capable of choosing an option bruh")
        if player["health"] < 0:
            player["health"] = 0
    elif option == 5:
        print("Bye see you soon!")
    else:
        print("You can't even enter an option noob")
    if player["health"] == 0:
        print("Game Over")