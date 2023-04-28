"""
The basic structure of a room is defined here
"""


class Room():
    """A blue print for a room the player can interact with"""

    # pylint: disable=too-many-instance-attributes
    # 8 are necassery to achieve full functionality

    change_room = True

    def __init__(self,
                 name,
                 room_id,
                 description,
                 explore_text=' you find nothing of note'):
        self.name = name  # the name of the room, used as the title
        self.room_id = room_id
        self.description = description  # the description fo the room the player is shown
        self.explore_text = explore_text
        self.contents = []  # any items in the room
        self.npcs = [] # npcs which are in the room
        self.exits = {}  # any exits the room has
        self.hidden_exits = [
        ]  # any exits which are hidden - found with "explore"
        self.locked_exits = []  # any exit the player cannot go through

        # changing the room the player is in
    def change(self, direction):
        """ checks if the direction wanted is possible """

        if direction in self.exits and direction not in self.hidden_exits:
            if direction not in self.locked_exits:
                return direction

            return None
        return None

    def remove_item(self, item):
        """Removes an item from the rooms contents"""
        self.contents.remove(item)

        self.description = self.description.replace(item.description, '')

    def add_item(self, item):
        """Adds an item to the room's contents"""

        if item not in self.contents:
            self.contents.append(item)

        self.description += item.description

    def data(self):
        """returns all the room's data"""
        conts = []
        for item in self.contents:
            conts.append(item.item_id)

        return {
            "Name": self.name,
            "Description": self.description,
            "Contents": conts,
            "Hidden exits": self.hidden_exits,
            "Locked exits": self.locked_exits
        }
