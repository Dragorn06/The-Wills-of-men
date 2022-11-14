import pygame

pygame.init()

# setting up important pygame constants
WINWIDTH, WINHIEGHT = 640, 480
CLOCK = pygame.time.Clock()
DISPLAY = pygame.display.set_mode((WINWIDTH, WINHIEGHT))
BASE_FONT = pygame.font.Font('structure/fonts/BitPotionExt.ttf', 26)
FANCY_FONT = pygame.font.Font('structure/fonts/antiquity-print.ttf', 26)