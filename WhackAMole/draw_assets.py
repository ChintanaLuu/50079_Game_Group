import pygame
pygame.init()

def draw_holes(spawnDict, screen, imagePath):
    hole_sprite = pygame.image.load(imagePath).convert_alpha()
    hole_sprite = pygame.transform.smoothscale_by(hole_sprite, (0.1, 0.1))
    for position in spawnDict.values():
        screen.blit(hole_sprite, position)