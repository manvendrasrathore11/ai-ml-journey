
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
    "money" : 0 ,
}

def money(doll,choice2):
    if doll >=  5.0 and choice2 == "latte":
        print("Here is %0.2f in change"%(doll - 5.00))
        resources["money"] +=5
        return  True
    else  :
        print("Sorry that's not enough money. Money refunded.")
        return False








def items_report(reso):
    print("The current recorces are :")
    print(f"water : {reso["water"]}ml")
    print(f"milk : {reso["milk"]}ml")
    print(f"coffee : {reso["coffee"]}g")

def cheak_quantity(choice):
    if choice == "espresso" and int(resources["water"])  >= 50 and  int(resources["coffee"])  >= 18 :
        return  True
    elif choice == "latte" and int(resources["water"])  >= 200 and  int(resources["coffee"])  >= 24 and int(resources["milk"])  >= 150 :
        return True

    elif choice == "cappuccino" and int(resources["water"]) >= 250 and int(resources["coffee"]) >= 24 and int(resources["milk"]) >= 100:
        return True
    else:
        return False



flag = 1


while flag:

    user_choice = input(" 'what would you like' ?  (espresso/latte/cappuccino):")
    if user_choice == "off" :
        flag = 0
    elif user_choice == "report":
        print(items_report(resources))

    elif user_choice == "espresso" or user_choice == "latte" or  user_choice == "cappuccino":

        if cheak_quantity(user_choice):
            print("insert coin in coin box")
            quarters = int(input("quarters :"))*0.25
            dimes = int(input("dimes  :"))*0.10
            nickles = int(input("nickles  :"))*0.05
            pennies = int(input("pennies  :")) *0.01
            dollars  =  quarters + dimes + nickles + pennies
            if money(dollars,user_choice)
