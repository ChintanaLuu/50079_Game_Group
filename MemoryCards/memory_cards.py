import pygame
import random
import os
from card import Card

print(pygame.ver)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1024, 768)) # Define the screen size
pygame.display.set_caption("Memory Match Game") # Set the window caption
clock = pygame.time.Clock() # Setting up game clock for frame rate

# Game loop
running = True
card_image = pygame.image.load(r"C:\Users\ADMIN\Desktop\ProjectStudio\50079_Game_Group\MemoryCards\images\number.jpg")
card1 = Card(100, 100, 200, 400, card_image)
card2 = Card(400, 100, 200, 400, card_image)
cards = [card1, card2]
# card.is_flipped = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Capture mouse click events
            pos = pygame.mouse.get_pos()  # Get the position of the mouse click
            for card in cards:
                if card.rect.collidepoint(pos) and not card.is_flipped and not card.is_matched:
                    card.flip()
                    

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    card1.draw(screen)
    card2.draw(screen)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()