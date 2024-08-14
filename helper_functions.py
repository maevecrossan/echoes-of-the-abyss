import os

def terminal_clear():
    """
    Clears terminal of all text.
    """
    os.system('clear')

def map():
    show_map = """

    Here is the map of the facility.

    +--------+  X  +--------+  X  +--------+
    |        |     |        |     |        |
    | Room 1 X-----X Room 2 X-----X Room 3 |
    | Entry  |     |Observa-|     | Storage|
    |  Hall  |     |  tion  |     | Closet |
    |        |     |Chamber |     |        |
    +---X----+     +---X----+     +---X----+
        |              |              |
    +---X----+     +---X----+     +---X----+
    |        |     |        |     |        |
    | Room 4 X-----X Room 5 X-----X Room 6 |
    | Office |     | Labor- |     | Morgue |
    |        |     |  atory |     |        |
    +---X----+     +---X----+     +---X----+
        |              |              |
    +---X----+     +---X----+     +---X----+
    |        |     |        |     |        |
    | Room 7 X-----X Room 8 X-----X Room 9 |
    | Break  |     |Security|     |Contain-|
    |  Room  |     |  Room  |     |  ment  |
    |        |     |        |     |  Room  |
    +--------+     +--------+     +--------+

    X = door\n
    """
    print(show_map)

def user_commands():
    while True:
        command = input("Press enter to continue...").strip().lower()
        if command == 'map':
            map()
        elif command == 'inventory': #not working
            display_inventory()
        elif command in ["continue", ""]:
            return
        elif command == 'quit':
            print("Exiting the game. Thank you for playing!")
            exit()
        else:
            print("Invalid command. Please try again.")

possible_inventory = ["syringe", "crowbar", "wire cutters", "roll of tape", "key", "keycard", "scalpel", "knife"]
current_inventory = []

def add_to_inventory(item):
    """
    Checks player input to see if it's a valid item and not already in inventory. 
    The selected item will be added to the player's inventory if both
    cases are true.
    If empty, player will be informed.
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
    else:
        print("Invetntory empty.")