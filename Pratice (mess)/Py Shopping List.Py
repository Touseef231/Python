fchoice = 6
shopping_list = ["Milk","Bread","Flour","Egg","Apples"]
while fchoice != 3:
    numb = 1
    print ("===== Shopping List Manager =====")
    print (f"1. View Shopping List",f"2. Add item",f"3. Exit", sep ="\n")
    print ("Your choice?")
    fchoice = int(input(""))
    if fchoice == 1:
        print("==== Shopping-list ====")
        for items in shopping_list:
            print(f"{numb}. {items}")
            numb = numb + 1
    elif fchoice == 2:
        print("Enter item to add")
        shopping_list.append(input(""))
        print("Item added!")
    elif fchoice == 3:
        print("Ok bye! Thanks for using this program")
    else:
        print("Invalid choice!")
