"""
T H E   W I L L S   O F   M E N
A high fantasy text adventure game
by Dragorn06
"""

import sys

import pygame

import room

# from colorama import Fore as f
# from colorama import Style as s

WINWIDTH = 1280
WINHIEGHT = 720

running = True

pygame.init()

CLOCK = pygame.time.Clock()

DISPLAY = pygame.display.set_mode((WINWIDTH, WINHIEGHT))
pygame.display.set_caption('The Wills of Men')

ROOM_LIST = [room.Title_Screen, room.Dark_Room]
Room_in = room.Title_Screen

BASE_FONT = pygame.font.Font(None, 28)
input_text = ''


def main():
    global input_text

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
                    cmd_handler()

                else:
                    input_text += event.unicode

        text_surface = BASE_FONT.render(input_text, True, (255, 255, 255))
        title_surface = BASE_FONT.render(Room_in.name, True, (255, 255, 255))
        title_rect = DISPLAY.get_rect(center=(WINWIDTH / 2, WINHIEGHT / 2))
        DISPLAY.blit(text_surface, (10, WINHIEGHT - 32))
        DISPLAY.blit(title_surface, title_rect)

        pygame.display.flip()
        CLOCK.tick(60)


def cmd_handler():
    global input_text

    input_text = ''

main()
