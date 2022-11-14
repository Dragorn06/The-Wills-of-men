import pygame
import sys
from .constants import WINWIDTH, WINHIEGHT, CLOCK, DISPLAY, BASE_FONT, FANCY_FONT

class Homescreen:

    SMALL_FONT_1 = pygame.font.Font('structure/fonts/antiquity-print.ttf', 16)
    SMALL_FONT_2 = pygame.font.Font('structure/fonts/BitPotionExt.ttf', 24)

    donext = None
    input_text = ''.lower()

    by = SMALL_FONT_1.render("by Dragorn06", True, (255,255,255))
    prompt = SMALL_FONT_2.render('Type "start" to begin and "load" to load a save. To quit type "quit".', True, (255,255,255))
    title = FANCY_FONT.render("THE WILLS OF MEN", True, (255, 255, 255))

    title_rect = title.get_rect(center=(WINWIDTH // 2, WINHIEGHT//2))
    by_rect = by.get_rect(center=(WINWIDTH // 2, WINHIEGHT//2+32))
    prompt_rect = prompt.get_rect(center=(WINWIDTH // 2, WINHIEGHT//2+128))

    center_y = title_rect.y
  
    @classmethod
    def loop(cls):
        while True:

            DISPLAY.fill((0, 0, 0))

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_BACKSPACE:

                        cls.input_text = cls.input_text[:-1]

                    elif event.key == pygame.K_RETURN:

                        if cls.input_text == "start":
                            cls.input_text = ''.lower()
                            cls.donext = "start"
                            continue

                        if cls.input_text == "load":
                            cls.input_text = ''.lower()
                            cls.donext = 'load'
                            break
                            

                        if cls.input_text == "quit":
                            cls.input_text = ''.lower()
                            pygame.quit()
                            sys.exit()

                        cls.input_text = ''.lower()

                    else:
                        cls.input_text += event.unicode

            # Rendering the players input as it is typed
            text_surface = BASE_FONT.render(cls.input_text, True,
                                            (255, 255, 255))
            DISPLAY.blit(text_surface, (10, WINHIEGHT - 32))

            DISPLAY.blit(cls.title, cls.title_rect)
            DISPLAY.blit(cls.by, cls.by_rect)
            DISPLAY.blit(cls.prompt, cls.prompt_rect)
          
            pygame.display.flip()
            CLOCK.tick(60)

            if cls.donext is not None:
              break

