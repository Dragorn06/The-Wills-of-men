class Item():
    def __init__(self, name, Id, description):
        self.name = name  # the name of the item
        self.Id = Id
        self.description = description
        self.usage = None  # the usage of the item
        self.hidden = False

    def debug(self):
      return {
        "Name": self.name,
        "ID": self.Id,
        "Is Hidden": self.hidden,
        "description": self.description,
        "usage": self.usage,
      }

    def data(self):
      return {
            "Name": self.name,
            "Is Hidden": self.hidden
        }
