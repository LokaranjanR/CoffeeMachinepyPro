MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

while True:
    userinput = input("What would you like? (espresso/latte/cappuccino)")

    if userinput == "off" :
     exit(0)
    elif userinput == "report" :
        print("Water: " + str(resources["water"]))
        print("Milk: " + str(resources["milk"]))
        print("Coffee: " + str(resources["coffee"]))
        print("Money: " + str(resources["money"]))
    elif userinput == "espresso":
        if MENU["espresso"]["ingredients"]["water"] > resources["water"] :
            print("Sorry,There is not enough water!,A refund has been issued")

        elif  MENU["espresso"]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry,There is not enough coffee!,A refund has been issued")

        else:
            print("Please insert your coins now!!!")
            quarters = float(input("How many quarters?"))
            dimes = float(input("How many dimes?"))
            nickles = float(input("How many nickles?"))
            pennies = float(input("How many pennies?"))
            total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
            if total >= MENU["espresso"]["cost"]:
                change = total - MENU["espresso"]["cost"]
                resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
                resources['money'] += MENU['espresso']['cost']
                print("Here is your espresso ☕")
                print("Here is your change = " + str(change) )
            elif total < MENU["espresso"]["cost"]:
                print("Sorry that's not enough money ,A refund has been issued")

    elif userinput == "latte":
        if MENU["latte"]["ingredients"]["water"] > resources["water"] :
            print("Sorry,There is not enough water!,A refund has been issued")

        elif MENU["latte"]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry,There is not enough milk!,A refund has been issued")

        elif MENU["latte"]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry,There is not enough coffee!,A refund has been issued")

        else:
            print("Please insert your coins now!!!")
            quarters = float(input("How many quarters?"))
            dimes = float(input("How many dimes?"))
            nickles = float(input("How many nickles?"))
            pennies = float(input("How many pennies?"))
            total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
            if total >= MENU["latte"]["cost"]:
                change = total - MENU["latte"]["cost"]
                resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
                resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
                resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
                resources['money'] += MENU['latte']['cost']
                print("Here is your latte ☕")
                print("Here is your change = " + str(change) )
            elif total < MENU["latte"]["cost"]:
                print("Sorry that's not enough money ,A refund has been issued")

    elif userinput == "cappuccino":
        if MENU["cappuccino"]["ingredients"]["water"] > resources["water"] :
            print("Sorry,There is not enough water!,A refund has been issued")

        elif MENU["cappuccino"]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry,There is not enough milk!,A refund has been issued")

        elif MENU["cappuccino"]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry,There is not enough coffee!,A refund has been issued")

        else:
            print("Please insert your coins now!!!")
            quarters = float(input("How many quarters?"))
            dimes = float(input("How many dimes?"))
            nickles = float(input("How many nickles?"))
            pennies = float(input("How many pennies?"))
            total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
            if total >= MENU["cappuccino"]["cost"]:
                change = total - MENU["latte"]["cost"]
                resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
                resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
                resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
                resources['money'] += MENU['cappuccino']['cost']
                print("Here is your cappuccino ☕")
                print("Here is your change = " + str(change) )
            elif total < MENU["cappuccino"]["cost"]:
                print("Sorry that's not enough money ,A refund has been issued")




