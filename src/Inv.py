class Inventory:

    contents = []

    @classmethod
    def add_item(cls, item):
        cls.contents.append(item)

    @classmethod
    def remove_item(cls, item):
        cls.contents.remove(item)