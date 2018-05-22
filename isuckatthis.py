from sys import exit
import time
import random
from textwrap import dedent

# Retried variable -- True if player restarts game without closing
# Few extra easter eggs if True
retried = False

punched_window = False

# GAME MECHANIC FUNCTIONS------------------------

# 'Press enter to continue' function. Chastises player if they type anything.
def cont():
    a = input("*")
    if a != "":
        print("(You're not supposed to type anything here)")
        print('')
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
    global punched_window
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
        print('')

    print("It\'s dark. A single dimly lit bulb hangs from the ceiling -- the room\'s only light source.")
    cont()
    print("You're dizzy. Someone must have drugged you.")
    cont()
    print("You sit up and look around. You\'re in a hospital room.")
    cont()
    print("There is a door across the room.")

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

    crowbar = [
        'crowbar',
        'use crowbar',
        'smash window with crowbar',
        'smash glass with crowbar',
        'smash door window with crowbar',
        'smash door glass with crowbar',
        'break window with crowbar',
        'break door window with crowbar',
        'break glass with crowbar',
        'break door glass with crowbar',
    ]

    drugs = [
        'drugs',
        'needles',
        'inject drugs',
        'inject needles',
        'do drugs',
        'take drugs',
        'take needles',
    ]

    throw_drugs = [
        'throw drugs',
        'throw needles',
        'throw needle',
        'smash window with needle',
        'smash window with drugs',
        'smash door window with needle',
        'smash door window with drugs',
        'break window with drugs',
        'break window with needle',
        'break door window with needle',
        'break door window with drugs',
        'break glass with drugs',
        'break glass with needle',
        'break door glass with drugs',
        'break door glass with needle',
    ]

    # Player input fail count
    ifc = 0

    # Tracks if player got up from bed from trying to unlock door.
    # Just for a tiny dialogue nitpick.
    got_up = False

    # First player action
    while True:
        print('')
        choice1 = input('What do you want to do? ')
        choice1 = choice1.lower()

        # Look around
        if choice1 == 'look around':
            print('You take a look around the room.')
            cont()
            print('You see that there is a crowbar on the counter to the side.')
            cont()
            print('Alternatively, there are some needles on the bedside stand.')
            input('*')

        # Try opening door
        elif choice1 == 'door' or choice1 == 'open door':
            got_up = True
            print('You get up from the bed and walk to the door.')
            cont()
            print("Strangely, the doorknob won\'t budge. It must be locked from the outside.")
            cont()
            print('The door has a window. Maybe you could smash it to reach the lock on the other side?')
            input('*')

        # Smash window w/fist
        elif choice1 in smash_glass:
            punched_window = True
            if got_up:
                print('You get up from the bed and walk to the door.')
                cont()
            print('You smash through the door window with your fist.')
            cont()
            print('Unsurprisingly, you get dozens of cuts from the glass.')
            cont()
            print('The pain is overwhelming.')
            cont()
            print('...And you eventually die of blood loss.')
            input('*')
            game_over()

        # Falcon punch window
        # (Player must have tried to smash window w/fist first)
        elif punched_window and choice1 in falcon_punch:
            print('You FALCON PUNCH through the door\'s window.')
            cont()
            print('However, Falcon Punches aren\'t immune to getting cut by glass...')
            input('*')
            game_over()

        # Smash window w/crowbar (correct action)
        elif choice1 in crowbar:
            print('You grab the crowbar off the counter and use it to smash the door window.')
            cont()
            print('You reach over and open the door from the other side.')
            cont()
            sequence2()
            break

        # Do drugs
        elif choice1 in drugs:
            print('You reach over to the needles on the stand to your left and violently jab yourself with one.')
            cont()
            print('You start to feel high, lighter than air!')
            cont()
            print('You get up and prance around the room with the feeling of bliss of the drugs in your bloodstream.')
            cont()
            print('...until it stops your heart.')
            cont()
            print('You obviously never learned that drugs are bad.')
            input('*')
            game_over()

        elif choice1 in throw_drugs:
            if not got_up:
                print('You reach over to the needles on the stand to your left and throw one at the door window.')
                cont()
            elif got_up:
                print('You go over to the stand by the bed and grab a needle.')
                cont()
                print("You throw it at the door's window.")
                cont()
            print("Unsurprisingly, it didn't to anything.")
            # Alternate: needle bounces back and drugs player
            input('*')

        # Hint
        elif choice1 == 'hint':
            print('Try looking around the room.')

        else:
            ifc += 1
            if ifc % 3 == 0:
                print('You know, you can type \'hint\' if you don\'t know what to do.')
            else:
                print('Yeah, I don\'t know what you\'re trying to do.')


def sequence2():
    print('YAY!')
    cont()
    print('U WINNER!')
    input('Press Enter to close')
    exit()



intro()
