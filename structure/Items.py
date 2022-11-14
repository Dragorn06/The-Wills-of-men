class Item():
    def __init__(self, name, id, description):
        self.name = name  # the name of the item
        self.id = id
        self.description = description
        self.usage = None  # the usage of the item
        self.hidden = False

    def __str__(self):
        print(f'Name: {self.name}\n '
              f'Usage: {self.usage}\n'
              f'Is Hidden: {self.hidden}')

        return {
            "Name": self.name,
            "Usage": self.usage,
            "Is Hidden": self.hidden
        }
