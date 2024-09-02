import pygame
import random
print(pygame.ver)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720)) # Define the screen size
pygame.display.set_caption("Memory Match Game") # Set the window caption
clock = pygame.time.Clock() # Setting up game clock for frame rate

# Game loop
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()