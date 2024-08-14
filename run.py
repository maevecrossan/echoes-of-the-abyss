# Write your code to expect a terminal of 80 characters wide and 24 rows high
import os
from art import text2art #title
from helper_functions import user_commands
from helper_functions import map
from helper_functions import terminal_clear
from choices_functions import *
#from player_inventory import *
#from ending_sequences import *

def title_screen():
    """
    Displays game title and welcome message.
    """
    title = text2art("Echoes  of  the  Abyss", font="smaller", chr_ignore = True)
    welcome_message = "Welcome to Echoes of the Abyss, a choose your own adventure game.\n"
    instructions = """
    You will be able to make multiple choices in this game.\n 
    To make a choice, when prompted, type the word in CAPITALS and hit 'enter'.\n
    To look at the map, type MAP and hit 'enter'.\n
    To see your inventory, type INVENTORY and hit 'enter'.\n
    To quit the game, type QUIT.\n
    """
    print(title)
    print(welcome_message)
    print(instructions)
    input("Press enter to begin.")

def backstory():

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
    input("Enter the facility.")


def entry_hall():

    """
    Gives the entry hall description and choices to be made.
    Links to external file which details the interactions with each
    item that can be found throughout the game. 
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

    user_commands()

    entry_hall_description_2 = """
    Near the center of the room is a large reception desk, toppled over 
    as if in a struggle. Papers and debris are scattered across the floor. 
    A faint draft passes through the hall, making the papers rustle eerily, 
    as if something unseen is moving through the space. The atmosphere is 
    oppressive, and every creak and groan of the old building sets your 
    nerves on edge.
    """
    print(entry_hall_description_2)

    user_commands()

    entry_hall_choices = """
    1. EXAMINE the room further.
    2. Move to Room 2, the OBSERVATION Chamber.
    3. Move to Room 4, the OFFICE. 
    """
    print(entry_hall_choices)

    while True: #Keep prompting until response is valid.
        entry_hall_prompt = input("Type keyword here to make your choice: ").strip().lower()

        if entry_hall_prompt == "examine":
            examine_entry_hall()
            break
        elif entry_hall_prompt == "observation":
            observation_chamber()
            break
        elif entry_hall_prompt == "office":
            office()
            break
        else:
            print("Invalid choice. Please try again.")


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

    user_commands()
    
    observation_chamber_description_2 = """
    The room is otherwise eerily quiet, the only sound being the occasional
    drip of water from a leaking pipe. In the corner, a metal tray holds 
    various surgical tools, all of them rusted and dull. There are signs 
    of a struggle—overturned chairs, broken equipment, and dark stains on 
    the floor that you hope are just oil. The air feels heavy, as though 
    the room is holding its breath, waiting for something to happen.
    """
    print(observation_chamber_description_2)

    user_commands()

    observation_chamber_choices = """
    1. Pick up the SYRINGE?\n
    2. Try to see what’s behind the MIRROR.\n
    3. Move to Room 3, the STORAGE closet.\n
    4. Move to Room 5, the LABORATORY.\n
    4. Move to Room 1, the ENTRY hall.\n
    """
    print(observation_chamber_choices)

    while True:
        observation_chamber_prompt = input("Type keyword here to make your choice: ").strip().lower()
        
        if observation_chamber_prompt == "syringe":
            take_syringe()
            break
        elif observation_chamber_prompt == "mirror":
            investigate_mirror()
            break
        elif observation_chamber_prompt == "toolbox":
            inspect_toolbox()
            break
        elif observation_chamber_prompt == "observation":
            observation_chamber()
            break
        elif observation_chamber_prompt == "morgue":
            morgue()
            break
        else:
            print("Invalid choice. Please try again.")
            
    user_commands()


def storage_closet(): #needs key to open
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

    user_commands()

    storage_closet_description_2 = """
    The walls are lined with peeling paint, and there’s a small, 
    cracked window that offers a view of the night outside, though the 
    glass is so dirty it’s hard to see anything clearly. The atmosphere 
    in the room is stifling, and you feel an overwhelming urge to 
    leave as soon as possible.  
    """
    print(storage_closet_description_2)

    user_commands()

    storage_closet_description_3 = """
    On one shelf, you spot a few items that might be useful: a small toolbox, 
    an old notebook, and a crowbar. The toolbox is locked, but it’s heavy, 
    suggesting it contains something valuable. 
    """

    print(storage_closet_description_3)

    user_commands()

    storage_closet_choices = """
    1. Pick up the CROWBAR. This could be helpful later.\n
    2. Examine the NOTEBOOK. Reading through it might reveal vital information 
    about the facility.\n
    3. Inspect the TOOLBOX. If you can find a way to open it, it might contain 
    something valuable.\n
    4. Move to Room 2, the OBSERVATION chamber.\n
    5. Move to Room 6, the MORGUE.\n
    """
    print(storage_closet_choices)

    while True: 
        storage_closet_prompt = input("Type keyword here to make your choice: ").strip().lower()

        if storage_closet_prompt == "crowbar":
            take_crowbar()
            break
        elif storage_closet_prompt == "notebook":
            read_notebook()
            break
        elif storage_closet_prompt == "toolbox":
            inspect_toolbox()
            break
        elif storage_closet_prompt == "observation":
            observation_chamber()
            break
        elif storage_closet_prompt == "morgue":
            morgue()
            break
        else:
            print("Invalid choice. Please try again.")


    user_commands()


def office():
    """
    Gives the office description and choices to be made.
    """
    terminal_clear()

    office_description_1 = """
    The Office is in disarray, with toppled chairs and scattered papers 
    littering the floor. The walls are lined with filing cabinets, many 
    of which have been pried open, their contents strewn about. A desk 
    sits in the center of the room, covered in dust and old files. One 
    of the computers on the desk is smashed, its screen shattered, 
    while another seems to be intact but unpowered.
    """
    print(office_description_1)

    user_commands()

    office_description_2 = """
    The room feels strangely untouched compared to the rest of the facility, 
    as if the people who worked here left in a hurry. There’s a sense of 
    urgency in the air, as though whatever happened here, happened quickly 
    and unexpectedly. A logbook lies open on the desk, its pages filled with 
    notes on the lab’s experiments.
    """
    print(office_description_2)

    user_commands()

    office_choices = """
    1. Read through the LOGBOOK. Gain insight into the experiments conducted in 
    the facility.\n
    2. Examine the broken COMPUTERS. There might be something useful or salvageable.\n
    3. Move to Room 1, the ENTRY hall.\n
    4. Move to Room 5, the LABRATORY.\n
    5. Move to Room 7, the BREAK room.\n
    """
    print(office_choices)

    while True: 
        office_choices_prompt = input("Type keyword here to make your choice: ").strip().lower()
        if office_choices_prompt == "logbook":
            read_logbook()
            break
        elif office_choices_prompt == "entry":
            entry_hall()
            break
        elif office_choices_prompt == "laboratory":
            laboratory()
            break
        elif office_choices_prompt == "break":
            break_room()
            break
        else:
            print("Invalid choice. Please try again.")

    user_commands()


def laboratory():
    """
    Gives the laboratory description and choices to be made.
    """
    terminal_clear()

    laboratory_description_1 = """
    The Laboratory is the heart of the facility, where experiments were conducted. 
    The room is large, with long tables covered in various pieces of scientific 
    equipment, most of which are now broken or rusted. Glass beakers and test tubes 
    are scattered across the floor, some of them shattered. A strange, faintly 
    glowing residue clings to the surfaces of the tables, and the air is thick 
    with the smell of chemicals that sting your nose.

    """
    print(laboratory_description_1)

    user_commands()

    laboratory_description_2 = """
    You can’t pinpoint the source, but you can hear the quiet hum of old machinery, 
    though none of it seems to be working. Occasionally, you hear a faint buzzing 
    noise, like electricity sparking. The room feels charged with an unseen energy, 
    as if the experiments conducted here left a permanent mark on the space. The 
    walls are lined with cabinets, most of which are locked. In one corner, a lab 
    coat hangs on a hook, and you notice something bulging in one of its pockets.
    """
    print(laboratory_description_2)

    user_commands()

    laboratory_choices = """
    1. Pick up the KEY: This might be the key to unlocking a critical part of the 
    facility.\n
    2. Examine the lab EQUIPMENT.\n
    3. Move to Room 2, the OBSERVATION chamber.\n
    4. Move to Room 4, the OFFICE.\n
    5. Move to Room 6, the MORGUE.\n
    6. Move to Room 8, the SECURITY Room.\n
    """
    print(laboratory_choices)

    while True:
        laboratory_choices_prompt = input("Type keyword here to make your choice: ").strip().lower()

        if laboratory_choices_prompt == "key":
            take_key()
            break
        elif laboratory_choices_prompt == "equipment":
            examine_equipment()
            break
        elif laboratory_choices_prompt == "observation":
            observation_chamber()
            break
        elif laboratory_choices_prompt == "office":
            office()
            break
        elif laboratory_choices_prompt == "morgue":
            morgue()
            break
        elif laboratory_choices_prompt == "security":
            security_room()
            break
        else:
            print("Invalid choice. Please try again.")

    user_commands()


def morgue():
    """
    Gives the morgue description and choices to be made.
    """
    terminal_clear()

    morgue_description_1 = """
    The Morgue is cold and sterile, with rows of metal drawers lining the walls. 
    The air is frigid, and your breath creates small clouds of mist in front of 
    you. The room is dimly lit, with a single lightbulb flickering overhead, 
    casting long, eerie shadows across the room. A metal examination table sits 
    in the center, covered with a stained sheet.\n
    """
    print(morgue_description_1)

    user_commands()

    morgue_description_2 = """
    The smell of formaldehyde is overwhelming, mixed with something else—something 
    rotten. The drawers in the walls are mostly closed, but a few are slightly ajar, 
    as if someone didn’t have time to close them all. In front of the row of draws, 
    you see a lab coat crumpled on the floor. Something is peaking out of the pocket.\n
    You pause, unable to shake the feeling that you’re being watched, even 
    though the room is empty. There’s a small, rusted surgical cart in the corner, 
    holding a few old, bloodstained tools. Something in the corner catches your eye.\n
    """
    print(morgue_description_2)

    user_commands()

    morgue_choices = """
    1. Pick up the SCALPEL.\n
    2. Examine the lab COAT.\n
    3. Move to Room 5, the LABORATORY.\n
    4. Move to Room 9, the CONTAINMENT Room.\n
    """
    print(morgue_choices)

    while True:
        morgue_choices_prompt = input("Type keyword here to make your choice: ").strip().lower()

        if morgue_choices_prompt == "scalpel":
            take_scalpel()
            break
        elif morgue_choices_prompt == "coat":
            examine_lab_coat()
            break
        elif morgue_choices_prompt == "laboratory":
            laboratory()
            break
        elif morgue_choices_prompt == "containment":
            containment_room()
            break
        else:
            print("Invalid choice. Please try again.")

    user_commands()


def break_room():
    """
    Gives the break room description and choices to be made.
    """
    terminal_clear()

    break_room_description_1 = """
    The Break Room was once a place where the lab staff could relax, but now it’s 
    a scene of chaos. The room is cluttered with overturned and broken chairs and 
    tables, as if something had torn through in a fit of rage. A vending machine 
    lies on its side, its glass shattered and snacks scattered across the floor. 
    There’s a small kitchenette in one corner, with a fridge and a microwave, 
    both covered in grime.
    """
    print(break_room_description_1)

    user_commands()

    break_room_description_2 = """
    The room feels oddly out of place compared to the rest of the facility, 
    as if the normalcy of a break room doesn’t belong in such a sinister 
    environment. There’s a calendar on the wall, still turned to a month from 
    decades ago, and a few personal items left behind on the counter—a coffee mug,
    a half-eaten sandwich, now mummified with age. The room is eerily silent, 
    and the air is thick with dust.
    """
    print(break_room_description_2)

    user_commands()

    break_room_choices = """
    1. Pick up the KNIFE.\n
    2. Take the energy DRINK.\n
    3. Go back to Room 4, the OFFICE.\n
    4. Move to Room 8, SECURITY Room, through the door ahead.\n
    """
    print(break_room_choices)

    while True:
        break_room_choices_prompt = input("Type keyword here to make your choice: ").strip().lower()
        
        if break_room_choices_prompt == "knife":
            security_panel()
            break
        elif break_room_choices_prompt == "drink":
            energy_drink()
            break
        elif break_room_choices_prompt == "office":
            office()
            break
        elif break_room_choices_prompt == "security":
            security_room()
            break
        else:
            print("Invalid choice. Please try again.")
       
    user_commands()


def security_room():
    """
    Gives the security room description and choices to be made.
    """
    terminal_clear()

    security_room_description_1 = """
    The Security Room is filled with monitors and control panels, most of which 
    are now dark and lifeless. A few of the monitors still flicker with static, 
    offering brief, distorted glimpses of various parts of the facility. The 
    room is cramped, with just enough space for a single chair in front of the 
    console. Papers and old security logs are scattered across the desk, 
    detailing the final days of the lab’s operation.
    """
    print(security_room_description_1)

    user_commands()

    security_room_description_2 = """
    A red light blinks ominously on one of the control panels, indicating that 
    something is still active in the facility. A nearby locker stands open, 
    with a few items left behind by the last security personnel. The room feels 
    like a nerve center, where someone once kept watch over the entire lab. 
    Now, it’s a tomb of information, with the only clues to what happened hidden 
    within the disjointed logs and static-filled screens.
    """
    print(security_room_description_2)

    user_commands()

    security_room_choices = """
    1. Read the security LOGS.\n
    2. Go back to Room 5, the LABORATORY.\n
    3. Move to Room 7, the BREAK Room.\n
    4. Move to Room 9, the CONTAINMENT Room.\n
    """
    print(security_room_choices)

    while True:
        security_room_choices_prompt = input("Type keyword here to make your choice: ").strip().lower()

        if security_room_choices_prompt == "logs":
            security_logs()
            break
        elif security_room_choices_prompt == "laboratory":
            laboratory()
            break
        elif security_room_choices_prompt == "break":
            break_room()
            break
        elif security_room_choices_prompt == "containment":
            containment_room()
            break
        else:
            print("Invalid choice. Please try again.")

    user_commands()


def containment_room():
    """
    Gives the containment room description and choices to be made.
    """
    terminal_clear()

    containment_room_description_1 = """
    The Containment Room is the most ominous part of the facility. It’s large and 
    mostly empty, with the main feature being a massive, reinforced glass enclosure 
    in the center. The glass is cracked but still intact, though dark stains and 
    scratch marks on the inside suggest something tried hard to escape. The room 
    is dimly lit by emergency lights, casting a red glow that makes everything 
    look surreal and threatening.
    """
    print(containment_room_description_1)

    user_commands()

    containment_room_description_2 = """
    The air is heavy with a sense of dread, as if the very walls are charged 
    with fear. The temperature here is noticeably lower, and a faint mist clings 
    to the floor. There’s a control panel near the entrance, still operational but 
    locked behind a password. You can hear the distant sound of something scraping 
    against metal, but it’s impossible to tell where it’s coming from. The 
    atmosphere is thick with tension, as if something terrible could happen at any 
    moment. The hair on the back of your neck stands on end. 
    """
    print(containment_room_description_2)

    user_commands()

    containment_room_choices = """
    1. Examine the control PANEL: Attempt to input the partial access code and 
    unlock it.\n
    2. INSPECT the glass enclosure: Try to determine what was once held inside.\n
    3. Move to Room 6, the MORGUE.\n
    4. Move to Room 8, the SECURITY Room.\n
    """
    print(containment_room_choices)

    while True:
        security_room_choices_prompt = input("Type keyword here to make your choice: ").strip().lower()

        if security_room_choices_prompt == "panel":
            security_panel()
            break
        elif security_room_choices_prompt == "inspect":
            encounter()
            break
        elif security_room_choices_prompt == "morgue":
            morgue()
            break
        elif security_room_choices_prompt == "security":
            security_room()
            break
        else:
            print("Invalid choice. Please try again.")

    user_commands()

def game_main():
    title_screen()
    backstory()
    entry_hall()
    observation_chamber()
    storage_closet()
    office()
    laboratory()
    morgue()
    break_room()
    security_room()
    containment_room()

game_main()
choices_main()