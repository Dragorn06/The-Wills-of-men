import gc
import json
from .Inv import Inventory
from .Rooms import Room
from .Items import Item


# a save function
def save(currentRoom):

    with open('saves/save.json', 'w', encoding='utf-8') as saveFile:
        inv = []
        roomData = {}
        itemData = {}

        for item in Inventory.contents:
            inv.append(item.Id)

        for obj in gc.get_objects():
            if isinstance(obj, Room):
                roomData[f'{obj.Id}'] = obj.data()

            elif isinstance(obj, Item):
                itemData[f'{obj.Id}'] = obj.data()

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


# a load function
def load():

    with open('saves/save.json', 'r', encoding='utf-8') as saveFile:
        loadData = json.load(saveFile)

        roomId = loadData['current room']
        allRoomData = loadData['Rooms']
        allitemData = loadData['Items']
        inv = loadData['Inventory']

        for obj in gc.get_objects():
            if isinstance(obj, Room):

                obj.contents = []

                roomData = allRoomData[f'{obj.Id}']
                contents = roomData['Contents']

                print(contents)

                obj.locked_exits = roomData['Locked exits']
                obj.hidden_exits = roomData['Hidden exits']
                obj.description = roomData['Description']

                if obj.Id == roomId:
                    currentRoom = obj

        for obj in gc.get_objects():
            if isinstance(obj, Item):

                if obj.Id in contents:
                    obj.contents.append(obj)

                elif obj.Id in inv:
                    Inventory.contents.append(obj)

                itemData = allitemData[f'{obj.Id}']

                obj.hidden = itemData['Is Hidden']

        saveFile.close()
        return currentRoom
