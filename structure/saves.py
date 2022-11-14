import gc
import json
from .Inv import Inventory
from .Rooms import Room
from .Items import Item


def save(currentRoom):

    with open('saves/save.json', 'w', encoding='utf-8') as saveFile:
        inv = []
        roomData = {}

        for item in Inventory.contents:
            inv.append(item.id)

        for obj in gc.get_objects():
            if isinstance(obj, Room):
                roomData[f'{obj.id}'] = obj.data()

        json.dump(
            {
                "current room": currentRoom,
                "Inventory": inv,
                "Rooms": roomData
            },
            saveFile,
            ensure_ascii=False,
            indent=4)

        saveFile.close()


def load(currentRoom):
    with open('saves/save.json', 'r', encoding='utf-8') as saveFile:
        load = json.load(saveFile)

        roomId = load['current room']
        allRoomData = load['Rooms']
        inv = load['Inventory']

        for obj in gc.get_objects():
            if isinstance(obj, Room):

                roomData = allRoomData[f'{obj.id}']

                obj.locked_exits = roomData['Locked exits']
                obj.hidden_exits = roomData['Hidden exits']
                obj.description = roomData['Description']

                if obj.id == roomId:
                    currentRoom = obj

                for item in gc.get_objects():
                    if isinstance(item, Item):
                        if item.id in roomData['Contents']:
                            obj.contents.append(item)

            if isinstance(obj, Item):
                if obj.id in inv:
                    Inventory.contents.append(obj)

        saveFile.close()
