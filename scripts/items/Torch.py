def light_forge():
    """Lights the forge in the Abandoned forge"""
    if Main.current_room.room_id == 2:
        if Booter.items[0] in Inventory.contents and Booter.items[1] in Inventory.contents:

            Main.responce = "you light the forge with the torch and coal."

            Main.event = "Suddenly a key appears on the anvil"

            Booter.items[2].description = 'There is a Rusty key on the anvil'
            Booter.items[2].hidden = False

            Main.current_room.add_item(Booter.items[2])

            Inventory.remove_item(Booter.items[1])

            Main.assign_get_nouns()
            Main.assign_examine_use_nouns()
