def Project2():
    CMD_BED = 'b'
    CMD_CLOSE = 'c'
    CMD_EAST = 'e'
    CMD_FEED = 'f'
    CMD_GET = 'g'
    CMD_LOCK = 'l'
    CMD_NORTH = 'n'
    CMD_OPEN = 'o'
    CMD_PUT = 'p'
    CMD_QUIT = 'q'
    CMD_SOUTH = 's'
    CMD_TV = 't'
    CMD_UNLOCK = 'u'
    CMD_WEST = 'w'

    ROOM_FRONT = 0
    ROOM_LIVING = 1
    ROOM_KITCHEN = 2
    ROOM_OFFICE = 3
    ROOM_BED = 4

    ROOM_NAMES = ("Front Door", "Living Room", "Kitchen", "Office", "Bedroom")

    flag_me_awake = True
    flag_tv_on = False
    has_bone = False
    stella_is_hungry = True
    pantry_door_open = False
    has_key = False
    pantry_unlocked = False
    safe_open = False

    room = 0
    turn = 0

    print("What an awful day! You are completely exhausted, all you want to do is climb into bed and collapse. Unfortunately, that is easier said than done…")
    print()
    print("CIIC 3015 Autumn 2021 Project 2: Time For Go-To-Bed")
    print()

    while flag_me_awake:
        print("Location: ", ROOM_NAMES[room])
        cmd = input("> ")
        turn += 1

        if cmd == CMD_QUIT:
            print("You pass out on the floor and ignore all of your surroundings like the lazy person you are.")
            print("You have quit the game.")
            return False

        if room == ROOM_FRONT:
            if cmd == CMD_EAST:
                if flag_tv_on == False:
                    print("You enter the living room.")
                    print('The tv is off.')
                    room = ROOM_LIVING
                    if stella_is_hungry == True:
                        print("Stella is looking very sad and hungry.")
                    elif stella_is_hungry == False:
                        print('Stella is going ham on her food.')
                    continue
                elif stella_is_hungry == True:
                    print("You enter the living room.")
                    print('Stella is looking very sad and hungry.')
                    room = ROOM_LIVING
                    if flag_tv_on == False:
                        print('The tv is off.')
                    elif flag_tv_on == True:
                        print('The tv is on.')
                    continue
                elif flag_tv_on == True:
                    print("You enter the living room.")
                    print('The tv is on.')
                    room = ROOM_LIVING
                    if stella_is_hungry == True:
                        print("Stella is looking very sad and hungry.")
                    elif stella_is_hungry == False:
                        print('Stella is going ham on her food.')
                    continue
                elif stella_is_hungry == False:
                    print("You enter the living room.")
                    print('Stella is going ham on her food.')
                    room = ROOM_LIVING
                    if flag_tv_on == False:
                        print('The tv is off.')
                    elif flag_tv_on == True:
                        print('The tv is on.')
                    continue
            elif cmd == CMD_WEST:
                print("You are way too tired to face the world again just now. Best to remain indoors.")
                continue
            else:
                print("illegal command.")
                continue
            return

        if room == ROOM_LIVING:
            if cmd == CMD_SOUTH:
                if pantry_door_open == False:
                    print('You enter the kitchen')
                    print('The pantry door is closed.')
                    room = ROOM_KITCHEN
                    continue
                elif pantry_door_open == True:
                    print('You enter the kitchen')
                    print("The pantry door is open.")
                    room = ROOM_KITCHEN
                    continue
            elif cmd == CMD_EAST:
                if has_key == False:
                    print('You enter the office.')
                    print('The office safe is closed.')
                    room = ROOM_OFFICE
                    continue
                elif has_key == True:
                    print("You enter the office.")
                    print("The office safe is open.")
                    room = ROOM_OFFICE
                    continue
            elif cmd == CMD_NORTH:
                if stella_is_hungry == True:
                    print("Stella blocks your path, she appears to be really hungry.")
                    continue
                elif stella_is_hungry == False:
                    print("Stella is happy chewing the bone. You may enter your bedroom.")
                    room = ROOM_BED
                    continue
            elif cmd == CMD_TV:
                if flag_tv_on == True:
                    print("You turn off the tv.")
                    flag_tv_on = False
                    continue
                elif flag_tv_on == False:
                    print("You turn on the tv.")
                    flag_tv_on = True
                    continue
            elif cmd == CMD_WEST:
                print("You are way too tired to face the world again just now. Best to remain indoors.")
                continue
            elif cmd == CMD_FEED and has_bone == True and flag_tv_on == False:
                print("Stella seems tense. She keeps glancing from the bone in your hand, to the silent tv, to you, and back to the silent tv again. Every now and then she makes a sad little noise.")
                room = ROOM_LIVING
                continue
            elif cmd == CMD_FEED and has_bone == True and flag_tv_on == True:
                print("Stella hungrily snatches the nice tasty bone out of your hand and starts\nto chew on it. She no longer seems to notice or care\nthat you are here.")
                stella_is_hungry = False
                room = ROOM_LIVING
                continue
            else:
                print("Illegal command.")
                continue
            return

        if room == ROOM_KITCHEN:
            if cmd == CMD_OPEN and pantry_door_open == False:
                print('The pantry door is locked. It will not open')
                continue
            elif cmd == CMD_UNLOCK and pantry_door_open == False:
                print('You unlock the pantry door.\nA nice treat is inside.')
                pantry_unlocked = True
                pantry_door_open = True
                room = ROOM_KITCHEN
                continue
            if cmd == CMD_OPEN and pantry_unlocked == True and pantry_door_open == True:
                print("You open the pantry door.")
                pantry_door_open = True
                room = ROOM_KITCHEN
                continue
            if cmd == CMD_GET and pantry_door_open == True:
                print("You grab the tastiest dog treat for Stella. She watches you with great interest from the living room.")
                has_bone = True
                room = ROOM_KITCHEN
                continue
            if cmd == CMD_CLOSE and pantry_door_open == True:
                print("You close the pantry door.")
                pantry_door_open = False
                room == ROOM_KITCHEN
                continue
            if cmd == CMD_LOCK and pantry_door_open == False:
                print("You lock the pantry door with the key.")
                pantry_unlocked = False
                room = ROOM_KITCHEN
                continue
            elif cmd == CMD_NORTH:
                if flag_tv_on == False:
                    print("You enter the living room.")
                    print('The tv is off.')
                    room = ROOM_LIVING
                    if stella_is_hungry == True:
                        print("Stella is looking very sad and hungry.")
                    elif stella_is_hungry == False:
                        print('Stella is going ham on her food.')
                    continue
                elif stella_is_hungry == True:
                    print("You enter the living room.")
                    print('Stella is looking very sad and hungry.')
                    room = ROOM_LIVING
                    if flag_tv_on == False:
                        print('The tv is off.')
                    elif flag_tv_on == True:
                        print('The tv is on.')
                    continue
                elif flag_tv_on == True:
                    print("You enter the living room.")
                    print('The tv is on.')
                    room = ROOM_LIVING
                    if stella_is_hungry == True:
                        print("Stella is looking very sad and hungry.")
                    elif stella_is_hungry == False:
                        print('Stella is going ham on her food.')
                    continue
                elif stella_is_hungry == False:
                    print("You enter the living room.")
                    print('Stella is going ham on her food.')
                    room = ROOM_LIVING
                    if flag_tv_on == False:
                        print('The tv is off.')
                    elif flag_tv_on == True:
                        print('The tv is on.')
                    continue
            else:
                print("illegal comand")
                continue
            return

        if room == ROOM_OFFICE:
            if cmd == CMD_OPEN and safe_open == False:
                print('Please enter the combination to the safe, one number at a time.\nYou remember that it is the next three numbers in the Collatz\nsequence after 42')
                firstNumber = int(input('First number? '))
                secondNumber = int(input('Second number? '))
                thirdNumber = int(input("Third number? "))
                if firstNumber != 21 or secondNumber != 64 or thirdNumber != 32:
                    print('Nope. That is not it. The locked safe silently mocks you.')
                    room = ROOM_OFFICE
                    yield False
                elif firstNumber == 21 and secondNumber == 64 and thirdNumber == 32:
                    print("You hear a satisfying 'Ka-CHUNK' as the handle turns and the safe\ndoor swings invitingly open. ")
                    print("Inside you see the pantry door key.")
                    safe_open = True
                    room = ROOM_OFFICE
                    continue
            if cmd == CMD_OPEN and safe_open == True:
                print("The safe is already open, dummy.")
                continue
            elif cmd == CMD_GET and safe_open == True:
                print("You remove the pantry door key from the safe.")
                has_key = True
                room == ROOM_OFFICE
                continue
            elif cmd == CMD_PUT and has_key == True:
                print("You put the pantry door key back into the safe.")
                has_key = False
                safe_open = False
                room = ROOM_OFFICE
                continue
            if cmd == CMD_WEST:
                if flag_tv_on == False:
                    print("You enter the living room.")
                    print('The tv is off.')
                    room = ROOM_LIVING
                    if stella_is_hungry == True:
                        print("Stella is looking very sad and hungry.")
                    elif stella_is_hungry == False:
                        print('Stella is going ham on her food.')
                    continue
                elif stella_is_hungry == True:
                    print("You enter the living room.")
                    print('Stella is looking very sad and hungry.')
                    room = ROOM_LIVING
                    if flag_tv_on == False:
                        print('The tv is off.')
                    elif flag_tv_on == True:
                        print('The tv is on.')
                    continue
                elif flag_tv_on == True:
                    print("You enter the living room.")
                    print('The tv is on.')
                    room = ROOM_LIVING
                    if stella_is_hungry == True:
                        print("Stella is looking very sad and hungry.")
                    elif stella_is_hungry == False:
                        print('Stella is going ham on her food.')
                    continue
                elif stella_is_hungry == False:
                    print("You enter the living room.")
                    print('Stella is going ham on her food.')
                    room = ROOM_LIVING
                    if flag_tv_on == False:
                        print('The tv is off.')
                    elif flag_tv_on == True:
                        print('The tv is on.')
                    continue
                else:
                    print("Illegal command.")
                    continue
            return

        if room == ROOM_BED:
            if cmd == CMD_SOUTH:
                if flag_tv_on == False:
                    print("You enter the living room.")
                    print('The tv is off.')
                    room = ROOM_LIVING
                    continue
                elif flag_tv_on == True:
                    print("You enter the living room.")
                    print('The tv is on.')
                    room = ROOM_LIVING
                    continue
                elif stella_is_hungry == False:
                    print("You enter the living room.")
                    print('Stella is going ham on her food.')
                    room = ROOM_LIVING
                    continue
                return
            elif flag_tv_on == True:
                print("You hear a faint noise coming from the living room, keeping you awake.")
                room = ROOM_BED
                yield False
            elif pantry_door_open == True:
                print("You remember that your pantry door is open, thus your crippling anxiety keeps you awake.")
                room = ROOM_BED
                yield False
            elif has_key == True:
                print("You realize that you still have the key from the safe on you, better put that back where it belongs!")
                room = ROOM_BED
                yield False
            elif cmd == CMD_BED and flag_tv_on == True and pantry_door_open == True and has_key == True and pantry_unlocked == True:
                print("You cannot fall asleep yet.")
                room = ROOM_BED
                yield False
            elif cmd == CMD_BED and flag_tv_on == False and pantry_door_open == False and has_key == False and pantry_unlocked == False:
                print('Sleep at last! You win!')
                print(turn, "turns played.")
                return True
Project2()
