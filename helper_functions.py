

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

def exit_game():
    print("Thank you for playing. Goodbye!")
    exit()

def user_commands():
    while True:
        command = input("Press enter to continue...").strip().lower()
        if command == 'map':
            map()
        elif command == 'inventory':
            current_inventory()
        elif command == 'quit':
            print("Exiting the game.")
        else:
            print("Invalid command. Please try again.")