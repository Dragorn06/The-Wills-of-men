import pygame
import textwrap
import sys

from src.Inv import Inventory
from src.Items import Item
from src.Rooms import Room
from src.Homescreen import Homescreen
from src.saves import save, load
from src.constants import WINWIDTH, WINHIEGHT, CLOCK, DISPLAY, BASE_FONT, FANCY_FONT

# initialising pygame
pygame.init()

# rendering functions
def display_inventory():

    Inv_height = 0
    Inv_y = 50

    for item in Inventory.contents:

        Inv_height += 20

        item_surface_i = BASE_FONT.render(item.name, True, (255, 255, 255))

        DISPLAY.blit(item_surface_i, (WINWIDTH - (WINWIDTH / 3) + 2, Inv_y))

        Inv_y += 15

    pygame.draw.rect(
        DISPLAY, (255, 255, 255),
        pygame.Rect(WINWIDTH - (WINWIDTH / 3), 50, ((WINWIDTH / 4)),
                    Inv_height), 2)


# setting the window caption to the room title
def set_title():

    title = FANCY_FONT.render(main.current_room.name, True, (255, 255, 255))

    title_rect = title.get_rect(center=(WINWIDTH // 2, 20))

    DISPLAY.blit(title, title_rect)


#setting the description text for a room
def set_description():

    description_y = 50
    dcr_height = 0

    for i in textwrap.wrap(main.current_room.description, 25):

        dcr_height += 17

        description_surface_i = BASE_FONT.render(i, True, (255, 255, 255))

        DISPLAY.blit(description_surface_i, (12, description_y))

        description_y += 15

    pygame.draw.rect(DISPLAY, (255, 255, 255),
                     pygame.Rect(8, 48, (WINWIDTH / 3) + 15, dcr_height), 2)


#setting up rooms

# creating items

Torch = Item('Torch', 0, ' On the wall there is a lit Torch.')
CoalBarrel = Item('Barrel of coal', 1,
                  ' In the corner there is a barrel of coal.')

Key = Item('Rusty key', 2, '')

# Hidding items
Key.hidden = True

# Iem usages
'''
first word - level item is used in e.g. l1 is used in level 1
second word - what it does
'''


def l1_LightForge():
    if main.current_room == Abandoned_forge and Torch in Inventory.contents and CoalBarrel in Inventory.contents:

        main.responce = 'you light the forge with the torch and coal. Suddenly a key appears on the anvil'

        Key.description = 'There is a Rusty key on the anvil'
        Key.hidden = False

        Inventory.removeItem(CoalBarrel)


def l1_OpenDoor():
    if main.current_room == Dark_Room and "north" not in Dark_Room.hidden_exits:

        main.responce = "you open the door"
        main.current_room.locked_exits.remove("north")
        Inventory.removeItem(Key)


Torch.usage = l1_LightForge
CoalBarrel.usage = l1_LightForge
Key.usage = l1_OpenDoor

# Level 1
Dark_Room = Room(
    'Dark Room', 0,
    "You're in a dark cave. It is pitch black but you begin to feel your way around the room",
    ' To the north of the room you find a key hole.')

Lake = Room(
    'Lake of Dreams',
    1,
    'You walk into a dimly lit cavern. In the center is a glowing blue lake. On the wall there is a lit Torch.',
)

Abandoned_forge = Room(
    'Abandoned Forge', 2,
    'You walk into a new room. It appears to be an old forge with old will forging equipment and an anvil. '
    'there is a thin been of light coming into the room from a man made hole in the ceiling. In the corner there is a barrel of coal.'
)

# Level 2
Crossroads = Room(
  'Crossroads', 3,
  'you find yourself at a crossroads in the mountains. There are three paths infront of you. One leads west down into a dark sprawlling forest. Another track to the east winds up high into the mountains. The last path leads down to a small hamlet far bellow you.',
)

Atvust = Room(
  'Atvust', 4,
  'you enter the village of Avust. As you walk down the narrow but clean streets the sounds of merriment begin to surround you. Soon you come to the main square to the west there is a tavern and to the east there is a market.'
)

Mountaintop = Room(
  'Mountaintop', 5,
  ''
)

Forest_entrance = Room(
  'Forest Entrance', 6,
  'You are unerved by the forrest as if the is an evil presense here. In the future there will be something here.'
)

Atvust_Market = Room(
  'Market', 7,
  'The small market you are now presented with is surprisingly lively. All around you villagers are haggling with merchants from the outer dales. Sitting quietly at one of the stands at the far end of the market is a wizard.'
)

Atvust_Tavern = Room(
  'Tavern',8 ,
  'The smell of hearty ale wafts towards you as you enter the Tavern. Once you are inside you see many people of the town including several arcinthian dwarves drinking and sining merrily. behind the bar you see the Landlord cleaning an tankard. '
)
# Setting up room exits
Dark_Room.Exits = {"north": Crossroads, "east": Abandoned_forge, "west": Lake}
Lake.Exits = {"east": Dark_Room}
Abandoned_forge.Exits = {"west": Dark_Room}
Crossroads.Exits = {"north": Atvust, "south": Dark_Room, "east": Mountaintop, "west": Forest_entrance}
Atvust.Exits = {"south": Crossroads, "west": Atvust_Tavern, "east": Atvust_Market}
Mountaintop.Exits = {"west": Crossroads}
Forest_entrance.Exits = {"east": Crossroads}
Atvust_Market.Exits = {"west": Atvust}
Atvust_Tavern.Exits = {"east": Atvust}

# setting up locked exits
Dark_Room.locked_exits = ["north"]

# setting up hidden exits
Dark_Room.hidden_exits = ["north"]

# setting up the contents of rooms
Dark_Room.contents = []
Lake.contents = [Torch]
Abandoned_forge.contents = [CoalBarrel, Key]


class main:

    # the room the player is in
    current_room = Dark_Room

    # responce
    responce = ''

    pygame.display.set_caption('The Wills of Men')

    # main game loop
    @classmethod
    def game_loop(cls):

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

                        main.action(input_text)

                        input_text = ''.lower()

                    else:
                        input_text += event.unicode

            # Rendering the players input as it is typed
            text_surface = BASE_FONT.render(input_text, True, (255, 255, 255))
            DISPLAY.blit(text_surface, (10, WINHIEGHT - 32))

            set_description()
            set_title()
            main.render_responcetext()

            display_inventory()

            pygame.display.flip()
            CLOCK.tick(60)

    @classmethod
    def action(cls, input_text):

        # splits the input text string into an arrary of strings
        split_input = input_text.split()

        if split_input in ([''],[],[' ']):
            pass

        # checks the first word against a list of actions
        elif "go" == split_input[0]:
            # changes the room using the second word as an argument

            direction = cls.current_room.change(split_input[1])

          
            if direction:

                cls.responce = f'you go {direction}'

                # sets the playrs current room to the new room
                save(cls.current_room.Id)
                cls.current_room = cls.current_room.Exits[direction]

            else:
                cls.responce = 'I dont understand'

        elif "get" == split_input[0]:

            # checks items in a room against the players input
            for item in main.current_room.contents:
                if split_input[1] in item.name.lower():

                    if not item.hidden:

                        Inventory.additem(item)
                        cls.responce = f'you get the {item.name}'
                        cls.current_room.removeitem(item)
                        save(cls.current_room.Id)

        elif "explore" == split_input[0]:
            if Torch in Inventory.contents:
                cls.responce = f'you look around.{cls.current_room.exploreText}'

                if cls.current_room.exploreText != ' you find nothing of note': 
                  cls.current_room.description += cls.current_room.exploreText
                  
                cls.current_room.hidden_exits = []

                save(cls.current_room.Id)

        elif "use" == split_input[0]:
            for item in Inventory.contents:

                if split_input[1] in item.name.lower():

                    item.usage()

        elif "save" == split_input[0]:
            save(cls.current_room.Id)
            cls.responce = 'you save'

        elif "load" == split_input[0]:
             cls.current_room = load()

        elif "quit" == split_input[0]:
            pygame.quit()
            sys.exit()

        else:
            cls.responce = 'I dont understand'

    @classmethod
    def render_responcetext(cls):

        responce_surface = BASE_FONT.render(cls.responce, True,
                                            (255, 255, 255))

        DISPLAY.blit(responce_surface, (10, WINHIEGHT - 57))

if __name__ == "__main__":

    set_title()

    Homescreen.loop()
    if Homescreen.donext == 'load':
        main.current_room = load()
    else:
        pass
    main.game_loop()
