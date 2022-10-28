import pygame
import textwrap
import sys
import shelve

# initialising pygame
pygame.init()

# setting up important pygame constants
WINWIDTH, WINHIEGHT = 640, 480
CLOCK = pygame.time.Clock()
DISPLAY = pygame.display.set_mode((WINWIDTH, WINHIEGHT))
BASE_FONT = pygame.font.Font(None, 26)

class Inventory:
    contents = []

    @classmethod
    def additem(cls, item):
        cls.contents.append(item)

    @classmethod
    def removeItem(cls, item):
        cls.contents.remove(item)

    @classmethod
    def display_inventory(cls):

        Inv_height = 0
        Inv_y = 30

        for item in cls.contents:

            Inv_height += 18

            item_surface_i = BASE_FONT.render(item.name, True, (255, 255, 255))

            DISPLAY.blit(item_surface_i,
                         (WINWIDTH - (WINWIDTH / 3) + 2, Inv_y))

            Inv_y += 15

        pygame.draw.rect(
            DISPLAY, (255, 255, 255),
            pygame.Rect(WINWIDTH - (WINWIDTH / 3), 28, ((WINWIDTH / 4)),
                        Inv_height), 2)



class Item():
    def __init__(self, name, description):
        self.name = name  # the name of the item
        self.description = description
        self.usage = None  # the usage of the item
        self.hidden = False


# creating items
Torch = Item('Torch', ' On the wall there is a lit Torch.')
CoalBarrel = Item('Barrel of coal', ' In the corner there is a barrel of coal.')

Key = Item('Rusty key', '')

# Hidding items
Key.hidden = True

# Iem usages
'''
first word - level item is used in e.g. l1 is used in level 1
second word - what it does
'''
def l1_LightForge():
  if main.currentRoom == Abandoned_forge and Torch in Inventory.contents and CoalBarrel in Inventory.contents:
    main.responce = 'you use the coal and the torch to light the forge. Suddenly a key appears on the anvil'

    Key.description = 'There is a Rusty key on the anvil'
    Key.hidden = False

    Inventory.removeItem(CoalBarrel)

def l1_OpenDoor():
  if main.currentRoom == Dark_Room and "north" not in Dark_Room.hidden_exits: 
    
    main.responce = "you open the door"
    main.currentRoom.locked_exits.remove("north")
     

Torch.usage = l1_LightForge
CoalBarrel.usage = l1_LightForge
Key.usage = l1_OpenDoor

# blue print for a room
class Room():

    change_room = True

    def __init__(self, name, description, exploreText='you find nothing of note'):
        self.name = name  # the name of the room, used as the title
        self.description = description  # the description fo the room the player is shown
        self.exploreText = exploreText
        self.contents = []  # any items in the room
        self.Exits = {}  # any exits the room has
        self.hidden_exits = []  # any exits which are hidden - found with "explore"
        self.locked_exits = []  # any exit the player cannot go through

    # setting the window caption to the room title
    def set_title(self):

        title = BASE_FONT.render(self.name, True, (255, 255, 255))

        title_rect = title.get_rect(center=(WINWIDTH // 2, 10))

        DISPLAY.blit(title, title_rect)

    #setting the description text for a room
    def set_description(self):

        description_y = 30
        dcr_height = 0

        for i in textwrap.wrap(self.description, 25):

            dcr_height += 17

            description_surface_i = BASE_FONT.render(i, True, (255, 255, 255))

            DISPLAY.blit(description_surface_i, (10, description_y))

            description_y += 15

        pygame.draw.rect(DISPLAY, (255, 255, 255),
                         pygame.Rect(8, 28, (WINWIDTH / 3) + 15, dcr_height),
                         2)

    # changing the room the player is in
    def change(self, direction):
        # hcecks if the direction wanted is possible

          if direction in self.Exits and direction not in self.hidden_exits and direction not in self.locked_exits:

              main.responce = f'you go {direction}'

              # sets the players current room to the new room
              main.currentRoom = self.Exits[direction]

              main.currentRoom.set_title()

    def removeitem(self, item):
        self.contents.remove(item)

        self.description = self.description.replace(item.description, '')

        main.currentRoom.set_description()


#setting up rooms
Dark_Room = Room(
    'Dark Room',
    "You're in a dark cave. It is pitch black but you begin to feel your way around the room",
    'To the north of the room you find a key hole'
)

Lake = Room(
    'Lake of Dreams',
    'You walk into a dimly lit cavern. In the center is a glowing blue lake. On the wall there is a lit Torch.',
)

Abandoned_forge = Room(
    'Abandoned Forge',
    'You walk into a new room. It appears to be an old forge with old will forging equipment and an anvil. there is a thin been of light coming into the room from a man made hole in the ceiling. In the corner there is a barrel of coal.'
)

# Setting up room exits
Dark_Room.Exits = {
  "north": None,
  "east": Abandoned_forge,
  "west": Lake
}
Lake.Exits = {
  "east": Dark_Room
}
Abandoned_forge.Exits = {
  "west": Dark_Room
}

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
    currentRoom = Dark_Room

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

            cls.currentRoom.set_description()
            cls.currentRoom.set_title()
            main.render_responcetext()

            Inventory.display_inventory()

            pygame.display.flip()
            CLOCK.tick(60)

    @classmethod
    def action(cls, input_text):

        # splits the input text string into an arrary of strings
        split_input = input_text.split()

        if [] == split_input or [''] == split_input:
            pass

        # checks the first word against a list of actions
        elif "go" == split_input[0]:
            # changes the room using the second word as an argument
            cls.currentRoom.change(split_input[1])

        elif "get" == split_input[0]:

            # checks items in a room against the players input
            for item in main.currentRoom.contents:
                if split_input[1] in item.name.lower():

                    if not item.hidden:

                        Inventory.additem(item)
                        cls.responce = f'you get the {item.name}'
                        cls.currentRoom.removeitem(item)

        elif "explore" == split_input[0]:
            if Torch in Inventory.contents:
              cls.responce = f'you look around. {cls.currentRoom.exploreText}'

              cls.currentRoom.hidden_exits = []

        elif "use" == split_input[0]:          
            for item in Inventory.contents:
              
                if  split_input[1] in item.name.lower():

                    item.usage()

        elif "save" == split_input[0]:
          cls.save()
          
        elif "load" == split_input[0]:
          cls.load()
          
        else:
            cls.responce = 'I dont understand'

    @classmethod
    def render_responcetext(cls):

        responce_surface = BASE_FONT.render(cls.responce, True,
                                            (255, 255, 255))
        DISPLAY.blit(responce_surface, (10, WINHIEGHT - 57))


    @classmethod
    def save(cls):
      saveFile = shelve.open('save')

      saveFile['currentRoom'] = main.currentRoom
      saveFile['inventory'] = Inventory.contents
      
    @classmethod
    def load(cls):
      saveFile = shelve.open('save')
      
      main.currentRoom = saveFile['currentRoom']
      Inventory.contents = saveFile ['inventory']
      
if __name__ == "__main__":

    main.currentRoom.set_title()

    main.game_loop()
