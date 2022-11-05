class Item():
    def __init__(self, name, description):
        self.name = name  # the name of the item
        self.description = description
        self.usage = None  # the usage of the item
        self.hidden = False