import time as t
from func import clear
import sys

#the homescreen the palyer is presented with
def homescreen():


  print('------------------')
  print(' The Wills of Men')
  print('------------------')

  start_text = ('\nType start to begin your adventure\n')

  for char in start_text:
    sys.stdout.write(char)
    sys.stdout.flush()
    t.sleep(0.08)

# recives and converts answer to lower case
  answer = input(">").lower()

  if 'start' in answer:

    print('It Begins')

    t.sleep(4)

    clear()
    
    start()

#starting function
def start():
  
  clear()

  #beginning text for the player
  print('DARK ROOM')
  t.sleep(1)
  print('\n Suddenly you wake into a dark cave. its pitch black but you begin to feel your way around the room ')
  t.sleep(3)
  print(' you find two doors one to the left one to the right')
  t.sleep(1)
  print('\n l for left r for right or look to explore some more\n')

  # recives and converts answer to lower case
  answer = input(">").lower()

#sends the player left
  if 'l' in answer:
    clear()
    print('you go left')
    t.sleep(3)
    lake_room()
    
#sends the player right
  elif 'r' in answer:
    clear()
    print('you go right')
    t.sleep(3)
    abandoned_forge()

#player death condition
  else:
    game_over('you died of boredom') # so did I

#room 2's function
def lake_room():
  #clears page for new room
  clear()
  #room's title
  print('LAKE OF DREAMS')
  print('\nYou walk into a dimly lit room. in the center is a glowing blue lake which does not appear to relfect the cave. On the wall the is an unlit note with something behind it ')

#room 3's function
def abandoned_forge():
  #clears page for neew room
  clear()
  #rooms title
  print('ABANDONED FORGE')
  #room outline for player
  print('\nYou walk into a new room. It appears to be an old forge with old will forging equipment and an anvil. there is a thin been of light coming into the room from a man made hole in the ceiling')

#kills the player when triggered
def game_over(reason):
  #why the player is killed
  print(reason)
  t.sleep(1)
  print('\nGAME OVER')

#begins it all (calls homescreen function)
homescreen()