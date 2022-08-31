MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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
    "money":0,
}
# print(MENU["espresso"]["ingredients"]["water"])
def initial_report(resources):
    """Gets you the resources if you ask for resources in the beginning"""
    water=resources["water"]
    milk=resources["milk"]
    coffee=resources["coffee"]
    money=resources["money"]
    print(f"Water : {water}ml")
    print(f"Milk : {milk}ml")
    print(f"Coffee : {coffee}g")
    print(f"Money : ${money}")

def updated_report(price,current_reso):
    """gives you the updated tally of resources data after each order"""
    # print(price["ingredients"])
    # print(current_reso["water"])
    if price["ingredients"]["water"]>current_reso["water"] or price["ingredients"]["milk"]>current_reso["milk"] or price["ingredients"]["coffee"]>current_reso["coffee"]:
        print("Sorry! Not enough resources")
        return
    print("Please insert coins")
    quaters = int(input("How many quaters?"))
    dimes = int(input("How many dimes?"))
    nickels = int(input("How many nickels?"))
    pennies = int(input("How many pennies?"))
    budget = 0.25 * quaters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
    if price["cost"]>budget:
        print("Not enough Money")
        return
    else:
        current_reso["water"]=current_reso["water"]-price["ingredients"]["water"]
        current_reso["milk"]=current_reso["milk"]-price["ingredients"]["milk"]
        current_reso["coffee"]=current_reso["coffee"]-price["ingredients"]["coffee"]

        current_reso["money"]=current_reso["money"]+price["cost"]
        change=budget-price["cost"]
        print(f"Here is ${round(change,2)} in change")

        return current_reso







def coffee(resources):
    """Main function that has the actual logic of the coffee machine"""
    while(2>1):
        choice=input("What would you like? (espresso/latte/cappuccino) :").lower()
        if choice=="report":
            initial_report(resources)
        if choice=="off":
            break
        if choice=="espresso":
            espre={}
            espre=MENU["espresso"]

            # print(espre)
            if updated_report(espre,resources):
                print("Here is your espresso ☕. Enjoy")
        if choice=="latte":
            lat={}
            lat=MENU["latte"]
            # print(lat)
            if updated_report(lat,resources):
                print("Here is your Latte ☕. Enjoy")
        if choice=="cappuccino":
            cappu={}
            cappu=MENU["cappuccino"]
            # print(cappu)
            if updated_report(cappu,resources):
                print("Here is your Cappuccino ☕. Enjoy")




coffee(resources)




