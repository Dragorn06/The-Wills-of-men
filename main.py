"""
The Wills of Men
by Dragorn 06

a text adventure game
"""

# general imports
import textwrap
import sys
import pygame

# importing other parts of the game
from src.inventory import Inventory
from src.items import Item
from src.rooms import Room
from src.homescreen import Homescreen
from src.save_data import save, load
from src.constants import WINWIDTH, WINHIEGHT, CLOCK, DISPLAY
from src.constants import BASE_FONT, FANCY_FONT

# initialising pygame
pygame.init()

# rendering functions


def render_title():
    """Renders the title at the top of the page"""

    title = FANCY_FONT.render(Main.current_room.name, True, (255, 255, 255))

    title_rect = title.get_rect(center=(WINWIDTH // 2, 20))

    DISPLAY.blit(title, title_rect)


def render_description():
    """Renders the current room's description"""

    description_y = 50

    for i in textwrap.wrap(Main.current_room.description, 30):

        description_surface_i = BASE_FONT.render(i, True, (255, 255, 255))

        DISPLAY.blit(description_surface_i, (12, description_y))

        description_y += 15


def render_inventory():
    """Renders the contents of the players inventory in a list"""

    inv_y = 50

    for item in Inventory.contents:

        item_surface_i = BASE_FONT.render(item.name, True, (255, 255, 255))

        DISPLAY.blit(item_surface_i, (WINWIDTH - (WINWIDTH / 3) + 2, inv_y))

        inv_y += 15


def render_event():
    """Renders any events that occur. These can be triggered by item uses"""

    event_surface = BASE_FONT.render(Main.event, True, (255, 255, 255))

    event_rect = event_surface.get_rect(center=(WINWIDTH // 2,
                                                WINHIEGHT - (WINHIEGHT // 3)))

    DISPLAY.blit(event_surface, event_rect)


def render_responcetext():
    """Renders the one line responce that the player is given"""

    responce_surface = BASE_FONT.render(Main.responce, True, (255, 255, 255))

    DISPLAY.blit(responce_surface, (10, WINHIEGHT - 57))


# creating items
Torch = Item('Torch', 0, ' On the wall there is a lit Torch.')
CoalBarrel = Item('Barrel of coal', 1,
                  ' In the corner there is a barrel of coal.')

Key = Item('Rusty key', 2, '')
CoinBag = Item(
    'Bag of Coins', 3,
    'In the gutter you see a bag of coins glinting in the sunlight.')

# Hidding items
Key.hidden = True

# Iem usages
'''
first word - level item is used in e.g. l1 is used in level 1
second word - what it does
'''


def l1_light_forge():
    """Lights the forge in the Abandoned forge"""
    if Main.current_room == Abandoned_forge:
        if Torch in Inventory.contents and CoalBarrel in Inventory.contents:

            Main.responce = "you light the forge with the torch and coal."

            Main.event = "Suddenly a key appears on the anvil"

            Key.description = 'There is a Rusty key on the anvil'
            Key.hidden = False

            Main.current_room.add_item(Key)

            Inventory.remove_item(CoalBarrel)


def l1_open_door():
    """opens the door in the dark room"""
    if Main.current_room == Dark_Room:
        if "north" not in Dark_Room.hidden_exits:

            Main.responce = "you open the door"
            Main.current_room.locked_exits.remove("north")
            Inventory.remove_item(Key)


# assigning usages to items
Torch.usage = l1_light_forge
CoalBarrel.usage = l1_light_forge
Key.usage = l1_open_door

# Level 1
Dark_Room = Room(
    'Dark Room', 0, """You're in a dark cave. It is pitch black but you
 begin to feel your way around the room """,
    ' To the north of the room you find a key hole.')

Lake = Room(
    'Lake of Dreams',
    1,
    """You walk into a dimly lit cavern.
 In the center is a glowing blue lake.
 On the wall there is a lit Torch.""",
)

Abandoned_forge = Room(
    'Abandoned Forge', 2, """You walk into a new room.
 It appears to be an old forge with old will forging equipment and an anvil.
There is a thin been of light coming into the room
 from a man made hole in the ceiling.
 In the corner there is a barrel of coal.""")

# Level 2
Crossroads = Room(
    'Crossroads',
    3,
    """you find yourself at a crossroads in the mountains.
 There are three paths infront of you.
 One leads west down into a dark sprawlling forest. Another track to the east winds
 up high into the mountains.
 The last path leads down to a small hamlet far bellow you.""",
)

Atvust = Room(
    'Atvust', 4, """you enter the village of Avust.
 As you walk down the narrow but clean streets the sounds of merriment begin to surround you.
 Soon you come to the main square to the west there is a tavern and to the east there is a market. 
 In the gutter you see a bag of coins glinting in the sunlight."""
)

Mountaintop = Room(
    'Mountaintop', 5,
    """As you crest the peak of the icy mountain the land stretches out far below you. 
Below you, a village can be seen in the distance as well as a dark sprawling forrest. 
There is a magical presence here."""
)

Forest_entrance = Room(
    'Forest Entrance', 6,
    """You are unerved by the forrest as if the is an evil presense here. 
In the future there will be something here."""
)

Atvust_Market = Room(
    'Market', 7,
    """The small market you are now presented with is surprisingly lively. 
All around you villagers are haggling with merchants from the outer dales. 
Sitting quietly at one of the stands at the far end of the market is a wizard."""
)

Atvust_Tavern = Room(
    'Tavern', 8,
    """The smell of hearty ale wafts towards you as you enter the Tavern.
 Once you are inside you see many people of the town including 
 several Arcinthian Dwarves drinking and sining merrily.
 Behind the bar you see the Landlord cleaning an tankard.
 """)

# Setting up room exits
# each room can have four exits
Dark_Room.exits = {"north": Crossroads, "east": Abandoned_forge, "west": Lake}
Lake.exits = {"east": Dark_Room}
Abandoned_forge.exits = {"west": Dark_Room}
Crossroads.exits = {
    "north": Atvust,
    "south": Dark_Room,
    "east": Mountaintop,
    "west": Forest_entrance
}
Atvust.exits = {
    "south": Crossroads,
    "east": Atvust_Market,
    "west": Atvust_Tavern
}
Mountaintop.exits = {"west": Crossroads}
Forest_entrance.exits = {"east": Crossroads}
Atvust_Market.exits = {"west": Atvust}
Atvust_Tavern.exits = {"east": Atvust}

# setting up locked exits
Dark_Room.locked_exits = ["north"]

# setting up hidden exits
Dark_Room.hidden_exits = ["north"]

# setting up the contents of rooms
Dark_Room.contents = []
Lake.contents = [Torch]
Abandoned_forge.contents = [CoalBarrel, Key]
Atvust.contents = [CoinBag]
Mountaintop.contents = []
Forest_entrance = []
Atvust_Market = []
Atvust_Tavern = []


class Main:
    """The main class containing player location data and the main game loop as well"""

    # the room the player is in
    current_room = Dark_Room

    # responce to player action
    responce = ''

    # text for an event which has occured
    event = ''

    pygame.display.set_caption('The Wills of Men')

    # main game loop
    @classmethod
    def game_loop(cls):
        """The main game function. Renders all game content and registers player input"""

        input_text = ''.lower()

        while True:

            DISPLAY.fill((0, 0, 0))

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_BACKSPACE:

                        input_text = input_text[:-1]

                    elif event.key == pygame.K_RETURN:

                        Main.action(input_text)

                        input_text = ''.lower()

                    else:
                        input_text += event.unicode

            # Rendering the players input as it is typed
            text_surface = BASE_FONT.render(input_text, True, (255, 255, 255))
            DISPLAY.blit(text_surface, (10, WINHIEGHT - 32))

            # all the information the player needs to see is rendered here
            render_title()
            render_description()
            render_inventory()

            render_event()
            render_responcetext()

            pygame.display.flip()
            CLOCK.tick(60)

    @classmethod
    def action(cls, input_text):
        """Takes a players input"""

        # pylint: disable=too-many-branches
        # currently this number of branches is needed
        # in the future this may change

        # splits the input text string into an arrary of strings
        split_input = input_text.split()

        if split_input in ([''], [], [' ']):
            pass

        # checks the first word against a list of actions
        elif "go" == split_input[0]:
            # changes the room using the second word as an argument

            direction = cls.current_room.change(split_input[1])

            if direction:

                cls.responce = f'you go {direction}'

                if cls.event == cls.current_room.explore_text:
                    cls.current_room.description += cls.current_room.explore_text

                cls.event = ''

                # sets the playrs current room to the new room
                cls.current_room = cls.current_room.exits[direction]
                save(cls.current_room.room_id)

            else:
                cls.responce = 'I dont understand'

        elif "get" == split_input[0]:

            # checks items in a room against the players input
            for item in Main.current_room.contents:
                if split_input[1] in item.name.lower():

                    if not item.hidden:

                        Inventory.add_item(item)
                        cls.responce = f'you get the {item.name}'
                        cls.current_room.remove_item(item)
                        save(cls.current_room.room_id)

        elif "explore" == split_input[0]:
            if Torch in Inventory.contents:
                cls.responce = 'you look around.'

                if cls.current_room.explore_text != ' you find nothing of note':
                    Main.event = cls.current_room.explore_text

                cls.current_room.hidden_exits = []

                save(cls.current_room.room_id)

        elif "use" == split_input[0]:
            for item in Inventory.contents:

                if split_input[1] in item.name.lower():
                    item.usage()

        elif "save" == split_input[0]:
            save(cls.current_room.room_id)
            cls.responce = 'you save'

        elif "quit" == split_input[0]:
            pygame.quit()
            sys.exit()

        else:
            cls.responce = 'I dont understand'


if __name__ == "__main__":

    render_title()

    Homescreen.loop()
    if Homescreen.donext == 'load':
        Main.current_room = load()
    else:
        pass
    Main.game_loop()
