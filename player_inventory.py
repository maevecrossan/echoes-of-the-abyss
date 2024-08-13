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
            print(f"{item} has been added to your inventory.")
        else:
            print(f"{item} is already in your invetory.")
    else:
        print(f"{item} is not valid. Please try again.")

while True:
    choice_prompt = input("Type keyword here to make your choice: ")

    if choice_prompt == 'quit':
        print("You are exiting the game.")
        break

#add_to_inventory(choice_prompt)