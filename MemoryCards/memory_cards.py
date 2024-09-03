import pygame
import random
from card import Card

print(pygame.ver)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1024, 768)) # Define the screen size
pygame.display.set_caption("Memory Match Game") # Set the window caption
clock = pygame.time.Clock() # Setting up game clock for frame rate

# Load images and assign identifiers
images = {
    "apple": pygame.image.load("./MemoryCards/images/apple.jpg"),
    "banana": pygame.image.load("./MemoryCards/images/banana.jpg"),
    "blueberry": pygame.image.load("./MemoryCards/images/blueberry.jpg"),
    "eggplant": pygame.image.load("./MemoryCards/images/eggplant.jpg"),
    "grape": pygame.image.load("./MemoryCards/images/grape.jpg"),
    "lime": pygame.image.load("./MemoryCards/images/lime.jpg"),
    "orange": pygame.image.load("./MemoryCards/images/orange.jpg"),
    "pumpkin": pygame.image.load("./MemoryCards/images/pumpkin.jpg"),
}

# Define grid properties
rows = 4
cols = 4
spacing = 20
card_width = (1024 - (cols + 1) * spacing) / cols # Calculate the card width and height with spacing around them 
card_height = (768 - (rows + 1) * spacing) / rows

# Create a list of image pairs
pairs = list(images.items()) * 2  # Multiply by 2 to create pairs

# Shuffle the pairs
random.shuffle(pairs)

# Generate cards using the shuffled pairs
cards = []
for i in range(rows * cols):
    row = i // cols
    col = i % cols
    x = col * (card_width + spacing) + spacing
    y = row * (card_height + spacing) + spacing
    identifier, image = pairs[i]
    card = Card(x, y, card_width, card_height, image, identifier)
    cards.append(card)


# Game loop
running = True
first_flipped_card = None
second_flipped_card = None
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Capture mouse click events
            pos = pygame.mouse.get_pos()  # Get the position of the mouse click
            for card in cards:
                if card.rect.collidepoint(pos) and not card.is_flipped and not card.is_matched: # Check if the click is within the boundaries of the rects
                    card.flip()
                    
                    if first_flipped_card == None:
                        first_flipped_card = card # Store the first flipped card
                    elif second_flipped_card == None:
                        second_flipped_card = card

        if first_flipped_card and second_flipped_card:
            screen.fill("purple")
            for card in cards:
                card.draw(screen)
            pygame.display.update()
            pygame.time.wait(500)  # Briefly show the cards for 1 second
            if first_flipped_card.identifier == second_flipped_card.identifier:
                first_flipped_card.is_matched = True
                second_flipped_card.is_matched = True

                # Remove the matched cards from the list
                cards.remove(first_flipped_card)
                cards.remove(second_flipped_card)
            else:
                first_flipped_card.is_flipped = False
                second_flipped_card.is_flipped = False

            # Reset the cards for the next turn
            first_flipped_card = None
            second_flipped_card = None

        
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    for card in cards:
        card.draw(screen)


    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()