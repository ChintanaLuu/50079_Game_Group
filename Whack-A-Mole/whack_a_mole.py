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

    # Update display screen.
    pygame.display.update()
    clock.tick(60)