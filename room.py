import items

class Room(object):
    def __init__(self, name, dcr, itemlist):
        self.name = name
        self.description = dcr
        self.itemlist = itemlist


Dark_Room = Room('Dark Room',
                 'You find yourself in a dark room. As you feel your way around you find two exits. One to the west '
                 'and the other to the east',[items.torch])

Title_Screen = Room("The Wills' of Men", 'Lorem ipsum dolor',[])