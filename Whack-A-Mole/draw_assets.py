import pygame
pygame.init()

def draw_holes(spawnDict, screen):
    hole_sprite = pygame.image.load('Game_Art/Circle.png').convert_alpha()
    hole_sprite = pygame.transform.smoothscale_by(hole_sprite, (0.1,0.1))
    for position in spawnDict.values():
        screen.blit(hole_sprite, position)


# def draw_mole(active_mole_position, screen):
#     mole_sprite = pygame.image.load('Game_Art/R (9).png').convert_alpha()
#     # Get rect and resize mole sprite
#     mole_rect = mole_sprite.get_rect(topleft=active_mole_position)
#     mole_sprite = pygame.transform.smoothscale_by(mole_sprite, (0.1, 0.1))
#     mole_rect = mole_sprite.get_rect(topleft=active_mole_position)  # Update rect after resizing. Positioning/placing from top left pixel of image.

#     screen.blit(mole_sprite, mole_rect.topleft)