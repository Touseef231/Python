from datetime import datetime
option =11
money = 10000000
cars = [
    {"brand": "Toyota", "model": "Corolla", "price": 4500000},
    {"brand": "Honda", "model": "Civic", "price": 5500000},
    {"brand": "BMW", "model": "M3", "price": 12000000}
]
def show_car():
    count = 1
    for car in cars:
        print(f" {count}.Brand : {car["brand"]} ",
        f" Model : {car["model"]} ",
        f" Price : {car["price"]} ",
        sep = "|")
        count = count + 1
def buy_car(money):
    counti = 0
    for car in cars:
        print(f" {counti}.Brand : {car["brand"]}")
        counti = counti + 1
    print("Enter the number of you car")
    buycarname = int(input())
    if 0 <= buycarname < len(cars):
        print(f"Car brand: {cars[buycarname]["brand"]}")
        print(f"Car price: {cars[buycarname]["price"]}")
        print(f"Car model: {cars[buycarname]["model"]}")
        if cars[buycarname]["price"] > money:
            print("You're budget is not enough")
        else:
            print("You got budget")
            print("Enter 1 for confirming your purchase")
            print("Enter 2 for cancelling your purchase")
            selectedcar = int(input())
            if selectedcar == 1:
                print("You're purchase completed",
                f"==== Car Purchase Recipt ====",
                f"Time of Purchase:{now}",
                f"Car Brand: {cars[buycarname]["brand"]}",
                f"Car Model: {cars[buycarname]["model"]}",
                f"Car Price: {cars[buycarname]["price"]}",
                f"Payment Status: Paid",
                f"Authorized by Touseef",
                f"Showroom Stamp: ⓣ ",
                sep = "\n")
                money = money - cars[buycarname]["price"]
                cars.pop(buycarname)
            elif selectedcar == 2:
                print("Purchase cancelled!")
            else:
                invalid_option()
    else:
        print("Invalid car number")
    return money
def add_car():
    print("Enter car brand")
    buycarbrand = input()
    print("What model you want to add")
    buycarmodel = input()
    print("How much price you want to set?")
    buycarprice = int(input())
    cars.append({"brand":buycarbrand,"model": buycarmodel,"price": buycarprice})
    print("Car added to Showroom sucessfully")
def show_money():
    print(f"You have balance of {money}")
def saying_bye():
    print(f"Bye thanks for visiting")
def invalid_option():
    print("Invalid Option")

while option != 5:
    now = datetime.now()
    print("========== TOUSEEF CAR DEALERSHIP ==========",
    "1. Show Cars",
    "2. Buy Car",
    "3. Add Car",
    "4. Show Money",
    "5. Exit",
    sep = "\n")
    print("What you want to do Sir!")
    option = int(input())
    if option == 1:
        show_car()
    elif option == 2:
        money = buy_car(money)
    elif option == 3:
        add_car()
    elif option == 4:
        show_money()
    elif option == 5:
        saying_bye()
    else:
        invalid_option()