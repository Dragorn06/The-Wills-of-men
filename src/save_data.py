"""
Handles all the save data writing and reading from a JSON file
"""

import gc
import json
from .inventory import Inventory
from .rooms import Room
from .items import Item


# a save function
def save(current_room):
    """Writes save data to the save file"""

    with open('saves/save.json', 'w', encoding='utf-8') as save_file:
        saved_inventory = []
        room_data = {}
        item_data = {}

        for item in Inventory.contents:
            saved_inventory.append(item.item_id)

        for obj in gc.get_objects():
            if isinstance(obj, Room):
                room_data[f'{obj.room_id}'] = obj.data()

            elif isinstance(obj, Item):
                item_data[f'{obj.item_id}'] = obj.data()

        json.dump(
            {
                "current room": current_room,
                "Inventory": saved_inventory,
                "Rooms": room_data,
                "Items": item_data
            },
            save_file,
            ensure_ascii=False,
            indent=4)

        save_file.close()


# a load function
def load():
    """reads data from the save file and sets game data equal to it"""

    with open('saves/save.json', 'r', encoding='utf-8') as save_file:
        load_data = json.load(save_file)

        # loads the players Inventory
        for item in gc.get_objects():
            if isinstance(item, Item):
                if item.item_id in load_data["Inventory"]:
                    Inventory.add_item(item)

        # loops through each room and substitutes the saved data into the room's data
        for room in gc.get_objects():
            if isinstance(room, Room):

                room.description = load_data["Rooms"][f"{room.room_id}"][
                    "Description"]
                room_contents = load_data["Rooms"][f"{room.room_id}"][
                    "Contents"]
                room.hidden_exits = load_data["Rooms"][f"{room.room_id}"][
                    "Hidden exits"]
                room.locked_exits = load_data["Rooms"][f"{room.room_id}"][
                    "Locked exits"]

                room.contents = []

                for item in gc.get_objects():
                    if isinstance(item, Item):
                        if item.item_id in room_contents:
                            room.contents.append(item)

                        item.hidden = load_data["Items"][f"{item.item_id}"]["Is Hidden"]

                if room.room_id == load_data["current room"]:
                    current_room = room

        save_file.close()
        return current_room
