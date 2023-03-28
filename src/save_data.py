"""
Handles all the save data writing and reading form a JSON file
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
        inv = []
        room_data = {}
        item_data = {}

        for item in Inventory.contents:
            inv.append(item.Id)

        for obj in gc.get_objects():
            if isinstance(obj, Room):
                room_data[f'{obj.room_id}'] = obj.data()

            elif isinstance(obj, Item):
                item_data[f'{obj.item_id}'] = obj.data()

        json.dump(
            {
                "current room": current_room,
                "Inventory": inv,
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

        room_id = load_data['current room']
        all_room_data = load_data['Rooms']
        all_item_data = load_data['Items']
        inv = load_data['Inventory']

        for obj in gc.get_objects():
            if isinstance(obj, Room):

                obj.contents = []

                room_data = all_room_data[f'{obj.room_id}']
                contents = room_data['Contents']

                print(contents)

                obj.locked_exits = room_data['Locked exits']
                obj.hidden_exits = room_data['Hidden exits']
                obj.description = room_data['Description']

                if obj.room_id == room_id:
                    current_room = obj

        for obj in gc.get_objects():
            if isinstance(obj, Item):

                if obj.item_id in contents:
                    obj.contents.append(obj)

                elif obj.item_id in inv:
                    Inventory.contents.append(obj)

                item_data = all_item_data[f'{obj.item_id}']

                obj.hidden = item_data['Is Hidden']

        save_file.close()
        return current_room
