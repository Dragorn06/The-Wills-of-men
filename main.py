import time as t
from os import system, name

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux
    else:
        _ = system('clear')
  
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
    t.sleep(5)
    lake_room()
    
#sends the player right
  elif 'r' in answer:
    clear()
    print('you go right')
    t.sleep(5)
    abandoned_forge()

#player death condition
  else:
    game_over('you died of boredom') # so did I

#room 2's function
def lake_room():
  print('LAKE OF DREAMS')
  print('hi this is unfinished')

#room 3's function
def abandoned_forge():
  print('hi this is unfinished')

#kills the player when triggered
def game_over(reason):
  print(reason)
  t.sleep(1)
  print('\nGAME OVER')

#begins it all (calls start function)
start()