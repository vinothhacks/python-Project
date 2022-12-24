from operator import truediv
from tkinter import OFF
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
profit = 0
resources = {
"water": 300,
"milk": 200,
"coffee": 100,
}
def resource(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
def coin():
    total=int(input("how many quarter: "))*0.25
    total+=int(input("how many dime: "))*0.10
    total+=int(input("how many nickel: "))*0.05
    total+=int(input("how many cent: "))*0.01
    return total

print("the coffees we have : ")
for i in MENU:
        print(i)
c=True
while(c):
    a=input("what do you want: ")
    if(a=="off"):
        break
    elif a=="report":    
        for i in resources:
            print("resources ",i," : ",resources[i])
    elif(a=="latte"):
        drink = MENU[a]
        if resource(drink["ingredients"]):
            print("please insert coin ")
            b=coin()
            if(b>MENU["latte"]["cost"]):
                print("your change is ",b-MENU["latte"]["cost"])
                print("here is your latte enjoy it ")
    elif(a=="espresso"):
        drink = MENU[a]
        if resource(drink["ingredients"]):
            print("please insert coin ")
            b=coin()
            if(b>MENU["espresso"]["cost"]):
                print("your change is ",b-MENU["espresso"]["cost"])
                print("here is your espresso enjoy it ")
    elif(a=="cappuccino"):
        
        drink = MENU[a]
        if resource(drink["ingredients"]):
            print("please insert coin ")
            b=coin()
            if(b>MENU["cappuccino"]["cost"]):
                print("your change is ",b-MENU["cappuccino"]["cost"])
                print("here is your cappuccino enjoy it ")
    else:
            print("not enough money ")