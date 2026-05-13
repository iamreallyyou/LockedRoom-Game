# ==============================
# 🔒 LOCKED ROOM GAME 🔒
# A mystery puzzle adventure
# ==============================

inventory = []

def show_status(room):
    print("\n" + "=" * 40)
    print(f"📍 Location: {room}")
    if inventory:
        print(f"🎒 Inventory: {', '.join(inventory)}")
    else:
        print("🎒 Inventory: (empty)")
    print("=" * 40)

def ask(prompt, valid_choices):
    while True:
        choice = input(prompt)
        if choice in valid_choices:
            return choice
        print("❌ Invalid choice. Try again.")

# ==============================
# ROOM 1: DARK ROOM
# ==============================
def room_dark():
    show_status("Dark Room")
    print("\nYou wake up on a cold floor.")
    print("It's pitch black. Your hands are shaking.")
    print("You feel something in your pocket...")

    choice = ask("\n1: Check your pocket\n2: Crawl around blindly\nChoose: ", ["1", "2"])

    if choice == "2":
        print("\nYou crawl into a wall. Hard.")
        print("You pass out again. (BAD ENDING ☠️)")
        return False

    print("\nYou pull out a LIGHTER from your pocket.")
    inventory.append("LIGHTER")

    show_status("Dark Room")
    print("\nThe lighter reveals the room.")
    print("You see: a VENT on the wall, a DOOR with a keypad, and a DESK.")

    choice = ask("\n1: Inspect the vent\n2: Try the keypad\n3: Search the desk\nChoose: ", ["1", "2", "3"])

    if choice == "1":
        print("\nThe vent is screwed shut. You need a tool.")

    elif choice == "2":
        print("\nThe keypad blinks red. You need a code.")

    if choice == "3" or choice in ["1", "2"]:
        print("\nYou search the desk and find a SCREWDRIVER and a torn NOTE.")
        print("The note reads: 'The code is where knowledge lives.'")
        inventory.append("SCREWDRIVER")
        inventory.append("NOTE: code is where knowledge lives")

    show_status("Dark Room")
    print("\nWhat do you do now?")
    choice2 = ask("1: Use screwdriver on vent\n2: Try keypad again\nChoose: ", ["1", "2"])

    if choice2 == "2":
        print("\nYou don't have the code yet. The door stays locked. (BAD ENDING ☠️)")
        return False

    print("\nYou unscrew the vent and crawl through a dark tunnel...")
    print("You emerge into a dimly lit room.")
    return True

# ==============================
# ROOM 2: THE LAB
# ==============================
def room_lab():
    show_status("The Lab")
    print("\nThe room smells like chemicals.")
    print("There are 3 tables: RED, BLUE, GREEN.")
    print("On the wall: a locked CABINET and a strange MACHINE.")

    choice = ask("\n1: Examine red table\n2: Examine blue table\n3: Examine green table\n4: Try the cabinet\nChoose: ", ["1", "2", "3", "4"])

    found_clue = False

    if choice == "1":
        print("\nBroken glass. Nothing useful.")
    elif choice == "2":
        print("\nYou find a VIAL with a blue liquid. Could be useful.")
        inventory.append("BLUE VIAL")
        found_clue = True
    elif choice == "3":
        print("\nA notebook! It says: 'Mix blue + heat = unlock'")
        inventory.append("LAB NOTEBOOK")
        found_clue = True
    elif choice == "4":
        print("\nThe cabinet is sealed with a chemical lock.")

    if not found_clue:
        print("\nYou search more and eventually find the BLUE VIAL and LAB NOTEBOOK.")
        if "BLUE VIAL" not in inventory:
            inventory.append("BLUE VIAL")
        if "LAB NOTEBOOK" not in inventory:
            inventory.append("LAB NOTEBOOK")

    show_status("The Lab")
    print("\nThe machine has a slot for a vial and a heat button.")
    choice2 = ask("\n1: Insert blue vial and press heat\n2: Leave the machine alone\nChoose: ", ["1", "2"])

    if choice2 == "2":
        print("\nYou ignore the machine and find no way forward. (BAD ENDING ☠️)")
        return False

    print("\nThe machine hisses. The cabinet UNLOCKS.")
    print("Inside: a KEY CARD and a map of the building.")
    inventory.append("KEY CARD")
    inventory.append("BUILDING MAP")

    show_status("The Lab")
    print("\nThe map shows a LIBRARY next door.")
    print("The key card can open it.")
    return True

# ==============================
# ROOM 3: THE LIBRARY
# ==============================
def room_library():
    show_status("The Library")
    print("\nRows of dusty books surround you.")
    print("'The code is where knowledge lives' — the note from Room 1.")
    print("\nYou see shelves labeled: SCIENCE, HISTORY, MYSTERY")

    choice = ask("\n1: Search SCIENCE shelf\n2: Search HISTORY shelf\n3: Search MYSTERY shelf\nChoose: ", ["1", "2", "3"])

    if choice == "1":
        print("\nScience books... nothing hidden.")
    elif choice == "2":
        print("\nHistory books... you find an old PHOTOGRAPH but no code.")
        inventory.append("OLD PHOTOGRAPH")
    elif choice == "3":
        print("\nA mystery novel falls open. Inside: '4891'")
        print("That must be the keypad code from Room 1!")
        inventory.append("CODE: 4891")

    if "CODE: 4891" not in inventory:
        show_status("The Library")
        print("\nYou keep searching...")
        choice2 = ask("1: Search MYSTERY shelf\n2: Give up\nChoose: ", ["1", "2"])

        if choice2 == "2":
            print("\nYou sit down and cry. (BAD ENDING ☠️)")
            return False

        print("\nThe mystery novel falls open. Inside: '4891'")
        inventory.append("CODE: 4891")

    show_status("The Library")
    print("\nYou now have the code. Time to go back.")
    print("But wait — there's a LOCKED DRAWER under the main desk.")

    choice3 = ask("\n1: Try to open the drawer\n2: Head straight to the exit\nChoose: ", ["1", "2"])

    if choice3 == "1":
        print("\nThe drawer is locked tight. You notice a keyhole shaped like a photograph...")
        if "OLD PHOTOGRAPH" in inventory:
            print("You slide the photograph in. *CLICK*")
            print("Inside: a SECRET BADGE with your name on it.")
            inventory.append("SECRET BADGE")
            print("How does someone here know your name?! 😱")
        else:
            print("You can't open it without the right key.")

    return True

# ==============================
# ROOM 4: EXIT HALL
# ==============================
def room_exit():
    show_status("Exit Hall")
    print("\nA long corridor. At the end: THE EXIT DOOR.")
    print("Next to it: the KEYPAD from Room 1 (same system).")
    print("And a SECURITY CAMERA watching you.")

    choice = ask("\n1: Enter code on keypad\n2: Smash the camera first\n3: Look for another way\nChoose: ", ["1", "2", "3"])

    if choice == "2":
        print("\nYou smash the camera. An alarm goes off.")
        print("Guards arrive in 30 seconds. You panic. (BAD ENDING ☠️)")
        return "bad"

    if choice == "3":
        print("\nYou find a side window. It's small but you could fit.")
        if "SECRET BADGE" in inventory:
            print("Your secret badge has a chip — it unlocks the window latch!")
            print("\nYou slip out through the window undetected.")
            print("\n🏆 (TRUE ENDING — You escaped AND kept your identity secret!) 🏆")
            return "true"
        else:
            print("The window is sealed. No way through.")

    if "CODE: 4891" not in inventory:
        print("\nYou don't remember the code. You stand there forever. (BAD ENDING ☠️)")
        return "bad"

    print("\nYou type: 4-8-9-1")
    print("*BEEP BEEP* — GREEN LIGHT")
    print("The door unlocks.")

    if "SECRET BADGE" in inventory:
        print("\nAs you step out, you look at the badge.")
        print("Someone set this whole thing up... and they know who you are.")
        print("\n✨ (SECRET ENDING — You're free, but the mystery isn't over...) ✨")
        return "secret"
    else:
        print("\nSunlight. Fresh air. Freedom.")
        print("\n🎉 (GOOD ENDING — You escaped!) 🎉")
        return "good"

# ==============================
# MAIN GAME
# ==============================
def main():
    print("\n" + "=" * 40)
    print("     🔍 LOCKED ROOM GAME v2.0")
    print("      A Mystery Puzzle Adventure")
    print("=" * 40)
    print("\nSomeone locked you in. You don't know why.")
    print("You need to think carefully to escape.")
    print("\n[TIP: Collect items. Read clues. Use your brain.]")
    input("\nPress Enter to begin...\n")

    if not room_dark():
        return
    if not room_lab():
        return
    if not room_library():
        return

    ending = room_exit()

    print("\n" + "=" * 40)
    if ending == "true":
        print("ENDINGS FOUND: TRUE ENDING 🏆 (Rarest!)")
    elif ending == "secret":
        print("ENDINGS FOUND: SECRET ENDING ✨ (Try again for TRUE ending!)")
    elif ending == "good":
        print("ENDINGS FOUND: GOOD ENDING 🎉 (2 more endings to find!)")
    else:
        print("ENDINGS FOUND: BAD ENDING ☠️ (Try again!)")
    print("=" * 40)

main()
print("\nThanks for playing! 🔒")
input("Press Enter to exit...")
