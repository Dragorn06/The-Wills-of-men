import pygame

pygame.init()

# setting up important pygame constants
WINWIDTH, WINHIEGHT = 640, 480
CLOCK = pygame.time.Clock()
DISPLAY = pygame.display.set_mode((WINWIDTH, WINHIEGHT))

# fonts
BASE_FONT = pygame.font.Font('src/fonts/BitPotionExt.ttf', 28)
FANCY_FONT = pygame.font.Font('src/fonts/antiquity-print.ttf', 26)