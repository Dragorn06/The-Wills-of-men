"""A collection of developer tools for making maps and debugging"""

import json

def add_room_json(filename):
  """Writes a room to a JSON file in the specified format, using the input() function to get the values for each field.

  Args:
    filename: The name of the JSON file to write to.
  """

  room_name = input("Enter the name of the room: ")
  room_id = input("Enter the room ID: ")
  description = input("Enter the description of the room: ")
  explore_text = input("Enter the text that is displayed when the player explores the room: ")

  exits = {}
  while True:
    direction = input("Enter a direction of an exit (or leave blank to finish): ")
    room = input("Enter the id of the room this takes you too (or leave blank to finish): ")
    print(room)
    if direction == "":
      break
    exits[f"{direction}"] = int(room)

  contents = []
  while True:
    item = input("Enter an item in the room (or leave blank to finish): ")
    if item == "":
      break
    contents.append(int(item))
  hidden_exits = []
  while True:
    exit = input("Enter a hidden exit from the room (or leave blank to finish): ")
    if exit == "":
      break
    hidden_exits.append(exit)
  locked_exits = []
  while True:
    exit = input("Enter a locked exit from the room (or leave blank to finish): ")
    if exit == "":
      break
    locked_exits.append(exit)

  room_data = {
    f"{room_id}": {
      "Name": room_name,
      "RoomId": int(room_id),
      "Description": description,
      "ExploreText": explore_text,
      "Exits": exits,
      "Contents": contents,
      "HiddenExits": hidden_exits,
      "LockedExits": locked_exits
    },
  }

  with open(filename, "a+") as f:
    json.dump(room_data, f, indent=4)