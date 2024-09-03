import pygame
pygame.init()

#import abc # abstract

# Create Sprite Class
# Abstract class. Mole and Friendly Animal

# class LivingObject(pygame.sprite.Sprite):
#     def __init__(self, x=0, y=0, imgpath1='', sndpath=''): #imgpath2=None,

#         self.x = x
#         self.y = y
#         self.image = pygame.load(f"{imgpath1}")
#         self.rect = self.image.get_rect(topleft = (0,0))
#         self.death_sound = pygame.mixer.Sound(f"{sndpath}")

#     def spawn(self, screen, x, y, waitTime=int):
#         screen.blit(x, y)
#         pygame.wait(waitTime)

#     def get_sprite_rect(self):
#         return self.rect
    
#     def animate_self(self, imgpath1): #, imgpath2=None):
#         # Only animate if the sprite exists!
#         self.image = pygame.image.load(f"{imgpath1}")
#         screen.blit(imgpath1, screen)
#         #pygame.time.wait(0.5)
#         #self.image = pygame.image.load(f"{imgpath2}")


# Mole
class Mole():
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Game_Art/R (9).png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (0,0))
        self.rect.x



# Rose
