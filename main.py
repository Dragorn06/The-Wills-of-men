"""
T H E   W I L L S   O F   M E N
A high fantasy text adventure game
by Dragorn06
"""

import sys
import json
import time as t
import os
from colorama import Fore as f
from colorama import Style as s


class Room:
    default = 0

    def __init__(self, num, fe):
        self.num = num
        self.has_entered = fe


class Item:
    def __init__(self, name, player_has):
        self.name = name
        self.player_has = player_has


class RoomObj(Item):
    def __init__(self, name, found):
        super().__init__(self, name)
        self.found = found


# rooms
Dark_Room = Room(1, False)
Lake_Room = Room(2, False)
Abandoned_Forge = Room(3, False)
Crossroads = Room(4, False)

# items
Torch = Item('Torch', False)
Coal_Barrel = Item('Barrel of coal', False)
key = Item('key', False)

# Object the player does not carry
Dark_Room_Door = RoomObj('door', False)

# all possible save data
data = {
    'Room': Room.default,
    'fe1': Dark_Room.has_entered,
    'fe2': Lake_Room.has_entered,
    'fe3': Abandoned_Forge.has_entered,
    'fe4': Crossroads.has_entered,
    'key': key.player_has,
    'door_found': Dark_Room_Door.found,
    'torch': Torch.player_has,
    'coal_bucket': Coal_Barrel.player_has
}


# the different 'rooms'
def home_screen():
    # tells us the player is in room 0
    global data

    # title
    print(f'{f.BLUE}------------------')
    print(' The Wills of Men')
    print(f'------------------{s.RESET_ALL}')

    start_text = (
        '\nType start to begin your adventure or load to continue your adventure. Remember type save to save and quit '
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

            os.system('clear')

            # begins Room 1
            dark_room()

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
def dark_room():
    os.system('clear')

    # tells the code we are in room 1
    data['Room'] = Dark_Room.num

    # Room title
    print(f.GREEN + 'DARK ROOM' + s.RESET_ALL)

    # prints this if you have been here before
    if data['fe1']:
        print(
            "\nyou're back in the dark room, its pitch black but you can feel your way around"
        )

    # checks if this is your first entry
    if not data['fe1']:
        Dark_Room.has_entered = False

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
    data['Room'] = Lake_Room.num

    # clears page for new room
    os.system('clear')

    # room's title
    print(f.GREEN + 'LAKE OF DREAMS' + s.RESET_ALL)

    # checks if you have been here before
    if data['fe2']:
        print(
            '\nyou re-enter the Lake of Dreams. You again see the iridescent lake'
        )
        if data['torch'] == 0:
            print('\nOn the wall there is an lit Torch with something behind it')

    if not data['fe2']:
        Lake_Room.has_entered = False

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
    data['Room'] = Abandoned_Forge.num

    # clears page for new room
    os.system('clear')

    # rooms title
    print(f.GREEN + 'ABANDONED FORGE' + s.RESET_ALL)
    if data['fe3']:
        print('you feel calm as you enter the forge')

        if data['coal_bucket'] == 0:
            print('\nin the corner there is a barrel of coal')
    if not data['fe3']:
        Abandoned_Forge.has_entered = True
        t.sleep(1)

        # room outline for player
        print(
            '\nYou walk into a new room. It appears to be an old forge with old will forging equipment and an anvil. '
            'there is a thin been of light coming into the room from a man made hole in the ceiling. in the corner '
            'there is a barrel of coal')

    # Room 3 game loop
    while True:
        cmd_handler()


# general command related functions
def go_back():
    if data['Room'] == 2 or 3:
        dark_room()


def room_check():
    # checks what room the player should be in and sends them there
    if data['Room'] == 1:
        dark_room()
    elif data['Room'] == 2:
        lake_room()
    elif data['Room'] == 3:
        abandoned_forge()
    else:
        # creates new game if no room can be found
        print('failed to find load creating new game')
        t.sleep(3)
        dark_room()


# handles all commands in the game
def cmd_handler():
    answer = input('\n>').lower()

    if 'go' in answer:

        if data['Room'] == 1:
            if 'left' in answer:
                os.system('clear')
                print('you go left')

                t.sleep(3)

                lake_room()

            if 'right' in answer:
                os.system('clear')
                print('you go right')

                t.sleep(3)

                abandoned_forge()

        if data['Room'] == 2:

            if 'back' in answer:
                go_back()

        if data['Room'] == 3:

            if 'back' in answer:
                go_back()

    if 'get' in answer:

        if data['Room'] == 1:
            print('')

        if data['Room'] == 2:

            if 'torch' in answer:

                # checks torch status
                if not data['torch']:
                    # changes torch status
                    data['torch'] = True
                    print('You grab the torch.')

        if data['Room'] == 3:
            if 'coal' in answer:
                if not data['coal_bucket']:
                    data['coal_bucket'] = True
                    print('you grab the barrel of coal')

            if 'key' in answer:
                if not data['key']:
                    data['key'] = True
                    print('You get the key from the anvil.')
                    print(
                        f'\nOn it there is an inscription . {f.BLUE} "The way to '
                        f'light is found in the darkest places"{s.RESET_ALL}'
                    )

    if 'open' in answer:

        if data['Room'] == 1:
            if 'open door' in answer:
                # check if the player has found the door and has the key
                if data['key'] and data['door_found']:
                    print(
                        '\nThe door flies open and you are blinded by the light of the outside world'
                    )

                    t.sleep(10)

                    os.system('clear')
                    print(
                        "\nYou've finished 0.2.1 of The Wills of Men. Thank you for playing!! "
                    )

                    t.sleep(10)

                    with open('save.json', 'w') as save:
                        json.dump(data, save)

                        os.system('clear')

                    home_screen()

        if data['Room'] == 2:
            print('')

        if data['Room'] == 3:
            print('')

    if 'light' in answer:

        if data['Room'] == 1:
            print('')

        if data['Room'] == 2:
            print('')

        if data['Room'] == 3:
            if 'forge' or 'fire' in answer:
                if data['torch'] and data['coal_bucket']:
                    t.sleep(2)
                    print(f'\nAs you place the coal in the forge and light the fire with your torch you feel a great '
                          f'increase in your power {f.YELLOW} Somewhere you can feel a way outsides {s.RESET_ALL} ')

                    t.sleep(1)

                    print('\na key materialises on the anvil')

    if 'explore' in answer:

        if data['Room'] == 1:
            if 'explore' in answer:
                # if they have a torch they find something
                if data['torch']:
                    print(
                        '\n you look around and find what appears to be a key hole in the wall'
                    )
                    data['door_found'] = True

        if data['Room'] == 2:
            print('')

        if data['Room'] == 3:
            print('')
    if 'save' in answer:
        with open('save.json', 'w') as save:
            json.dump(data, save)
            print('\nSaved!')

    if 'quit' in answer:
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


# calls the script
if __name__ == "__main__":
    home_screen()
