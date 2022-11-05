class Inventory:

    contents = []

    @classmethod
    def additem(cls, item):
        cls.contents.append(item)

    @classmethod
    def removeItem(cls, item):
        cls.contents.remove(item)