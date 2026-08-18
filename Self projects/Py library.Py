books = ["Python", "Math", "History","English","Islamiat"] 
userchoice = 10 
print("=====================") 
print(" ") 
print("     TS Library ") 
print(" ") 
print("=====================")
while userchoice != 4:
    count = 1 
    print(f"===== Library Manager =====",f"1. View Books",f"2. Add Book",f"3. Remove Book",f"4. Exit", sep = "\n") 
    print("What you want to do") 
    userchoice = int(input("")) 
    if userchoice == 1: 
        for items in books: 
            print(f" {count}. {items}") 
            count = count + 1 
    if userchoice == 2:
        print("Enter book to add:") 
        addbook = books.append(input("")) 
        print("Book Added!") 
    if userchoice == 3:
        print("Enter book to remove") 
        removebook = input("") 
        if removebook in books:
            print("Book removed!") 
        else: 
            print("Book name is invalid")
        if removebook in books:
            books.remove(removebook) 
    if userchoice == 4: 
        print("Bye have a good day!")