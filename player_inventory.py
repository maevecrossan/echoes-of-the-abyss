from choices_functions import *

possible_inventory = ["syringe", "crowbar", "wire cutters", "roll of tape", "key", "keycard", "scalpel", "knife"]
current_inventory = []

def add_to_inventory(item):
    """
    Checks player input to see if it's a valid item and not already in inventory. 
    The selected item will be added to the player's inventory if both
    cases are true.
    """
    item = item.strip().lower()

    #checks the item is in the possible_inventory list.
    if item in possible_inventory:
        if item not in current_inventory:
            current_inventory.append(item) #adds item to inventory.
            print(f"{item.capitalize()} has been added to your inventory.\n")
        else:
            print(f"{item.capitalize()} is already in your invetory.\n")
    else:
        print(f"{item.capitalize()} is not valid. Please try again.\n")

def display_inventory():
    if current_inventory:
        print("Current inventory: ")
        for i, item in enumerate(current_inventory, starts=1):
            print(f"{i}. {item.capitalize()}")