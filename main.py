"""
The Wills of Men v0.4.1
a text adventure game
by Dagorn06
"""

import gc
import sys
import json
import os
# general imports
import textwrap

import pygame

from scripts.player.actions import Noun, Verb, Misc_Button
from scripts.constants import (BASE_FONT, CLOCK, DISPLAY, FANCY_FONT, WINHIEGHT,
                           WINWIDTH)
from scripts.homescreen import Homescreen

# importing other parts of the game
from scripts.player.inventory import Inventory
from scripts.items.ItemStructure import Item
from scripts.npcs import Npc
from scripts.rooms.RoomStructure import Room
from scripts.rooms import *
from scripts.save_data import load, save

# initialising pygame
pygame.init()

# rendering functions


def render_title():
    """Render the title at the top of the page."""
    title_text = Main.current_room.name

    # Render the title text.
    title_surface = FANCY_FONT.render(title_text, True, (255, 255, 255))
    title_rect = title_surface.get_rect(center=(WINWIDTH // 2, 20))

    # Display the title text.
    DISPLAY.blit(title_surface, title_rect)

def render_description():
    """Render the current room's description."""

    # Set the initial description position.
    description_y = 50

    # Wrap the room's description text.
    description_lines = textwrap.wrap(Main.current_room.description, 30)

    # Render each line of the description text.
    for line in description_lines:
        description_surface_line = BASE_FONT.render(line, False, (255, 255, 255))
        DISPLAY.blit(description_surface_line, (12, description_y))
        description_y += 15

def render_inventory():
    """Render the contents of the player's inventory in a list."""

    # Set the initial inventory position.
    inventory_y = 50

    # Render each item in the player's inventory.
    for item in Inventory.contents:
        item_surface = BASE_FONT.render(item.name, False, (255, 255, 255))
        DISPLAY.blit(item_surface, (WINWIDTH - (WINWIDTH / 3) + 2, inventory_y))
        inventory_y += 15

def render_verbs(mouse: pygame.Vector2, verb_list: list[Verb]):
    """Render the verbs the player can use.

    Args:
        mouse: The mouse position.
        verb_list: The list of verbs to render.
    """

    # Count the number of clicked verbs.
    num_clicked = len([v for v in verb_list if v.clicked])

    # Group the verbs into rows of 3.
    verb_rows = [verb_list[x:x+3] for x in range(0, len(verb_list), 3)]

    # Set the initial verb position.
    verb_x = WINWIDTH // 3
    verb_y = WINHIEGHT - WINHIEGHT // 3

    # Render each verb row.
    for verb_row in verb_rows:
        for verb in verb_row:
            # Render the verb text.
            verb_surface = FANCY_FONT.render(f" {verb.name} ", True, (255, 255, 255))

            # Set the verb's rectangle.
            verb.rect = verb_surface.get_rect(center=(verb_x, verb_y))

            # Draw a border around the verb if it is clicked or hovered over.
            if verb.rect.collidepoint(mouse) or verb.clicked:
                pygame.draw.rect(DISPLAY, (255, 255, 255), verb.rect, 2, border_radius=5)

                # Render the verb's noun list if there is only one clicked verb and it is clicked
                if not verb.clicked and num_clicked == 1:
                    pass
                else:
                    render_nouns(verb, mouse)

            # Display the verb text.
            DISPLAY.blit(verb_surface, verb.rect)

            # Move the verb position down.
            verb_y += 50

        # Reset the verb position to the next row.
        verb_y = WINHIEGHT - WINHIEGHT // 3
        verb_x += 120

def render_nouns(verb: Verb, mouse: pygame.Vector2):
    """Render the nouns for the given verb.

    Args:
        verb: The verb to render the nouns for.
        mouse: The mouse position.
    """

    # Set the initial noun position.
    noun_x = WINWIDTH - WINWIDTH // 3
    noun_y = WINHIEGHT - WINHIEGHT // 3

    # Render each noun.
    for noun in verb.nouns:
        # Render the noun text.
        noun_surface = FANCY_FONT.render(f" {noun.name} ", True, (255, 255, 255))

        # Set the noun's rectangle.
        noun.rect = noun_surface.get_rect(center=(noun_x, noun_y))

        # Draw a border around the noun if it is clicked or hovered over.
        if noun.rect.collidepoint(mouse) or noun.clicked:
            pygame.draw.rect(DISPLAY, (255, 255, 255), noun.rect, 2, border_radius=5)

        # Display the noun text.
        DISPLAY.blit(noun_surface, noun.rect)

        # Move the noun position down.
        noun_y += 50

def render_misc_buttons(mouse: pygame.Vector2, button_list: list[Misc_Button]):
    """Render the misc buttons.

    Args:
        mouse: The mouse position.
        button_list: The list of misc buttons to render.
    """

    # Set the initial misc button position.
    misc_button_y_offset = 0

    # Render each misc button.
    for button in button_list:
        # Render the misc button text.
        button_surface = FANCY_FONT.render(f"{button.name}", True, (255, 255, 255))

        # Set the misc button's rectangle.
        button.rect = button_surface.get_rect(center=(WINWIDTH - (WINWIDTH // 10), 20 + misc_button_y_offset))
        
        # draw a border if the mouse hovers over the button
        if button.rect.collidepoint(mouse):
            pygame.draw.rect(DISPLAY, (255, 255, 255), button.rect, 2, border_radius=5)

        # blit the button
        DISPLAY.blit(button_surface, button.rect)

        # move the next button down
        misc_button_y_offset += 50


def render_event():
    """Render any events that occur. These can be triggered by item uses."""

    # Set the initial event position.
    event_y_offset = 0

    # Wrap the event text.
    event_lines = textwrap.wrap(Main.event, 40)

    # Render each line of the event text.
    for line in event_lines:
        event_surface = BASE_FONT.render(line, False, (255, 255, 255))
        event_rect = event_surface.get_rect(
            center=(WINWIDTH // 2,
                    WINHIEGHT - (WINHIEGHT // 2.4) + event_y_offset))
        DISPLAY.blit(event_surface, event_rect)
        event_y_offset += 15

def render_response_text():
    """Render the one-line response that the player is given."""

    # Get the response text.
    response_text = Main.responce

    # Render the response text.
    response_surface = BASE_FONT.render(response_text, False, (255, 255, 255))

    # Display the response text.
    DISPLAY.blit(response_surface, (WINWIDTH // 48, WINHIEGHT - 57))

# Item usages
'''
first word - level item is used in e.g. l1 is used in level 1
second word - what it does
'''


def l1_light_forge():
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


def explore_room():
    """
    displays the explore text of a room and removes any hidden exits
    """
    if Main.current_room.explore_text != ' you find nothing of note':
        Main.event = Main.current_room.explore_text

        Main.current_room.hidden_exits = []

        save(Main.current_room.room_id)

    
def l1_open_door():
    """opens the door in the dark room"""
    if Main.current_room.room_id == 0:
        if "north" not in Main.current_room.hidden_exits:

            Main.responce = "you open the door"
            Main.current_room.locked_exits.remove("north")
            Inventory.remove_item(Booter.items[2])


def l2_buy_sword():
    """buys the sword in the market"""
    if Main.current_room == Booter.rooms[7]:
        if Booter.items[3] in Inventory.contents:

            Main.responce = "you buy the sword"
            Main.event = "'Here the sword is yours!'"
            Inventory.add_item(Booter.items[5])
            Inventory.remove_item(Booter.items[3])

            Main.current_room.description = Main.current_room.description.replace(
                "There is a sword for sale at one of the stalls", '')


def l2_fight_bear():
    """Fight the bear using the sword and the scroll"""
    if Main.current_room == Booter.rooms[6]:
        if Booter.items[5] in Inventory.contents and Booter.items[4] not in Inventory.contents:
            Main.event = """You use your sword to take on the bear.
            You fight valiantly but are forced to retreat"""
        elif Booter.items[5] in Inventory.contents and Booter.items[4] in Inventory.contents:
            Main.event = """You use your sword and the magic scroll to scare the bear away!"""

            Main.current_room.description = Main.current_room.description.replace(
                "Suddenly a bear jumps out infront of you blocking the way.",
                "")

            Main.current_room.description = "You have finished The Wills of Men v0.4.1"
            Booter.items[4].usage = None
            Booter.items[5].usage = None

class Booter:
    rooms = []
    items = []
    usages = {
        "0": [l1_light_forge, explore_room],
        "1": [l1_light_forge],
        "2": [l1_open_door],
        "3": [l2_buy_sword],
        "4": [l2_fight_bear],
        "5": [l2_fight_bear]
    }
    npcs = []

    @classmethod
    def boot(cls):

        cls.create_items("GameObjects/items.json", cls.usages)
        cls.create_npcs("GameObjects/npcs.json", cls.items)
        cls.create_rooms("GameObjects/rooms.json", cls.items, cls.npcs)

        # print([i.data() for i in cls.rooms])
        Main.current_room = cls.rooms[0]
        render_title()

        Homescreen.loop()
        if Homescreen.donext == 'load':
            Main.current_room = load()
        else:
            pass
        Main.game_loop()


    @classmethod
    def create_items(cls, json_file, usages):
        """Creates instances of the Item class from a JSON file.

        Args:
            json_file: The path to the JSON file.
        """

        with open(json_file, "r") as f:
            json_data = json.load(f)

        for item_data in json_data:
            item = Item(
            json_data[f"{item_data}"]["Name"],
            json_data[f"{item_data}"]["ID"],
            json_data[f"{item_data}"]["description"],
            json_data[f"{item_data}"]["Examine Text"]
            )

            if json_data[f"{item_data}"]["Is Hidden"]:
                item.hidden = True
            else:
                item.hidden = False

            try:
                item.usage = usages[f"{item.item_id}"]
            except KeyError:
                print("item has no defined usages")
            
            cls.items.append(item)


    @classmethod
    def create_npcs(cls, json_file, items):
        """Creates instances of the Room class from a JSON file.

        Args:
            json_file: The path to the JSON file.
            items: a list of all of the item objects
        """

        with open(json_file, "r") as f:
            json_data = json.load(f)

        for npc_data in json_data:
            npc = Npc(
                json_data[f"{npc_data}"]["Name"],
                json_data[f"{npc_data}"]["NpcId"],
                json_data[f"{npc_data}"]["Primary Dialogue"],
                json_data[f"{npc_data}"]["Secondary Dialogue"]
            )

            condition_item = json_data[f"{npc_data}"]["Condition Item"]
            for item in cls.items:
                if condition_item == item.item_id:
                    npc.condition_item = item

            cls.npcs.append(npc)

    @classmethod
    def create_rooms(cls, json_file, items, npcs):
        """Creates instances of the Room class from a JSON file.

        Args:
            json_file: The path to the JSON file.
            items: a list of all of the item objects.
            npcs: a list of all of the npc objects.
        """

        with open(json_file, "r") as f:
            json_data = json.load(f)

        for room_data in json_data:
            room = Room(
            json_data[f"{room_data}"]["Name"],
            json_data[f"{room_data}"]["RoomId"],
            json_data[f"{room_data}"]["Description"],
            json_data[f"{room_data}"]["ExploreText"],
            )

            # Add any items in the room.
            for item_id in json_data[f"{room_data}"]["Contents"]:
                for item in cls.items:
                    if item_id == item.item_id:
                        room.contents.append(item)
            
            for npc_id in json_data[f"{room_data}"]["Npcs"]:
                for npc in cls.npcs:
                    if npc_id == npc.npc_id:
                        room.npcs.append(npc)

            #set the rooms exits
            room.exits = json_data[f"{room_data}"]["Exits"]

            # Add any hidden exits.
            room.hidden_exits = json_data[f"{room_data}"]["HiddenExits"]

            # Add any locked exits.
            room.locked_exits = json_data[f"{room_data}"]["LockedExits"]

            cls.rooms.append(room)


class Main:
    """The main class containing player location data and the main game loop as well"""

    # the room the player is in
    current_room = None

    # responce to player action
    responce = ''

    # text for an event which has occured
    event = ''

    live_verb = None

    pygame.display.set_caption('The Wills of Men')

    verbs = None
    nouns = None
    misc_buttons = None

    # main game loop
    @classmethod
    def game_loop(cls):
        """The main game function. Renders all game content and registers player input"""

        input_text = ''.lower()

        cls.assign_get_nouns()

        cls.assign_examine_use_nouns()

        cls.assign_talk_nouns()

        clicked_verb = None
        clicked_noun = None

        while True:

            DISPLAY.fill((0, 0, 0))

            mouse = pygame.mouse.get_pos()

            cls.verbs = [s for s in gc.get_objects() if isinstance(s, Verb)]
            cls.nouns = [s for s in gc.get_objects() if isinstance(s, Noun)]
            cls.misc_buttons = [b for b in gc.get_objects() if isinstance(b, Misc_Button)]

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:

                    clicked_verb = None
                    clicked_noun = None
                    clicked_misc_button = None

                    # Get the list of collisions for all three types of objects.
                    verb_collisions = [v for v in cls.verbs if v.rect.collidepoint(mouse)]
                    if cls.live_verb is not None:
                        noun_collisions = [n for n in cls.live_verb.nouns if n.rect.collidepoint(mouse) ]
                    else:
                        noun_collisions = []
                    misc_button_collisions = [b for b in cls.misc_buttons if b.rect.collidepoint(mouse)]
                    # If there are any collisions, set the corresponding variable to the collided object.

                    if verb_collisions:
                        clicked_verb = verb_collisions[0]
                    if noun_collisions:
                        clicked_noun = noun_collisions[0]
                    if misc_button_collisions:
                        clicked_misc_button = misc_button_collisions[0]

                    # Update the verbs, nouns, and misc buttons based on the clicked objects.
                    cls.update_verbs(clicked_verb)
                    cls.update_nouns(cls.live_verb, clicked_noun)
                    cls.update_misc_button(clicked_misc_button)

            # all the information the player needs to see is rendered here
            render_title()
            render_description()
            render_inventory()

            render_verbs(mouse, cls.verbs)
            render_misc_buttons(mouse, cls.misc_buttons)

            render_event()
            render_response_text()

            # Update the display.
            pygame.display.flip()

            # Limit the framerate to 60 FPS.
            CLOCK.tick(120)

    @classmethod
    def assign_get_nouns(cls):
        """Assign nouns to the `get` verb."""

        get_nouns = []
        for item in cls.current_room.contents:
            if not item.hidden:
                get_noun = Noun(f"{item.name}", [get])
                get_nouns.append(get_noun)

        get.nouns = get_nouns


    @classmethod
    def assign_examine_use_nouns(cls):
        """Assign nouns to the `examine` and `use` verbs."""

        examine_use_nouns = []
        for item in Inventory.contents:
            examine_use_noun = Noun(f"{item.name}")
            examine_use_nouns.append(examine_use_noun)

        use.nouns = examine_use_nouns
        examine.nouns = examine_use_nouns

        # Assign the `use` and `examine` verbs to each noun.
        for noun in examine_use_nouns:
            noun.verbs = [use, examine]

    @classmethod
    def assign_talk_nouns(cls):
        """Assign nouns to the `talk` verb."""

        talk_nouns = []
        for npc in cls.current_room.npcs:
            talk_noun = Noun(f"{npc.name}", [talk])
            talk_nouns.append(talk_noun)

        talk.nouns = talk_nouns


    @classmethod
    def update_nouns(cls, clicked_verb: Verb, clicked_noun: Noun):
        """Update the nouns associated with the clicked verb.

        Args:
            clicked_verb: The verb that was clicked.
            clicked_noun: The noun that was clicked.
        """

        if clicked_noun:
            # Find the verb on the noun and update it.
            for verb in clicked_noun.verbs:
                if verb.name == clicked_verb.name:
                    verb.action(clicked_noun.name)

            # Reset all other verbs and nouns.
            cls.live_verb = None
            for noun in cls.nouns + cls.verbs:
                noun.reset()

    @classmethod
    def update_verbs(cls, clicked_verb: Verb):
        """Update the verbs associated with the clicked verb.

        Args:
            clicked_verb: The verb that was clicked.
        """

        if clicked_verb:
            # Update the clicked verb.
            clicked_verb.update()

            # Set the live verb if the clicked verb is clicked.
            if clicked_verb.clicked:
                cls.live_verb = clicked_verb
            else:
                cls.live_verb = None

            # Unclick all other verbs.
            for verb in [verb for verb in cls.verbs if verb is not clicked_verb]:
                verb.clicked = False


    @classmethod
    def update_misc_button(cls, clicked_misc_button: Misc_Button):
        """Update the clicked misc button.

        Args:
            clicked_misc_button: The misc button that was clicked.
        """

        if clicked_misc_button:
            # Call the action of the clicked misc button.
            clicked_misc_button.action()

    @classmethod
    def go_direction(cls, direction: str):
        """Try to go in the given direction.

        Args:
            direction: The direction to go in.
        """
        try:
            target_id = cls.current_room.exits[direction]
        except KeyError:
            cls.responce = "You can't go that way."
            return 0
       
        # Check if the exit is hidden or locked.
        if direction not in cls.current_room.hidden_exits + cls.current_room.locked_exits:
            # Set the player's current room to the new room.
            for room in Booter.rooms:
                    if target_id == room.room_id:
                        
                        cls.current_room = room

                    else:
                        cls.responce = "You can't go that way."


            # Save the player's current room.
            save(cls.current_room.room_id)
            # Assign nouns to the `get`, `examine`, `use`, and `talk` verbs.
            cls.assign_get_nouns()
            cls.assign_examine_use_nouns()
            cls.assign_talk_nouns()

            cls.responce = f"You go {direction}"
            # Clear the event.
            cls.event = ""
        else:
            cls.responce = "You can't go that way."
 

    @classmethod
    def get_item(cls, item: str):
        """Pick up the given item from the current room.

        Args:
            item: The item to pick up.
        """
        # checks items in a room against the players input a
        for i in cls.current_room.contents:
            if item == i.name and not i.hidden:
                    
                    # adds the item to the players inventory and removes it from the room
                    Inventory.add_item(i)
                    cls.current_room.remove_item(i)

                    cls.responce = f'you get the {item}'

                    # assigns 'get', 'use' and 'examine nouns
                    cls.assign_get_nouns()
                    cls.assign_examine_use_nouns()
                    
                    # saves the game
                    save(cls.current_room.room_id)


    @classmethod
    def talk_to_npc(cls, npc_name: str):
        """Talk to the NPC with the given name.

        Args:
            npc_name: The name of the NPC to talk to.

        Returns:
            The NPC's response.
        """

        for npc in cls.current_room.npcs:
            if npc.name == npc_name:
                cls.event = npc.say_something()

    @classmethod
    def use_item(cls, item_name: str):
        """Use the item with the given name.

        Args:
            item_name: The name of the item to use.
        """

        for item in Inventory.contents:
            if item_name in item.name:
                if item.usage is not None:
                    for usage in item.usage:
                        usage()

    @classmethod
    def examine_item(cls, item_name: str):
        """Examine the item with the given name.

        Args:
            item_name: The name of the item to examine.
        """

        for item in Inventory.contents:
            if item_name in item.name:
                cls.responce = item.examine_text

    @classmethod
    def save(cls):
        """Save the player's progress."""

        save(cls.current_room.room_id)
        cls.responce = "You save."

    @classmethod
    def load(cls):
        """Load the player's progress."""

        save_data.load()

    @classmethod
    def quit(cls):
        """Quit the game."""

        pygame.quit()
        sys.exit()


# creating nouns
north = Noun("north")
south = Noun("south")
east = Noun("east")
west = Noun("west")

# creating verbs
go = Verb("go", [north, south, east, west], Main.go_direction)
get = Verb("get", [], Main.get_item)
use = Verb("use", [], Main.use_item)
examine = Verb("examine", [], Main.examine_item)
talk = Verb("talk", [], Main.talk_to_npc)

north.verbs = [go]
south.verbs = [go]
east.verbs = [go]
west.verbs = [go]

# creating misc buttons
save_button = Misc_Button("save", Main.save)
load_button = Misc_Button("load", Main.load)
quit_button = Misc_Button("quit", Main.quit)

if __name__ == "__main__":
    Booter.boot()
