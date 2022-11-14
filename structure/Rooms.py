# blue print for a room
class Room():

    change_room = True

    def __init__(self,
                 name,
                 id,
                 description,
                 exploreText='you find nothing of note'):
        self.name = name  # the name of the room, used as the title
        self.id = id
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

        else:
            return False

    def removeitem(self, item):
        self.contents.remove(item)

        self.description = self.description.replace(item.description, '')

    def debug(self):
        print(f'Name: {self.name}\n'
              f'ID: {self.id}\n'
              f'Description {self.description}\n'
              f'Text On Explore: {self.exploreText}\n'
              f'Contents: {self.contents}\n'
              f'Exits: {self.Exits}\n'
              f'Hidden exits: {self.hidden_exits}\n'
              f'Locked exits: {self.locked_exits}\n')

    def data(self):
        conts = []
        for item in self.contents:
            conts.append(item.id)

        return {
            "Name": self.name,
            "Description": self.description,
            "Contents": conts,
            "Hidden exits": self.hidden_exits,
            "Locked exits": self.locked_exits
        }
