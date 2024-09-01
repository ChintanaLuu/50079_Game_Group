import pygame
import sys

# Initialize pygame
pygame.init()

# Define screen dimensions
screen_width = 800
screen_height = 600

# Create the game screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("shooter game")

# Set background color to white
white = (255, 255, 255)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with white
    screen.fill(white)
    
    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
