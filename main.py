"""
T H E   W I L L S   O F   M E N
A high fantasy text adventure game
by Dragorn06
"""

import sys

import pygame

import room

WINWIDTH = 640
WINHIEGHT = 480

running = True

pygame.init()

CLOCK = pygame.time.Clock()

DISPLAY = pygame.display.set_mode((WINWIDTH, WINHIEGHT))
pygame.display.set_caption('The Wills of Men')

ROOM_LIST = [room.Title_Screen, room.Dark_Room]
Room_in = room.Dark_Room

BASE_FONT = pygame.font.Font(None, 28)
WHITE = (255, 255, 255)

input_text = ''
responce_text = ''
inventory = []



class main:


  @classmethod
  def main(self):
    global input_text, responce_text

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
                    main.cmd_handler(Room_in)

                else:
                    input_text += event.unicode


      
        text_surface = BASE_FONT.render(input_text, True, WHITE)

        title_surface = BASE_FONT.render(Room_in.name, True, WHITE)
        title_rect = DISPLAY.get_rect(center = (320, 240))
        description_surface = BASE_FONT.render(Room_in.description, True, WHITE)
      
        responce_surface = BASE_FONT.render(responce_text, True, WHITE)


        
        pygame.draw.rect(DISPLAY,(255, 255, 255),(200,200,0,0))
      
        DISPLAY.blit(text_surface, (10, WINHIEGHT - 32))
        DISPLAY.blit(title_surface, (title_rect.centerx, 0))
        DISPLAY.blit(responce_surface,(10, WINHIEGHT - 64))
        DISPLAY.blit(description_surface,(10, WINHIEGHT*0.25))
  
        pygame.display.flip()
        CLOCK.tick(60)


  
  @classmethod
  def cmd_handler(self, room):
    global input_text, responce_text

    if 'get' in input_text:
      for item in room.itemlist:
        if item.name.lower() in input_text:
          
          inventory.append(item)

          responce_text = f'you got the {item.name}'
          print('yo')
        else:
          print('1')
    else:
      print('2')
    input_text = ''


main.main()
