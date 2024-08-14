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
        elif command == 'inventory':
            current_inventory()
        elif command in ["continue", ""]:
            return
        elif command == 'quit':
            print("Exiting the game. Thank you for playing!")
            exit()
        else:
            print("Invalid command. Please try again.")