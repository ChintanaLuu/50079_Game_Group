# Import pygame library
import pygame
from sys import exit
pygame.init()

clock = pygame.time.Clock()

# Define window size.
windowWidth = 1920
windowHeight = 1080

# Create app window.
screen = pygame.display.set_mode((windowWidth, windowHeight))

while True:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            if mole_rect.collidepoint(mousepos):
                print("MOLE CAUGHT!")

    pygame.Surface.fill(screen, (0,255,0))
    # Draw the mole.
    mole_sprite = pygame.image.load('Game_Art\R (9).png').convert_alpha()
    screen.blit(mole_sprite, (0,0))

    # Make mole clickable.
    mole_rect = mole_sprite.get_rect()



    # Update display screen.
    pygame.display.update()
    clock.tick(60)



