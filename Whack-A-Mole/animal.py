import pygame
pygame.init()

screen = ()

# Create Sprite Class
# Abstract class. Mole and Friendly Animal

class Animal(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, imgpath=''):

        self.x = x
        self.y = y
        self.image = pygame.load(f"{imgpath}") # Abstract
        self.rect = self.image.get_rect()


    def spawn(self, screen, x, y, waitTime=int):
        screen.blit(x, y)
        pygame.wait(waitTime)
    

# Mole

class Mole(Animal):
    #__super__.()
    def __init__():
        pass