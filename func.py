import json
from os import system, name

data = {
    'Room' : 0,
    'fe1'  : 1,
    'fe2'  : 1,
    'fe3'  : 1,
    'has_key' : 0,
    'door_found' : 0,
    'torch': 0,
    'coal_bucket': 0
  }

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')

def quit():
  print ('do you want to save before quitting? y/n')

  answer = input(">").lower()

  if 'y' in answer:
    print('saving and exiting')
    with open('save.json', 'w') as save:
      json.dump(data, save)
    
  elif 'n' in answer:
    print('ok if you say so')
