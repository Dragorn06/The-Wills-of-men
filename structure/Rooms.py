# blue print for a room
class Room():

    change_room = True

    def __init__(self,name, description, exploreText='you find nothing of note'):
        self.name = name  # the name of the room, used as the title
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