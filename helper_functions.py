import os
from art import text2art  # title art


def title_screen():
    """
    Displays game title and welcome message.
    Informs the user of the type commands they can use.
    """
    terminal_clear()
    title = text2art("Echoes  of  the  Abyss", font="smaller", chr_ignore=True)
    welcome_message = "Welcome to Echoes of the Abyss, a choose your own adventure game.\n"
    instructions = """
    You will be able to make multiple choices in this game.\n
    To make a choice, when prompted, type the word in CAPITALS and hit 'enter'.\n
    To look at the map, type MAP and hit 'enter'.\n
    To see your inventory, type INVENTORY and hit 'enter'.\n
    To quit the game, type QUIT.\n
    To see this list of commands, type HELP and hit 'enter'.\n
    """
    print(title)
    print(welcome_message)
    print(instructions)
    user_commands()


def terminal_clear():
    """
    Clears terminal of all text.
    """
    os.system('clear')


def map():
    """
    Prints facility map to terminal without disrupting the story.
    """
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
    """
    Reads user's comands and calls the relevant functions.
    """
    while True:
        command = input(
            "Type a command, or press enter to continue...").strip().lower()
        if command == 'map':
            map()
        elif command == 'inventory':
            display_inventory()
        elif command in ["continue", ""]:
            return
        elif command == 'quit':
            print("""
            Exiting the game. Thank you for playing!
            Click 'Run Program' to restart.
            """)
            exit()
        elif command == 'help':
            print("""
            To make a choice, when prompted, type the word in CAPITALS and hit 'enter'.\n
            To look at the map, type MAP and hit 'enter'.\n
            To see your inventory, type INVENTORY and hit 'enter'.\n
            To quit the game, type QUIT.\n
            To see this list of commands, type HELP and hit 'enter'.\n
            """)
        else:
            print("Invalid command. Please try again.")


# list of all possible collectable items
possible_inventory = [
    "syringe",
    "crowbar",
    "wire cutters",
    "key",
    "keycard",
    "scalpel",
    "knife"]

current_inventory = []


def add_to_inventory(item):
    """
    Checks player input to see if it's a valid item and not already in inventory.
    The selected item will be added to the player's inventory if both
    cases are true.
    If empty, player will be informed.
    """
    item = item.strip().lower()

    # checks the item is in the possible_inventory list.
    if item in possible_inventory:
        if item not in current_inventory:
            current_inventory.append(item)  # adds item to inventory.
            print(f"{item.capitalize()} has been added to your inventory.\n")
        else:
            print(f"{item.capitalize()} is already in your invetory.\n")
    else:
        print(f"{item.capitalize()} is not valid. Please try again.\n")


def display_inventory():
    if current_inventory:
        print("\nCurrent inventory: ")
        for i, item in enumerate(current_inventory, start=1):
            print(f"{i}. {item.capitalize()}\n")
    else:
        print("Invetntory empty.\n")
