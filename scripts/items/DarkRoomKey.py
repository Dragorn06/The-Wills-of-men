def l1_open_door():
    """opens the door in the dark room"""
    if Main.current_room.room_id == 0:
        if "north" not in Main.current_room.hidden_exits:

            Main.responce = "you open the door"
            Main.current_room.locked_exits.remove("north")
            Inventory.remove_item(Booter.items[2])
