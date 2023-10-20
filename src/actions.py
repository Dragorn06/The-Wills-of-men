import pygame

class word(pygame.sprite.Sprite):
        
    def __init__(self, name):
        self.name = name
        self.clicked  = False
        self.rect = None

    def __str__(self):
        return self.name
      
    def update(self):
        if self.clicked:
            self.clicked = False
        else:
            self.clicked = True

    def reset(self):
        self.clicked = False

class Verb(word):
      def __init__(self, name, nouns, action=None):
          super().__init__(name)

          self.nouns = nouns
          self.action = action

class Noun(word):
    def __init__(self, name, verbs=[None]):
        super().__init__(name)
        self.verbs = verbs

    def disable_collider(self):
        self.colliable = False


class Misc_Button(word):
    def __init__(self, name, action=None):
        super().__init__(name)

        self.action = action

    def execute_action(self):
        self.action()

