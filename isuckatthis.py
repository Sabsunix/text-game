from sys import exit
import time
import random
from textwrap import dedent

retried = False


# GAME MECHANIC FUNCTIONS------------------------

# 'Press enter to continue' function. Chastises player if they type anything.
def cont():
    a = input("*")
    if a != "":
        print("(You're not supposed to type anything here)")
    return


def game_over():
    global retried
    quips = [
        'Oof.',
        'Nice one, dude!',
    ]
    
    print("")
    print(random.choice(quips))
    print("You freakin' died!")

    # Retry y/n loop
    while True:
        retry = input("Try again? ")
        retry = retry.lower()

        if retry == 'y' or retry == 'yes' or retry == 'ye':
            retried = True
            print("")
            intro()
        elif retry == 'no' or retry == 'n' or retry == 'nah':
            exit()
        else:
            print("")
            print("Yes or no. Easy question.")


# STORY FUNCTIONS--------------------------------

def intro():
    global retried
    print("You awake on a bed in a room you've never seen before.")
    # Show tutorial if the game is rebooted.
    if not retried:
        print("(Press Enter whenever you see a * to continue.)")
    # cont() replacement
    lol = input('*')
    lol = lol.lower()
    
    # 'Getting mad at tutorial' easter egg
    if not retried and (lol == 'shut up' or lol == 'screw off'):
        print("Alright, fine. Geez.")
        input('*')
    elif lol != "":
        print("(You're not supposed to type anything here)")
    
    print("It\'s dark. A single dimly lit bulb hangs from the ceiling -- the room\'s only light source.")
    cont()
    print("You're dizzy. Someone must have drugged you.")
    cont()
    print("You sit up and take a look around. You\'re in a hospital room.")
    cont()
    print("There is a door accross the room.")

    smash_glass = [
        'smash glass',
        'smash window',
        'smash door glass',
        'smash door window',
        'break glass',
        'break window',
        'break door glass',
        'break door window',
    ]


    falcon_punch = [
        'falcon punch',
        'falcon punch glass',
        'falcon punch window',
        'falcon punch door glass',
        'falcon punch door window',            
    ]
    
    while True:
        print("")
        choice1 = input("What do you want to do? ")
        choice1 = choice1.lower()
        
        if choice1 == 'door' or choice1 == 'open door':
            print("Strangely, the doorknob won\'t budge. It must be locked from the outside.")

        elif choice1 in smash_glass:
            print("You smash through the door window with your fist.")
            cont()
            print("Unsurprisingly, you get dozens of cuts.")
            cont()
            print("The pain is overwhelming.")
            cont()
            print("And you eventually die of blood loss.")
            input("*")
            game_over()

        elif retried == True and choice1 in falcon_punch:
            print("You FALCON PUNCH the door's window.")
            cont()
            print("However, Falcon Punches aren't immune to getting cut by glass...")
            input("*")
            game_over()
            
        elif choice1 == 'drugs' or choice1 == 'needles':
                print(dedent("""
                You reach over to the needles on the counter to your left and violently jab yourself with one.
                You obviously never learned that drugs are bad.
                """))
                game_over()
                
        else:
                print("Yeah, I don\'t know what you\'re trying to do.")
                
intro()
