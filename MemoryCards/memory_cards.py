import pygame
import random
import os
import json
from card import Card


def main_game():
    print(pygame.ver)

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1024, 768)) # Define the screen size
    pygame.display.set_caption("Memory Match Game") # Set the window caption
    clock = pygame.time.Clock() # Setting up game clock for frame rate

    # Add background image
    bg_img = pygame.image.load('MemoryCards/images/christmas_bg.png')
    bg_img_rect = bg_img.get_rect(topleft = (0,0))

    def initialize_game():
        # Load images and assign identifiers
        images = {
            "bauble": pygame.image.load("./MemoryCards/images/bauble.png"),
            "gingerbread": pygame.image.load("./MemoryCards/images/gingerbread.png"),
            "holly": pygame.image.load("./MemoryCards/images/holly.png"),
            "milk_and_cookies": pygame.image.load("./MemoryCards/images/milk_and_cookies.png"),
            "present": pygame.image.load("./MemoryCards/images/present.png"),
            "santas_hat": pygame.image.load("./MemoryCards/images/santas_hat.png"),
            "wreath": pygame.image.load("./MemoryCards/images/wreath.png"),
            "xmasTree": pygame.image.load("./MemoryCards/images/xmasTree.png"),
        }

        # Define grid properties
        rows = 4
        cols = 4
        horizontalSpacing = 75
        spacing = 20
        top_padding = 50  # Add padding at the top
        card_width = (1024 - (cols + 1) * horizontalSpacing) / cols # Calculate the card width and height with spacing around them 
        card_height = (768 - top_padding - (rows + 1) * spacing) / rows

        # Create a list of image pairs
        pairs = list(images.items()) * 2  # Multiply by 2 to create pairs

        # Shuffle the pairs
        random.shuffle(pairs)

        # Generate cards using the shuffled pairs
        cards = []
        for i in range(rows * cols):
            row = i // cols
            col = i % cols
            x = col * (card_width + horizontalSpacing) + horizontalSpacing
            y = row * (card_height + spacing) + spacing + top_padding
            identifier, image = pairs[i]
            backImage = pygame.image.load("MemoryCards/images/xmas_card_back.png")
            card = Card(x, y, card_width, card_height, image, identifier, backImage)
            cards.append(card)
        return cards

    # Game loop
    running = True
    cards = initialize_game()
    first_flipped_card = None
    second_flipped_card = None
    tries = 0  # Counter for the number of attempts
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
                            tries += 1  # Increment the tries counter when a second card is flipped

            if first_flipped_card and second_flipped_card:
                #
                screen.blit(bg_img, bg_img_rect)
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

        # Check if the board is cleared
        if not cards:
            # Display a message or wait a bit before restarting
            pygame.time.wait(1000)
            cards = initialize_game()
            tries = 0  # Reset the tries counter for the new game
        
        # fill the screen with background to wipe away anything from last frame
        screen.blit(bg_img, bg_img_rect)
        for card in cards:
            card.draw(screen)

        # Display the number of tries
        font = pygame.font.Font(None, 36)
        tries_text = font.render(f"Tries: {tries}", True, (255, 255, 255))
        screen.blit(tries_text, (20, 20))

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()