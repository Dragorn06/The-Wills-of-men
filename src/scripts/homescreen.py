"""
This file acts almost as its own program functioning as a homescreen for the game
"""

import sys
import pygame
from .constants import WINWIDTH, WINHIEGHT, CLOCK, DISPLAY, BASE_FONT, FANCY_FONT, TITLE_FONT, FLAVOUR_TEXT_FONT


class Homescreen:
    """The homescreen class which renders the homescreen and takes some limmited input"""



    donext = None
    input_text = ''.lower()

    made_by = TITLE_FONT.render("made by Dragorn06", False, (255, 255, 255))
    prompt = FLAVOUR_TEXT_FONT.render(
        'Type "start" to begin and "load" to load a save. To quit type "quit".',
        True, (255, 255, 255))
    title = FANCY_FONT.render("THE WILLS OF MEN", True, (255, 255, 255))

    title_rect = title.get_rect(center=(WINWIDTH // 2, WINHIEGHT // 2))
    made_by_rect = made_by.get_rect(
        center=(WINWIDTH // 2, WINHIEGHT // 2 + 32))
    prompt_rect = prompt.get_rect(center=(WINWIDTH // 2, WINHIEGHT // 2 + 128))

    center_y = title_rect.y

    @classmethod
    def loop(cls):
        """A small loop which allows the homescreen to render in real time"""
        while True:

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_BACKSPACE:

                        cls.input_text = cls.input_text[:-1]

                    elif event.key == pygame.K_RETURN:
                        cls.action()

                    else:
                        cls.input_text += event.unicode

                elif event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()

            DISPLAY.fill((0, 0, 0))
            # Rendering the players input as it is typed
            text_surface = BASE_FONT.render(cls.input_text, True,
                                            (255, 255, 255))
            DISPLAY.blit(text_surface, (10, WINHIEGHT - 32))

            DISPLAY.blit(cls.title, cls.title_rect)
            # DISPLAY.blit(cls.made_by, cls.made_by_rect)
            DISPLAY.blit(cls.prompt, cls.prompt_rect)

            pygame.display.flip()
            CLOCK.tick(60)

            if cls.donext is not None:
                break

    @classmethod
    def action(cls):
        """does an action based on the input"""
        if cls.input_text == "start":
            cls.input_text = ''.lower()
            cls.donext = "start"

        if cls.input_text == "load":
            cls.input_text = ''.lower()
            cls.donext = 'load'

        if cls.input_text == "quit":
            cls.input_text = ''.lower()
            pygame.quit()
            sys.exit()

        cls.input_text = ''.lower()