import gc
import json
from .Inv import Inventory
from .Rooms import Room
from .Items import Item


def save(currentRoom):

    with open('saves/save.json', 'w', encoding='utf-8') as saveFile:
        inv = []
        roomData = {}
        itemData = {}

        for item in Inventory.contents:
            inv.append(item.id)

        for obj in gc.get_objects():
            if isinstance(obj, Room):
                roomData[f'{obj.id}'] = obj.data()

            elif isinstance(obj, Item):
                itemData[f'{obj.id}'] = obj.data()

        json.dump(
            {
                "current room": currentRoom,
                "Inventory": inv,
                "Rooms": roomData,
                "Items": itemData
            },
            saveFile,
            ensure_ascii=False,
            indent=4)

        saveFile.close()


def load():

    global roomData, contents

    with open('saves/save.json', 'r', encoding='utf-8') as saveFile:
        load = json.load(saveFile)

        roomId = load['current room']
        allRoomData = load['Rooms']
        allitemData = load['Items']
        inv = load['Inventory']

        for obj in gc.get_objects():
            if isinstance(obj, Room):

                obj.contents = []

                roomData = allRoomData[f'{obj.id}']
                contents = roomData['Contents']

                obj.locked_exits = roomData['Locked exits']
                obj.hidden_exits = roomData['Hidden exits']
                obj.description = roomData['Description']

                if obj.id == roomId:
                    currentRoom = obj

        for obj in gc.get_objects():
            if isinstance(obj, Item):

                if obj.id in contents:
                    obj.contents.append(obj)

                elif obj.id in inv:
                    Inventory.contents.append(obj)

                itemData = allitemData[f'{obj.id}']

                obj.hidden = itemData['Is Hidden']

        saveFile.close()
        return currentRoom
