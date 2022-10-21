import pygame
import textwrap
import sys

# initialising pygame
pygame.init()

# setting up important pygame constants
WINWIDTH, WINHIEGHT = 640, 480
CLOCK = pygame.time.Clock()
DISPLAY = pygame.display.set_mode((WINWIDTH, WINHIEGHT))
BASE_FONT = pygame.font.Font(None, 26)

# blue print for a room
class Room():

    change_room = True

    def __init__(self, name, description):
        self.name = name  # the name of the room, used as the title
        self.description = description  # the description fo the room the player is shown
        self.contents = [] # any items in the room
        self.exits = {}  # any exits the room has
        self.hidden_exits = {} # any exits which are hidden - found with "explore"
        self.locked_exits = {} # any exit the player cannot go through

    # setting the window caption to the room title
    def set_title(self):

      title = BASE_FONT.render(self.name, True, (255,255,255))
      
      title_rect = title.get_rect(center = (WINWIDTH // 2, 10))

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
        
      pygame.draw.rect(DISPLAY, (255, 255, 255), pygame.Rect(8, 28, (WINWIDTH/3)+15, dcr_height), 2)

    # changing the room the player is in
    def change(self, direction):
        # hcecks if the direction wanted is possible
        for exit in self.exits:
            if exit in direction:
              
                # sets the players current room to the new room
                main.current_room = self.exits[exit]

                main.current_room.set_title()
              
    def removeitem(self, item):
      self.contents.remove(item)

      self.description = self.description.replace(item.description, '')

      main.current_room.set_description()
      
class Item():
    def __init__(self, name, description):
      self.name = name # the name of the item
      self.description = description
      self.usage = None # the usage of the item
      self.hidden = False

class Inventory:
  contents = []

  @classmethod
  def additem(cls, item):
    cls.contents.append(item)

  @classmethod
  def display_inventory(cls):

    Inv_height = 0
    Inv_y = 30
    
    for item in cls.contents:

      Inv_height += 18

      item_surface_i = BASE_FONT.render(item.name, True, (255, 255, 255))

      DISPLAY.blit(item_surface_i, (WINWIDTH-(WINWIDTH/3)+2, Inv_y))

      Inv_y += 15
      
    pygame.draw.rect(DISPLAY, (255, 255, 255), pygame.Rect(WINWIDTH-(WINWIDTH/3), 28, ((WINWIDTH/4)), Inv_height), 2)
  
      
# creating items 
Torch = Item('Torch',' On the wall there is a lit Torch.')
Coal_barrel = Item('Barrel of coal', ' In the corner there is a barrel of coal.')

#setting up rooms
Dark_Room = Room('Dark Room', "You're in a dark cave. It is pitch black but you begin to feel your way around the room")

Lake = Room('Lake of Dreams', 'You walk into a dimly lit cavern. In the center is a glowing blue lake. On the wall there is a lit Torch.')

Abandoned_forge = Room('Abandoned Forge', 'You walk into a new room. It appears to be an old forge with old will forging equipment and an anvil. there is a thin been of light coming into the room from a man made hole in the ceiling. In the corner there is a barrel of coal.')

# Setting up room exits
Dark_Room.exits = {"west": Lake,
                   "east": Abandoned_forge}
Lake.exits = {"east": Dark_Room}
Abandoned_forge.exits = {"west": Dark_Room}

# setting up locked exits
Dark_Room.locked_exits_exits = {"north": None}

# setting up hidden exits
Dark_Room.hidden_exits = {"north": None}

# setting up the contents of rooms
Dark_Room.contents = []
Lake.contents = [Torch]
Abandoned_forge.contents = [Coal_barrel]

class main():
  
    # the room the player is in
    current_room = Dark_Room

    pygame.display.set_caption('The Wills of Men')

    # main game loop
    @staticmethod
    def game_loop():

        input_text = ''.lower()

        while running:

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

            main.current_room.set_description()
            main.current_room.set_title()

            Inventory.display_inventory()
              
            pygame.display.flip()
            CLOCK.tick(60)

    @staticmethod
    def action(input_text):

        # splits the input text string into an arrary of strings
        split_input = input_text.split()

        # checks the first word against a list of actions
        if "go" == split_input[0]:

          # changes the room using the second word as an argument
          main.current_room.change(split_input[1])

        elif "get" == split_input[0]:
          for item in main.current_room.contents:
            
            if split_input[1] in item.name.lower() :
              if not item.hidden:
                Inventory.additem(item)
                main.current_room.removeitem(item)
              
        elif "explore" == split_input[0]:
          pass
        elif "use" == split_input[0]:
          pass

if __name__ == "__main__":

  running = True

  main.current_room.set_title()
  
  main.game_loop()