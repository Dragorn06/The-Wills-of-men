"""
T H E   W I L L S   O F   M E N
A high fantasy text adventure game
by Dragorn06
"""

import sys
import json
import time as t
from os import system, name
from colorama import Fore as f
from colorama import Style as s

# all possible save data
data = {
    'Room': 0,
    'fe1': 1,
    'fe2': 1,
    'fe3': 1,
    'has_key': 0,
    'door_found': 0,
    'torch': 0,
    'coal_bucket': 0
}


# the different 'rooms'
def home_screen():
    # tells us the the player is in room 0
    global data

    # title
    print(f'{f.BLUE}------------------')
    print(' The Wills of Men')
    print(f'------------------{s.RESET_ALL}')

    start_text = (
        '\nType start to begin your adventure or load to countinue your adventure. Remember type save to save and quit '
        'to quit at any point\n')

    for char in start_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        t.sleep(0.03)

    while True:
        # receives and converts answer to lower case
        answer = input("\n>").lower()

        # checks for start command
        if 'start' in answer:

            # creates save data
            with open('save.json', 'w') as save:
                json.dump(data, save)

            print('\nIt Begins')

            t.sleep(4)

            clear()

            # begins Room 1
            start()

        # checks for load command
        elif 'load' in answer:
            # tries to load a save
            with open('save.json') as save:
                data = json.load(save)
            room_check()

        elif 'quit' in answer:
            # asks the player i they want to save
            print('do you want to save before quitting? y/n')

            answer = input(">").lower()

            # if y saves the game and quits
            if 'y' in answer:
                print('exiting')
                with open('save.json', 'w') as save:
                    json.dump(data, save)
                    exit()

            elif 'n' in answer:
                exit()


# starting function
def start():
    clear()

    # tells the code we are in room 1
    data['Room'] = 1

    # Room title
    print(f.GREEN + 'DARK ROOM' + s.RESET_ALL)

    # prints this if you have been here before
    if data['fe1'] == 0:
        print(
            "\nyou're back in the dark room, its pitch black but you can feel your way around"
        )

    # checks if this is your first entry
    if data['fe1'] == 1:
        data['fe1'] = 0

        with open('save.json', 'w') as save:
            json.dump(data, save)

        t.sleep(1)
        # Room outline
        print(
            '\nSuddenly you wake into a dark cave. its pitch black but you begin to feel your way around the room '
        )
        t.sleep(3)
        print(
            ' \nas you search you stumble two doors one to the left one to the right'
        )

    t.sleep(1)
    # suggested commands
    print(
        '\n "go left" for left or "go right" for right or "explore" to explore some more'
    )

    # Room 1 game loop
    while True:
        cmd_handler()


# room 2's function
def lake_room():
    data['Room'] = 2

    # clears page for new room
    clear()

    # room's title
    print(f.GREEN + 'LAKE OF DREAMS' + s.RESET_ALL)

    # checks if you have been here before
    if data['fe2'] == 0:
        print(
            '\nyou re-enter the Lake of Dreams. You again see the iridescent lake'
        )
        if data['torch'] == 0:
            print('\nOn the wall there is an lit Torch with something behind it')

    if data['fe2'] == 1:
        data['fe2'] = 0

        t.sleep(1)

        # room outline
        print(
            '\nYou walk into a dimly lit cavern. in the center is a glowing blue lake. On the wall there is an lit '
            'Torch with something behind it '
        )

    # room game loop
    while True:
        cmd_handler()


# room 3's function
def abandoned_forge():
    data['Room'] = 3

    # clears page for new room
    clear()

    # rooms title
    print(f.GREEN + 'ABANDONED FORGE' + s.RESET_ALL)
    if data['fe3'] == 0:
        print('you feel calm as you enter the forge')

        if data['coal_bucket'] == 0:
            print('\nin the corner there is a barrel of coal')
    if data['fe3'] == 1:
        data['fe3'] = 0
        t.sleep(1)

        # room outline for player
        print(
            '\nYou walk into a new room. It appears to be an old forge with old will forging equipment and an anvil. '
            'there is a thin been of light coming into the room from a man made hole in the ceiling. in the corner '
            'there is a barrel of coal')

    # Room 3 game loop
    while True:
        cmd_handler()


# kills the player when triggered

# general cammond related functions
def go_back():
    if data['Room'] == 1:
        print('no')
        start()
    if data['Room'] == 2:
        print('the dark room')
        start()
    if data['Room'] == 3:
        print('the dark room')
        start()


def room_check():
    # checks what room the player should be in and sends them there
    if data['Room'] == 1:
        start()
    elif data['Room'] == 2:
        lake_room()
    elif data['Room'] == 3:
        abandoned_forge()
    else:
        # creates new game if no room can be found
        print('failed to find load creating new game')
        t.sleep(3)
        start()


# clears the screen
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')


# handles all commands in the game
def cmd_handler():
    answer = input('\n>').lower()

    if 'go' in answer:

        if data['Room'] == 1:
            if 'left' in answer:
                clear()
                print('you go left')
                t.sleep(3)
                lake_room()
            elif 'right' in answer:
                clear()
                print('you go right')
                t.sleep(3)
                abandoned_forge()

        elif data['Room'] == 2:
            if 'back' in answer:
                go_back()

        elif data['Room'] == 3:
            if 'back' in answer:
                go_back()

    elif 'get' in answer:

        if data['Room'] == 1:
            print('')

        if data['Room'] == 2:
            if 'torch' in answer:
                # checks torch status
                if data['torch'] == 0:
                    # changes torch status
                    data['torch'] = 1
                    print('You grab the torch.')

        if data['Room'] == 3:
            if 'coal' in answer:
                if data['coal_bucket'] == 0:
                    data['coal_bucket'] = 1
                    print('you grab the barrel of coal')

            if 'key' in answer:
                if data['has_key'] == 0:
                    data['has_key'] = 1
                    print('You get the key from the anvil.')
                    print(f'\nOn it there is an inscription . {f.BLUE} "The way to light is found in the darkest places"{s.RESET_ALL}')

    elif 'open' in answer:

        if data['Room'] == 1:
            if 'open door' in answer:
                # check if the player has found the door and has the key
                if data['has_key'] == 1 and data['door_found'] == 1:
                    print(
                        '\nThe door flies open and you are blinded by the light of the outside world'
                    )

                    t.sleep(10)

                    clear()

                    print(
                        "\nYou've finished 0.2.1 of The Wills of Men. Thank you for playing!! "
                    )

                    t.sleep(10)

                    with open('save.json', 'w') as save:
                        json.dump(data, save)

                        clear()

                    home_screen()

        if data['Room'] == 2:
            print('')

        if data['Room'] == 3:
            print('')

    elif 'light' in answer:

        if data['Room'] == 1:
            print('')

        if data['Room'] == 2:
            print('')

        if data['Room'] == 3:
            if 'forge' or 'fire' in answer:
                if data['torch'] == 1 and data['coal_bucket'] == 1:
                    t.sleep(2)
                    print(f'\nAs you place the coal in the forge and light the fire with your torch you feel a great '
                          f'increase in your power {f.YELLOW} Somewhere you can feel a way outsides {s.RESET_ALL} ')

                    t.sleep(1)

                    print('\na key materialises on the anvil')

    elif 'explore' in answer:

        if data['Room'] == 1:
            if 'explore' in answer:
                # if they have a torch they find something
                if data['torch'] == 1:
                    print(
                        '\n you look around and find what appears to be a key hole in the wall'
                    )
                    data['door_found'] = 1

        if data['Room'] == 2:
            print('')

        if data['Room'] == 3:
            print('')
    elif 'save' in answer:
        with open('save.json', 'w') as save:
            json.dump(data, save)
            print('\nSaved!')

    elif 'quit' in answer:
        # asks the player i they want to save
        print('do you want to save before quitting? y/n')

        answer = input(">").lower()

        # if y saves the game and quits
        if 'y' in answer:
            print('saving and exiting')
            with open('save.json', 'w') as save:
                json.dump(data, save)
                exit()

        elif 'n' in answer:
            print('if you say so')
            exit()

    else:
        print(f'{f.RED} Syntax error{s.RESET_ALL}')


# calls the script
if __name__ == "__main__":
    home_screen()
