import time as t

def start():
 
  #beginning text for the player
  print('\n Suddenly you wake into a dark cave. its pitch black but you begin to feel your way around the room ')
  t.sleep(3)
  print(' you find two doors one to the left one to the right')
  t.sleep(1)
  print('\n l for left r for right or look to explore some more\n')

  # recives and converst answer
  answer = input(">").lower()

#sends the player left
  if 'l' in answer:
    
    print('you go left')
    room_2()
    
#sends the player left
  elif 'r' in answer:
  
    print('you go right')
    room_3()
  
  else:
    game_over("you died of boredom")

def room_2():
  print('hi this is unfinished')

def room_3():
  print('hi this is unfinished')

def game_over():
  print('GAME OVER')
start()

