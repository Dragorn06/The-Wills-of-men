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

class verb(word):
      def __init__(self, name, nouns, action=None):
          super().__init__(name)

          self.nouns = nouns
          self.action = action

class noun(word):
    def __init__(self, name):
        super().__init__(name)

    def destroy_collider(self):
        self.rect = None