"""
A file containing constants used by the whole game
"""

import pygame

pygame.init()

# setting up important pygame constants
WINWIDTH, WINHIEGHT = 1280,720
CLOCK = pygame.time.Clock()
DISPLAY = pygame.display.set_mode((WINWIDTH, WINHIEGHT), pygame.RESIZABLE|pygame.SCALED)


# fonts
BASE_FONT = pygame.font.Font('assets/fonts/BitPotionExt.ttf', 28, )
FANCY_FONT = pygame.font.Font('assets/fonts/antiquity-print.ttf', 26) 
TITLE_FONT = pygame.font.Font('assets/fonts/antiquity-print.ttf', 16)
FLAVOUR_TEXT_FONT = pygame.font.Font('assets/fonts/BitPotionExt.ttf', 24)