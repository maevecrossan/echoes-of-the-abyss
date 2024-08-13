import os #clear terminal

def terminal_clear():
    """
    Clears terminal for user readibility
    """
    os.system('clear')

def map():
    show_map = """
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
    input("Press enter to continue...")



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

    if choice_promptlogs == 'quit':
        print("You are exiting the game.")
        break

add_to_inventory(choice_prompt)

def user_commands():
    while True:
        command = input("Press enter to continue...").strip().lower()
        if command == 'map':
            map()
        elif command == 'inventory':
            current_inventory()