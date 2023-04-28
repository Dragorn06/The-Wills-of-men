"""
structure of a Non player character who can be talked to 
"""

from .inventory import Inventory


class Npc():
    """
  Blueprint for a Non player character who the player can interact with
  """
    def __init__(self, name, npc_id, condition_item, default_dialogue,
                 secondary_dialogue):
        self.name = name
        self.npc_id = npc_id
        self.condition_item = condition_item
        self.default_dialogue = default_dialogue
        self.secondary_dialogue = secondary_dialogue  # returned if a condition is met

    def say_something(self):
        if self.condition_item in Inventory.contents:
            return self.secondary_dialogue
        else:
            return self.default_dialogue
