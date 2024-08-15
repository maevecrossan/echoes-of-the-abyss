from helper_functions import user_commands


def examine_desk():
    desk_content = """
    Upon closer inspection, the you find a small panel on the wall 
    hidden behind the desk. It has been pried open. Inside the panel, 
    scrawled in a hurried, shaky hand on the metal surface, is a 
    message etched into the steel:

        It’s watching.
        Don’t trust your senses.
        Get out. -J\n
    """
    print(desk_content)


def take_syringe():  # working #INVENTORYITEM
    syringe_content = """
    You take a closer look at the syringe. It is filled with a strange, 
    glowing liquid, found on the floor near a metal tray. This might be 
    useful later on.\n
    You put it carefully in your pocket.\n
    """

    print(syringe_content)
    return "syringe"


def take_crowbar():  # INVENTORYITEM
    crowbar_content = """
    A sturdy metal crowbar that can be used to pry open doors or defend
    against an attack."\n
    """
    print(crowbar_content)
    return "crowbar"


def read_notebook():
    """
    This function holds the string content for the notebook found
    in the storage room.
    The notebook hints at the existence of the keycard and the
    critical role the Containment Room plays in stopping the creature.
    """
    notebook_content = """
    May 4th, 1998\n

    I can’t believe what they’ve done. The experiment was a failure 
    from the start. \n

    Now, it’s out there, lurking in the shadows. We’ve sealed it in, 
    but for how long? The creature is smarter than we anticipated. 
    It’s only a matter of time before it finds a way out. Or maybe it
    wants to stay...\n

    They told us to keep working, to find a way to "neutralize" it, 
    but I don’t think we have enough time. I just want to get out of 
    here, but the higher-ups won’t let anyone leave. We’re trapped, 
    and it knows. \n

    If anyone finds this, know that the keycard is our only hope. Get 
    to the Containment Room, find the panel, and shut it down 
    before it’s too late.\n

    - Dr. Alice Reynolds \n
    """
    print(notebook_content)


def inspect_toolbox():  # INVENTORYITEM
    toolbox_content = """
    You reach for the toolbox, underestimating its weight. It bangs to 
    the floor, it's hinges fracturing revealing the contents.\n

    Inside you find a variety of tools useful things. A roll of duct 
    tape that might be useful for securing items or fixing broken equipment. 
    There is also a set of wire cutters. They might be useful for
    disabling security systems or cutting through locks.\n

    You put them in your backpack.\n
    """
    print(toolbox_content)
    return "wire cutters", "roll of tape"


def investigate_mirror():
    """

    """
    mirror_content = """
    You step closer to the mirror. You swear you can hear faint 
    scratching noises coming, as if something is moving behind it.\n
    """
    print(mirror_content)


def read_logbook():  # working
    logbook_content = """
    April 27th, 1998\n

    Entry 147\n

    The subject continues to exhibit signs of increased aggression 
    and intelligence. It has begun to recognize patterns in our containment 
    procedures, and I fear it’s only a matter of time before it attempts 
    to escape. \n

    We’ve reinforced the glass in the containment unit, but I’m not sure it 
    will hold. The creature’s strength is beyond anything we anticipated. 
    Dr. Reynolds has suggested sedating it, but I’m worried the sedatives 
    won’t be enough.\n

    We’re running out of options. If we can’t find a way to neutralize 
    it, this whole facility could be at risk.\n

    - Dr. Gregory Shaw\n

    """
    print(logbook_content)


def examine_computers():  # working
    computer_content = """
    You press a button on the keyboard, and the sudden bright light form
    the screen hurts your eyes for a moment. When your eyes adjust, you see
    a warning message on the screen that reads:\n

        URGENT: CONTAINMENT PROTOCOL\n

        In case of containment breach, all personnel are to evacuate the 
        facility immediately. The creature must not be allowed to escape 
        under any circumstances. Keycards are required to access the Containment 
        Room and initiate the lockdown procedure.\n

        Failure to follow protocol will result in immediate termination of the
        facility’s power and security systems. This measure is in place to 
        prevent the creature from escaping the premises.\n

        - Director Markson\n
    """
    print(computer_content)


def take_key():  # working #INVENTORYITEM
    key_content = """
    As you search through the chaos of broken glassware, overturned tables, 
    and scattered notes, they notice a small key lying on the floor near an
    overturned chair. The key is tagged with a faded label that reads 
    "Storage," which indicates that it unlocks a cabinet or door within 
    the facility.\n
    """
    print(key_content)
    return "key"


def examine_equipment():  # working
    lab_equipment_content = """
    You search around the graveyard of the lab equipment. Behind a 
    pair of toppled monitors, you see a clipboard. \n

        SUBJECT: SPECIMEN #42

        Notes on Weaknesses:

        - METABOLISM: The creature exhibits an extremely high metabolic rate.
        Sedatives have a temporary effect but can slow it down enough for containment.\n
        - EXPOSURE TO COLD: Preliminary tests suggest that the creature is sensitive
        to extreme cold. Cryogenic solutions or environments may temporarily
        immobilize it.\n
        - GLOWING SERUM: Compound X-17, when injected, causes severe neural disruption
        in the creature. Temporary paralysis observed in 83% of cases.\n
    """
    print(lab_equipment_content)


def examine_lab_coat():  # working #INVENTORYITEM
    lab_coat_keycard = """
    You cross the cold, eerie room, and pick up the bloodied
    lab coat from its place on the floor. You find a keycard in the 
    inner pocket.\n
    The keycard is labeled "Level 3 Clearance – Containment Access."\n
    """
    print(lab_coat_keycard)
    return "keycard"


def take_scalpel():  # working #INVENTORYITEM
    scalpel_content = """
    You pick up the scalpel, not looking too closely at the stains on it that
    look like blood. You decide to take it with you.\n
    """
    print(scalpel_content)
    return "scalpel"


def take_knife():  # working #INVENTORYITEM
    knife_content = """
    You pick up the knife. It's rusted and blunt, but better than nothing.\n
    """
    print(knife_content)
    return "knife"


def energy_drink():  # working
    energy_drink_content = """
    You drink the energy drink. It tastes good, but the caffeine hits your
    system. Whatever nerves you felt before are heightened significantly,
    making you more jumpy.\n
    """
    print(energy_drink_content)


def security_logs():  # working
    security_logs_content = """
    You move closer to the desk and scan the papers strewn across it. 
    One catches your eye, so you take a closer look:

        April 29th, 1998 - 23:15
        - Movement detected in the lower levels. Subject appears to be testing 
        the containment barrier.

        April 30th, 1998 - 02:30
        - Subject has breached the secondary containment unit. Lockdown 
        initiated in zones 4 and 5.

        April 30th, 1998 - 04:00
        - Security personnel dispatched to subdue the subject. No contact 
        since last report.

        April 30th, 1998 - 05:45
        - Emergency power activated. All non-essential systems offline. 
        Facility personnel ordered to secure keycards and await further 
        instructions.

        April 30th, 1998 - 06:00
        - Major breach reported in the Containment Room. Subject last seen
        heading toward the maintenance tunnels. Lockdown protocols failing.\n
    """
    print(security_logs_content)


def security_panel():
    security_panel_content = """
    The screen glitches and the cover is dusty, making it difficult to 
    decipher much. The cover is also conceals a large red button labelled:\n
        'INITIATE LOCKDOWN SEQUENCE'\n
    You debate pressing it, but you sense something silently moving behind 
    you. Your suspicions are confirmed by a faint clink of broken glass.\n
    """
    print(security_panel_content)


def choices_main():
    """
    Responsible for calling all the choices functions.
    """
    examine_desk()
    take_crowbar()
    read_notebook()
    inspect_toolbox()
    read_logbook()
    examine_computers()
    take_key()
    examine_lab_coat()
    take_scalpel()
    take_knife()
    energy_drink()
    security_logs()
    security_panel()
    investigate_mirror()
