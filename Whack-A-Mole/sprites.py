import pygame
pygame.init()

#import abc # abstract

# Create Sprite Class


# Mole
class Mole(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Game_Art/R (9).png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (0,0))
        #self.rect.x



# Rose
