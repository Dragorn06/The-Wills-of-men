"""
structure of a Non player character who can be talked to 
"""

from .player.inventory import Inventory


class Npc():
    """
  Blueprint for a Non player character who the player can interact with
  """

    # pylint: disable=too-many-arguments
    # need to refoactor to remove condition_item as an argument
    def __init__(self, name, npc_id, default_dialogue,
                 secondary_dialogue):
        self.name = name
        self.npc_id = npc_id
        self.condition_item = None
        self.default_dialogue = default_dialogue
        self.secondary_dialogue = secondary_dialogue  # returned if a condition is met

    def say_something(self):
        """Returns text for the NPC to say"""   
        # pylint: disable=no-else-return
        # This is infact necessary
        if self.condition_item in Inventory.contents:
            return self.secondary_dialogue
        else:
            return self.default_dialogue

    def data(self):
        """returns all the data of an NPC. Used for Debugging"""
        return {"name": self.name,
                "ID": self.npc_id,
                "default dialogue": self.default_dialogue}
