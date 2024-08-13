

def investigate_mirror():
    """
    Gives the description for the encounter in the containment room if the 
    user decides to inspect the enclosure.
    """
    #terminal_clear()

    encounter_description_1 = """
    As you stand near the cracked glass enclosure, your curiosity gets the better 
    of you. You lean closer to inspect the dark stains and the deep scratch marks. 
    Suddenly, the rumbling growl you heard earlier intensifies, becoming a 
    full-blown roar that shakes the room. The mist on the floor begins to swirl 
    violently, and the air grows colder still.
    """
    print(encounter_description_1)

    input("Press enter to continue...")

    encounter_description_2 = """
    Before you can react, a pair of glowing eyes appear in the darkness behind 
    the cracked glass. A powerful force slams against the inside of the enclosure, 
    causing the glass to splinter further. Panic sets in as you realize the 
    creature is still inside, but it’s almost free.\n

    You need to do something. Fast.
    """
    print(encounter_description_2)

    input("Press enter to continue...")

    encounter_choices = """
    1. Attempt to RUN.
    2. Use the CROWBAR.
    3. use the SYRINGE.
    4. Examine GLASS further. 
    """
    print(encounter_choices)
    encounter_choices_prompt = input("Type prompt here: ")
    input("Press enter to continue...")

def endings_main():
    """
    Responsible for calling all ending functions.
    """
    #investigate_mirror()

#endings_main()