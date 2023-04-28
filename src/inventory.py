"""
Contains the player's inventory 
"""

class Inventory:
    """The players invenotry with add and remove methods"""

    contents = []

    @classmethod
    def add_item(cls, item):
        """adds an item to the players inventory"""
        cls.contents.append(item)

    @classmethod
    def remove_item(cls, item):
        """removes an item from the players inventory"""
        cls.contents.remove(item)
