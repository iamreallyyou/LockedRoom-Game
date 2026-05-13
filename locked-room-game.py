print("=== LOCKED ROOM ===")
print("You wake up in a dark room.")

choice1 = input("\n1: Turn on the light\n2: Stay in the dark\nChoose: ")

if choice1 == "1":
    print("\nThe light flickers on. You see a door and a box.")
    
    choice2 = input("\n1: Open the door\n2: Open the box\nChoose: ")
    
    if choice2 == "1":
        print("\nThe door is locked. You are stuck forever. (BAD ENDING)")
    
    elif choice2 == "2":
        print("\nYou found a key inside the box!")
        print("You use the key to open the door and escape. (GOOD ENDING 🎉)")
    
    else:
        print("\nYou froze and did nothing. (BAD ENDING)")

elif choice1 == "2":
    print("\nYou trip over something in the dark and hit your head. (BAD ENDING)")

else:
    print("\nInvalid choice.")