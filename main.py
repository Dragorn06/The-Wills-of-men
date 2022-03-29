import sys
import json
import time as t
from functions import *
from colorama import Fore as f
from colorama import Style as s


# the homescreen the player is presented with
def homescreen():
    # tells us the the player is in room 0
    global data

    # help for the player
    command_list = (
        'save - saves the game\n quit - quits the game\n go back - takes you to the previous room you were in')

    # title
    print(f.BLUE + '------------------')
    print(' The Wills of Men')
    print('------------------' + s.RESET_ALL)

    start_text = (
        '\nType start to begin your adventure or load to countinue your adventure. Remeber type save to save and quit '
        'to quit at any point\n')

    for char in start_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        t.sleep(0.08)

    # recives and converts answer to lower case
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

    # prints command_list
    elif 'help' in answer:
        print(command_list)

    # checks for load command
    elif 'load' in answer:
        # tries to load a save
        try:
            with open('save.json') as save:
                data = json.load(save)
        except:
            print('')
            Room_Check()


# starting function
def start():
    clear()

    # tells the code we are in room 1
    data['Room'] = 1

    # Room title
    print(f.GREEN + 'DARK ROOM' + s.RESET_ALL)

    # prints this if you have been here before
    if data['fe1'] == 0:
        print("\nyou're back in the dark room")

    # checks if this is your first entry
    if data['fe1'] == 1:
        data['fe1'] = 0

        with open('save.json', 'w') as save:
            json.dump(data, save)

        t.sleep(1)
        # Room outline
        print('\n Suddenly you wake into a dark cave. its pitch black but you begin to feel your way around the room ')
        t.sleep(3)
        print(' \nyou find two doors one to the left one to the right')

    t.sleep(1)
    # suggested commands
    print('\n l for left r for right or look to explore some more')

    # Room 1 game loop
    while True:

        # recives and converts answer to lower case
        answer = input("\n>").lower()

        # sends the player left
        if 'l' == answer:
            clear()
            print('you go left')
            t.sleep(3)
            lake_room()

        # sends the player right
        elif 'r' == answer:
            clear()
            print('you go right')
            t.sleep(3)
            abandoned_forge()

        # the player explore the area
        elif 'look' == answer:
            # if they have a torch they find something
            if data['torch'] == 1:
                print('\n you look around and find what appears to be another door in the wall')
                data['door_found'] = 1

        # check for the open door command
        elif 'open door' == answer:
            # check if the playere has found the door and has the key
            if data['has_key'] == 1 and data['door_found'] == 1:
                print('The door flies open and you are blinded by the light of the outside world')

                t.sleep(2)

                print("You've finished 0.0.2 of The Wills of Men. Thank you for playing!! ")

                with open('save.json', 'w') as save:
                    json.dump(data, save)
                break

        # saves the game
        elif 'save' in answer:
            with open('save.json', 'w') as save:
                json.dump(data, save)
                print('Saved!')

        # sends player to quit function
        elif 'quit' in answer:
            quit1()

        # player death condition
        else:
            game_over('you died of boredom')  # so did I


# room 2's function
def lake_room():
    data['Room'] = 2

    # clears page for new room
    clear()

    # room's title
    print(f.GREEN + 'LAKE OF DREAMS' + s.RESET_ALL)

    # checks if you have been here before
    if data['fe2'] == 0:
        print('\nyou re-enter the Lake of Dreams')
        if data['torch'] == 0:
            print('\nOn the wall there is an lit Torch with something behind it')

    if data['fe2'] == 1:
        data['fe2'] = 0

        t.sleep(1)

        # room outline
        print(
            '\nYou walk into a dimly lit room. in the center is a glowing blue lake which does not appear to relfect '
            'the cave. On the wall there is an lit Torch with something behind it ')

    # room game loop
    while True:
        answer = input('\n>')

        # check for torch command
        if 'torch' in answer:

            # checks torch status
            if data['torch'] == 0:
                # changes torch status
                data['torch'] = 1
                print('You grab the torch, as it comes away from the wall something drops on the floor')

        # sends the player to the previous room
        elif 'go back' in answer:
            go_back()

        # saves the game
        elif 'save' in answer:
            with open('save.json', 'w') as save:
                json.dump(data, save)
                print('Saved!')

        # quits the game
        elif 'quit' in answer:
            quit1()


# room 3's function
def abandoned_forge():
    data['Room'] = 3

    # clears page for neew room
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
        answer = input('\n>')

        # sends the player to the previous room
        if 'go back' == answer:
            go_back()

        # saves the game
        elif 'save' == answer:
            with open('save.json', 'w') as save:
                json.dump(data, save)
                print('Saved!')

        # checks if the player wants to get the coal bucket
        elif 'get coal bucket' == answer:
            if data['coal_bucket'] == 0:
                data['coal_bucket'] = 1
                print('you grab the bucket of coal')

        # checks the player wants to light the forge
        elif 'light' or 'light forge' or 'light fire' == answer:
            if data['torch'] == 1 and data['coal_bucket'] == 1:
                t.sleep(2)
                print(
                    '\nAs you place the coal in the forge and light the fire you feel a great increase in your power ' + f.YELLOW + 'Somewhere a door to the outside can be found' + s.RESET_ALL, )

                t.sleep(1)

                print('\na key materialises on the anvil')

                t.sleep(1)

                print('\n do you want to pick it up y/n')

                answer = input('\n>')

                # check the player want the key
                if 'y' in answer:
                    data['has_key'] = 1
                    print('you get the key from the anvil.')
                    print(
                        '\n on it there is an inscription .' + f.RED +
                        '"The way to light is found in the darkest places"' + s.RESET_ALL)

                # the player says no (why would you)
                elif 'n' in answer:
                    print('ok')

        # quits the game
        elif 'quit' in answer:
            quit1()


# kills the player when triggered
def game_over(reason):
    # why the player is killed
    print(reason)
    t.sleep(1)
    print('\nGAME OVER')


# send the player to the previous room
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


# checks what room the player should be in and sends them there
def Room_Check():
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


# begins it all (calls home screen function)
homescreen()
