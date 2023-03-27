# blue print for a room
class Room():

    change_room = True

    def __init__(self,
                 name,
                 Id,
                 description,
                 exploreText=' you find nothing of note'):
        self.name = name  # the name of the room, used as the title
        self.Id = Id
        self.description = description  # the description fo the room the player is shown
        self.exploreText = exploreText
        self.contents = []  # any items in the room
        self.Exits = {}  # any exits the room has
        self.hidden_exits = [
        ]  # any exits which are hidden - found with "explore"
        self.locked_exits = []  # any exit the player cannot go through

        # changing the room the player is in
    def change(self, direction):
        # checks if the direction wanted is possible

        if direction in self.Exits and direction not in self.hidden_exits and direction not in self.locked_exits:
            return direction

    def remove_item(self, item):
        self.contents.remove(item)

        self.description = self.description.replace(item.description, '')

        return 0

    def add_item(self, item):

        if item not in self.contents:
            self.contents.append(item)

        self.description += item.description

    def data(self):
        conts = []
        for item in self.contents:
            conts.append(item.Id)

        return {
            "Name": self.name,
            "Description": self.description,
            "Contents": conts,
            "Hidden exits": self.hidden_exits,
            "Locked exits": self.locked_exits
        }

