from helper_functions import *

def encounter():
    """
    Gives the description for the encounter in the containment room if the 
    user decides to inspect the enclosure.
    """
    terminal_clear()

    encounter_description_1 = """
    As you stand near the cracked glass enclosure, your curiosity gets the better 
    of you. You lean closer to inspect the dark stains and the deep scratch marks. 
    Suddenly, you hear the rumbling growl you heard earlier. Suddenly, it becomes a 
    full-blown roar that shakes the room. The mist on the floor begins to swirl 
    violently, and the air grows colder still. That's when you look up and see an
    opening at the top of the enclosure.\n
    """
    print(encounter_description_1)

    user_commands()

    encounter_description_2 = """
    Before you can react, a pair of glowing eyes appear in the darkness behind 
    the cracked glass. A powerful force slams against the inside of the enclosure, 
    causing the glass to splinter further. Panic sets in as you realize the 
    creature is still inside, but can roam within the containment room as 
    it pleases. \n
    """
    print(encounter_description_2)

    user_commands()

    encounter_description_3 = """
    From inside the enclosure, you see a black, shapless entity spring through the
    hole in the top sof the enclosure. Glass fractures and falls as it prowls in 
    your direction.\n
    
    You need to do something. Fast.\n
    """
    print(encounter_description_3)

    user_commands()

    encounter_choices = """
    1. RUN.
    2. Use the CROWBAR.
    3. Use the SYRINGE.
    4. Accept your FATE. 
    """
    print(encounter_choices)

    while True:
        encounter_choices_prompt = input("Type keyword here to make your choice: ").strip().lower()
        
        if encounter_choices_prompt == "run":
            encounter_run()
        elif encounter_choices_prompt == "crowbar":
            use_crowbar()
        elif encounter_choices_prompt == "syringe":
            use_syringe()
            break
        elif encounter_choices_prompt == "fate":
            accept_fate()
            break
        elif encounter_choices_prompt == "inventory": #not working
            display_inventory()
        elif encounter_choices_prompt == "quit":
            print("Exiting the game. Thank you for playing!")
            exit()
        else:
            print("Invalid choice. Please try again.")


def encounter_run():

    encounter_run_content = """
    Your heart pounds in your chest as the entity prowls closer,
    its glowing eyes locked onto you. Without a second thought, you turn 
    and bolt towards the door. The room is a maze, and panic threatens to 
    cloud your mind, but you force yourself to focus. You remember the 
    layout of the facility and the sequence of rooms that lead 
    to the entryway.
    
    You have to get it right. There's no room for error. 
    What are the two room numbers that will get you out quickest?
    """
    print(encounter_run_content)
    print(map)

    correct_sequence = ["5", "1"]
    player_sequence = []

    while len(player_sequence) < 2:
        room_choice = input("Enter the room number to escape (Room 5, Room 1): ").strip()

        if room_choice in ["1", "5"]:
            player_sequence.append(room_choice)
        else:
             print("That's not a valid room number. Try again.")

        if player_sequence == correct_sequence:
            print("""
            You dash through the facility, your footsteps echoing as you rush through Room 5, then Room 1. 
            The entity is close behind, but you don’t dare look back. You reach the entryway and slam 
            your hand against the door controls. The door slides open, and you throw yourself through 
            just in time, sealing it shut behind you.
            
            You're safe... for now. 
            """)
            user_commands()
            print("You escaped. Ending X of X.")
            user_commands()
        else:
            print("""
            In your panic, you take a wrong turn. You burst through a door, only to find yourself trapped 
            in a dead-end room. The entity is upon you before you can react. There's no escape.
            
            This is the end...
            """) 
            user_commands()
            print("You died. Ending X of X.")
            user_commands()
    

def use_crowbar(): #crowbar?

    use_crowbar_content = """
    Hands sweaty, you grip onto the crowbar and prepare to defend yourself.
    You just need to buy some time to get out. The entity is now right in front
    out you. It's claws making a shrieking noise as it stalks lazily towards you,
    like it knows it's won already.\n
    """
    print(use_crowbar_content)

    user_commands()

    use_crowbar_content_2 = """
    It pauses about 15 feet from you, and you try to take a steadying breath. \n
    """
    print(use_crowbar_content_2)

    user_commands()

    use_crowbar_content_3 = """
    It lunges for you. \n
    """
    print(use_crowbar_content_3)

    user_commands()

    use_crowbar_content_4 = """
    You didn't even get to raise your arm. \n
    """
    print(use_crowbar_content_4)

    user_commands()

    news_report = """
    Missing Urbex Explorer Sparks Urgent Search

    Date: August 14, 2024

    Location: Edgewood City

    Reporter: Jamie Miller, WXY News

    Edgewood City authorities have launched a search for 28-year-old
    Alex Carter, a known urban explorer, who vanished while
    investigating the abandoned Edgewood Facility. Carter entered
    the facility late yesterday night, aiming to explore the abandoned
    facility for content creation purposes. Communication with Carter
    ceased later that day, raising alarm among their peers.

    The Edgewood Facility, closed since the early 2000s due to safety
    concerns and mysterious incidents, is notorious for its dangerous
    conditions. Authorities are combing the area and reviewing security
    footage, urging anyone with information to come forward.

    “Carter is a seasoned explorer with a meticulous approach,” said
    a close friend. “Their disappearance is very concerning.”

    The search continues as authorities warn of the facility’s
    hazards and urge the public to report any leads.\n
    """
    print(news_report)
    user_commands()
    print("You died. Ending X of X.")
    user_commands()


def use_syringe():
    use_syringe_content = """
    Desperation fuels your next move. With shaking hands, you grab the syringe from your pocket. 
    The strange, glowing liquid inside pulses as if alive. The entity is almost upon you, its 
    darkness swallowing the light around it.
    
    As it lunges, you thrust the syringe forward, plunging it into the creature's form. The liquid 
    spreads quickly, glowing brighter and brighter, until the entity is enveloped in light. It lets 
    out a terrible, otherworldly screech, thrashing violently before collapsing to the ground.
    
    The glow fades, and the entity dissolves into a harmless puddle of darkness.
    
    You did it. You’ve subdued it.
    
    The path to the exit is clear. You don't waste any more time and make your way out. You're free.\n
    """
    print(use_syringe_content)
    print("You escaped. Ending X of X")
    
    user_commands()

def accept_fate():
    fate_description = """
    You realize there's no way out. The entity is too close, too powerful.
    You lower your hands, your body trembling, as you stand your ground. The 
    entity looms over you, its form shifting and writhing, its glowing 
    eyes piercing into your soul.
    
    You close your eyes, taking a final, steadying breath. The air around you 
    turns cold, and you feel the entity’s presence enveloping you. 
    There’s a moment of excruciating pain, then… nothing.
    
    Darkness. Silence. It’s all over.
    
    Your story ends here.
    """
    print(fate_description)

    user_commands()

    print("You died. Ending X of X.")

    user_commands()