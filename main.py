import sys
import json
import time as t
from func import clear
from colorama import Fore as f
from colorama import  Style as s

# the homescreen the palyer is presented with
def homescreen():

  # tells us the the player is in room 0
  global data
  data = {
    'Room' : 0,
    'fe1'  : 1,
    'fe2'  : 1,
    'fe3'  : 1
  }

  command_list = ('save - saves the game\n quit - quits the game\n go back - takes you to the previous room you were in')

  print(f.BLUE +'------------------')
  print(' The Wills of Men' )
  print('------------------'+ s.RESET_ALL)

  start_text = ('\nType start to begin your adventure or load to countinue your adventure. Remeber type save to save and quit to quit at any point\n')

  for char in start_text:
    sys.stdout.write(char)
    sys.stdout.flush()
    t.sleep(0.08)

# recives and converts answer to lower case
  answer = input(">").lower()

  if 'start' in answer:

    #creates save data
    with open('save.txt', 'w') as save:
      json.dump(data, save)

    print('\nIt Begins')

    t.sleep(4)

    clear()
    
    start()

  elif 'help' in answer:
    print(command_list) 

  elif 'load' in answer:
    try:
      with open('save.txt') as save:
        data = json.load(save)
    except:
      print(' no previous save ')
    Room_Check()
    

    
# starting function
def start():

  clear()

  data['Room'] = 1

  # beginning text for the player
  print(f.GREEN +'DARK ROOM'+ s.RESET_ALL)
  if data['fe1'] == 1:

    data['fe1'] = 0

    save()


    t.sleep(1)
    print('\n Suddenly you wake into a dark cave. its pitch black but you begin to feel your way around the room ')
    t.sleep(3)
    print(' you find two doors one to the left one to the right')
    
  t.sleep(1)
  print('\n l for left r for right or look to explore some more\n')

  # recives and converts answer to lower case
  answer = input(">").lower()

# sends the player left
  if 'l' in answer:
    clear()
    print('you go left')
    t.sleep(3)
    lake_room()
    
# sends the player right
  elif 'r' in answer:
    clear()
    print('you go right')
    t.sleep(3)
    abandoned_forge()

  elif 'save' in answer:
    save()

  elif 'quit' in answer:
    quit()

# player death condition
  else:
    game_over('you died of boredom') # so did I

# room 2's function
def lake_room():

  # clears page for new room
  clear()

  # room's title
  print('LAKE OF DREAMS')
  print('\nYou walk into a dimly lit room. in the center is a glowing blue lake which does not appear to relfect the cave. On the wall there is an unlit Torch with something behind it ')

# room 3's function
def abandoned_forge():
  # clears page for neew room
  clear()
  # rooms title
  print('ABANDONED FORGE')
  # room outline for player
  print('\nYou walk into a new room. It appears to be an old forge with old will forging equipment and an anvil. there is a thin been of light coming into the room from a man made hole in the ceiling. in the corner there is a barrel of coal')

# kills the player when triggered
def game_over(reason):
  #why the player is killed
  print(reason)
  t.sleep(1)
  print('\nGAME OVER')

def save():
  with open('save.txt', 'w') as save:
      json.dump(data, save)

      Room_Check()

def quit():
  print ('do you want to save before quitting? y/n')

  answer = input(">").lower()

  if 'y' in answer:
    print('saving and exiting')
    save()
  elif 'n' in answer:
    print('ok if you say so')

def go_back():
  if data['Room'] == 1:
    print('no')
  if data['Room'] == 2:
    start()
  if data['Room'] == 3:
    start()


def Room_Check():
  if data['Room'] == 1:
    start()
  if data['Room'] == 2:
    lake_room()
  if data['Room'] == 3:
    abandoned_forge()
    


# begins it all (calls homescreen function)
homescreen()
