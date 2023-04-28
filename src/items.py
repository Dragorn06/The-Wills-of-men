"""
the basic structure of an item
"""


class Item():
    """a blueprint class for an item"""

    def __init__(self, name, item_id, description):
        self.name = name  # the name of the item
        self.item_id = item_id
        self.description = description
        self.usage = None  # the usage of the item
        self.hidden = False

    def debug(self):
        """a debug class which returns the item's data"""

        return {
            "Name": self.name,
            "ID": self.item_id,
            "Is Hidden": self.hidden,
            "description": self.description,
            "usage": self.usage,
        }

    def data(self):

        """returns the name and hidden status of an item"""

        return {
            "Name": self.name,
            "Is Hidden": self.hidden
        }
