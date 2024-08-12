# Write your code to expect a terminal of 80 characters wide and 24 rows high
from art import text2art #title
import os #clear terminal

def terminal_clear():
    """
    Clears terminal for user readibility
    """
    os.system('clear')


def title_screen():
    """
    Displays game title and welcome message.
    """
    title = text2art("Echoes  of  the  Abyss", font="smaller", chr_ignore = True)
    welcome_message = "Welcome to Echoes of the Abyss, a choose your own adventure game.\n"
    instructions = """
    You will be able to make multiple choices in this game.\n 
    To make a choice, when prompted, type the word in CAPITALS and hit 'enter'.\n
    """
    print(title)
    print(welcome_message)
    print(instructions)
    input("Press enter to begin.")
    


def backstory():
    terminal_clear()
    intro = """
    You are Alex, a 16-year-old who has lived in the quiet town of Redbrook
    your whole life. One summer night, your friend dares you to enter the
    long-abandoned government lab on the outskirts of town, a place shrouded
    in mystery and fear. No one dares to speak of what happened there, and
    those who have ventured inside never returned. The task was simple:
    retrieve your skateboard your friend claimed to have hidden in one of the
    rooms the day before.\n

    With nothing but a flashlight, you step into the cold, crumbling 
    facility. The door slams shut behind you with an eerie finality, 
    and you realize too late that this is no ordinary dare. Something 
    lurks within these walls, something far worse than the rumors 
    ever suggested.
    """
    print(intro)
    input("Press enter to continue...")


def entry_hall():

    """
    Gives the entry hall description and choices to be made.
    """

    terminal_clear()

    entry_hall_description_1 = """ 
    The Entry Hall is the facility's main entrance, now a hollow shell of 
    what it once was. The room is dark, with only a small window letting 
    in faint moonlight, casting eerie shadows across the floor. A thick 
    layer of dust covers the cracked tiles, and the air smells stale and 
    unused. The walls are lined with broken glass cases that once held 
    emergency equipment, now empty and shattered. The remnants of old 
    government posters, their messages faded and peeling, cling to the 
    walls.\n
    """
    print(entry_hall_description_1)

    input("Press enter to continue...")

    entry_hall_description_2 = """
    Near the center of the room is a large reception desk, toppled over 
    as if in a struggle. Papers and debris are scattered across the floor. 
    A faint draft passes through the hall, making the papers rustle eerily, 
    as if something unseen is moving through the space. The atmosphere is 
    oppressive, and every creak and groan of the old building sets your 
    nerves on edge.
    """
    print(entry_hall_description_2)
    input("Press enter to continue...")

    entry_hall_choices = """
    1. EXAMINE the room further.
    2. Move to Room 2 (OBSERVATION Chamber).
    3. Move to Room 4 (OFFICE). 
    """
    print(entry_hall_choices)


def observation_chamber():
    """
    Gives the observation chamber description and choices to be made.
    """
    terminal_clear()

    observation_chamber_description_1 = """
    You enter the Observation Chamber, once used to monitor experiments 
    in the lab. The room is dimly lit by a flickering fluorescent light,
    casting a sickly green glow over everything. A large, one-way mirror 
    dominates one wall. Once upon a time, you would have been able to see 
    through to the other side. Not anymore. It now bears a huge crack, 
    spiderwebbing from the center, as if something struck it with immense
    force. Occasionally, you think you can hear faint scratching noises 
    coming, as if something is moving behind it. 
    """
    print(observation_chamber_description_1)

    input("Press enter to continue...")
    
    observation_chamber_description_2 = """
    The room is otherwise eerily quiet, the only sound being the occasional
    drip of water from a leaking pipe. In the corner, a metal tray holds 
    various surgical tools, all of them rusted and dull. There are signs 
    of a struggle—overturned chairs, broken equipment, and dark stains on 
    the floor that you hope are just oil. The air feels heavy, as though 
    the room is holding its breath, waiting for something to happen.
    """
    print(observation_chamber_description_2)

    input("Press enter to continue...")

    observation_chamber_choices = """
    1. You see a syringe. It is filled with a strange, glowing liquid, 
    found on the floor near a metal tray. This might be useful later on.
    Pick up the SYRINGE?\n
    2. The flickering light creates a disorienting effect, making it 
    difficult to tell what’s real and what’s a trick of the eye. The 
    cracks in the mirror seem to form a pattern, though it’s hard to 
    tell what it is. Should you try to see what’s behind the MIRROR?\n
    3. Move to Room 3, the STORAGE closet.\n
    4. Move to Room 5, the LABRATORY.\n
    """
    print(observation_chamber_choices)
    
    input("Press enter to continue...")


#def storage_closet():
    """
    Gives the storage closet description and choices to be made.
    """
    terminal_clear()

    storage_closet_description_1 = """
    The Storage Closet is cramped and claustrophobic, with shelves 
    crammed with old equipment and supplies. The light here is even 
    dimmer than in the other rooms, casting long, flickering shadows 
    that make the space feel even smaller. Dust covers everything, 
    and the air is thick with the smell of mold and chemicals.  
    """
    print(storage_closet_description_1)

    input("Press enter to continue...")

    storage_closet_description_2 = """
    The walls are lined with peeling paint, and there’s a small, 
    cracked window that offers a view of the night outside, though the 
    glass is so dirty it’s hard to see anything clearly. The atmosphere 
    in the room is stifling, and you feel an overwhelming urge to 
    leave as soon as possible.  
    """
    print(storage_closet_description_2)

    input("Press enter to continue...")

    storage_closet_description_3 = """
    On one shelf, you spot a few items that might be useful: a small toolbox, 
    an old notebook, and a crowbar. The toolbox is locked, but it’s heavy, 
    suggesting it contains something valuable. 
    """
    print(storage_closet_description_3)

    input("Press enter to continue...")

#def office():


#def labratory():


#def morgue():


#def breakroom():


#def security_room():


#def containment_room():


#title_screen()
#backstory()
#entry_hall()
#observation_chamber()