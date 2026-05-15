'''
DEVELOPER(S): Shaya Hoseini
COLLABORATORS: Copilot (referencing concepts I wanted a reminder for)
DATE: 5/1/26
'''

"""
This program starts the user in a store with an empty shopping basket and a starting amount of 20 dollars. The user is then prompted to buy anything the store has to offer in a list,
each item only being able to be bought once. When purchasing an item, the user is told the cost and whether they want to proceed or not if they change their mind. The user may 
also check their shopping basket and wallet at any time. The user may also stop at any time to checkout, where they will be told if they quality for express checkout.

"""

##########################################
# IMPORTS:
# <list of modules needed for the program and their purpose>
##########################################

##########################################
# FUNCTIONS:
##########################################
def make_basket_file():
    '''
    Writes the basket ASCII image onto the basket.txt file to be referenced later.
    '''

    basket = ("   _____\n  |     |\n__|_____|__\n\\         /\n \\_______/\n")
    
    file = open("basket.txt", "w")
    file.write(basket)
    file.close()

def view_basket():
    '''
    Allows the user to print the current state of the basket.txt file.
    '''
    file = open("basket.txt", "r")
    basket_print = file.read()
    file.close()
    print(basket_print)

def buy_produce(user, item, item_price):
    '''
    When called, takes the parameters of the item being bought, its price, as well as the information of the user (wallet and basket contents)
    First asks whether user wants to purchase item. If the user wants to buy the item and can afford it, will append the item to their basket.
    If they can't afford it, returns them to menu.
    When an item is successfully purchased, also overwrites the basket text file with updated basket item count.
    '''
    buy = input(f"Would you like to buy this {item} for {item_price}?\n(1) Yes.\n(2) No.\n")
    if buy.isalpha():
        buy = buy.lower()

    if (buy == "1" or buy == "yes") and user["wallet"] > item_price:
        user["wallet"] = user["wallet"] - item_price
        user["basket"].append(item)

        count = len(user["basket"])
        file = open("basket.txt", "w")
        file.write(f"   _____\n  |  {count:^}  |\n__|_____|__\n\\         /\n \\_______/\n")
        file.close()
        return user, True
    elif buy == "2" or buy == "no":
        return user, False
    
    elif (buy == "1" or buy == "yes") and user["wallet"] < item_price:
        print("Sorry, it looks like you don't have enough to buy that!")
        return user, False

def main():
    '''
    First initalizes the user dictionary and store dictionary. Then initializes and prints the empty basket as you're welcomed into the store.

    I utilize two dictionaries here because the numerical indexes of the values are of little importance in this context,
    the values attached to the keys being useful for quickly calling the prices of each item within the store, as well as the
    simple 'del' statement that allowed me to easily remove key elements from 'basket'. However, within the
    'basket' key, I made the value an accumulating list so I could continue to append every item the user purchased.
    '''
    user = {"wallet": 20.00, "basket": []}
    store = {"Apple": 3.99, "Banana": 1.99, "Orange": 2.49, "Bread": 4.75, "Milk": 4.00, "Pears": 3.75, "Cereal": 5.99, "Eggs": 6.99}

    print("Welcome to the store! Here is your basket, it even has a tracker to tell you if you can use our express checkout (4 items max), neat huh!")
    make_basket_file()
    view_basket()
    buying = ""

    # While loop to check if user wants to keep shopping with "buying" variable.
    while buying.lower() != "nevermind":
        print(f"What would you like to buy here? We have:")
        for items in store.keys():
            print("> " + items)
        buying = input("> Type the item name or 'nevermind' to stop. You can also type 'check' to look at your basket and wallet.\n")

        # Checks to see if the item being asked for is within the store. Is case-sensitive. Will return an error statement if store does not contain item, then takes user back to menu. 
        if buying in store:
            user, purchased = buy_produce(user, buying, store[buying])
            if purchased:
                del store[buying]
                view_basket()
        # If item is not in store and also isn't a viable response, returns an error message and returns to menu.
        elif buying not in store and buying.lower() != "nevermind" and buying.lower() != "check":
            print("Sorry we don't have that.")
        elif buying == "check" and len(user["basket"]) > 0:
            basket_contents = ""
            for items in user["basket"]:
                basket_contents += items + ", "
            print("You have " + basket_contents + f"in your basket and ${user['wallet']:.3} in your wallet.")
        elif buying == "check" and len(user["basket"]) == 0:
            print(f"You don't have anything in your basket yet! But you have ${user['wallet']:.3} in your wallet.")

    if len(user["basket"]) == 0:
        print("\nAww, well I hope you'll purchase from us next time! Toodles!")
    elif len(user["basket"]) > 4:
        print("\nI hope you found everything you were looking for! You unfortunately don't qualify for express checkout, but it'll be quick regardless!")
        print("I hope you had a stellar time shopping with us! See you next time!")   
    else:
        print("\nI hope you found everything you were looking for! And look at that, we can get you into the express checkout, snazzy!")
        print("I hope you had a stellar time shopping with us! See you next time!")


##########################################
# MAIN PROGRAM:
##########################################
main()
