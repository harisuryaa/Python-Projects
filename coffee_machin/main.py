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
global resources

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

set = True


def remaining(drink, resources):
    ingredients = drink["ingredients"]
    for i in ingredients:
        resources[i] -= ingredients[i]


def check_ing(drink, resources):
    ingre = drink["ingredients"]

    for i in ingre:

        if ingre[i] > resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
        else:
            return True


def process_coins(cost, coffee):
    print("please insert coins")
    quarter = (int(input("How many quarter? :$ "))) * 0.25
    dime = (int(input("How many dime? :$ "))) * 0.10
    nickel = (int(input("How many nickel? :$ "))) * 0.05
    penny = (int(input("How many penny? :$ "))) * 0.01

    total_cost = quarter + dime + nickel + penny
    if total_cost == cost:
        print(f"Please take your {coffee}")
    elif total_cost > cost:
        print(f"Here is your change {round((total_cost - cost), 1)}$ ")
        print(f"Please take your {coffee} ☕️. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


while set:
    coffee = input(" What would you like (espresso/latte/cappuccino): ")

    if coffee == "off":
        set = False
    if coffee == "report":
        for i in resources:
            print(f"{i} : {resources[i]} ")
    else:
        drink = MENU[coffee]
        if check_ing(drink, resources):
            remaining(drink, resources)
            cost = drink["cost"]
            process_coins(cost, coffee)
