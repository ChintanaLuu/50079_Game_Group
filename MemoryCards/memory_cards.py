import pygame
import random
from MemoryCards.card import Card
from leaderboard import update_leaderboard

def main_game(player_name):
    print(pygame.ver)

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1024, 768)) # Define the screen size
    pygame.display.set_caption("Memory Match Game") # Set the window caption
    clock = pygame.time.Clock() # Setting up game clock for frame rate

    # Add background image
    bg_img = pygame.image.load('MemoryCards/images/christmas_bg.png')
    bg_img_rect = bg_img.get_rect(topleft = (0,0))

    # Define color
    black = (0, 0, 0)

    # Load the pause button images
    pause_button_image = pygame.image.load("Shooter/FreeAssets/UI/button/pause_button.png")
    pause_button_pressed_image = pygame.image.load("Shooter/FreeAssets/UI/button/pause_button_press.png")
    
    # Load the menu button images
    menu_button_image = pygame.image.load("Shooter/FreeAssets/UI/button/menu_button.png")
    menu_button_pressed_image = pygame.image.load("Shooter/FreeAssets/UI/button/menu_button_press.png")
    
    # Resize the pause button since the asset is too small
    scale = 3
    pause_button_width = pause_button_image.get_width() * scale
    pause_button_height = pause_button_image.get_height() * scale
    pause_button_image = pygame.transform.scale(pause_button_image, (pause_button_width, pause_button_height))
    pause_button_pressed_image = pygame.transform.scale(pause_button_pressed_image, (pause_button_width, pause_button_height))
    
    # Resize the menu buttons
    menu_button_width = menu_button_image.get_width() * 2
    menu_button_height = menu_button_image.get_height() * 2
    resume_button_image = pygame.transform.scale(menu_button_image, (menu_button_width, menu_button_height))
    resume_button_pressed_image = pygame.transform.scale(menu_button_pressed_image, (menu_button_width, menu_button_height))
    exit_menu_button_image = resume_button_image
    exit_menu_button_pressed_image = resume_button_pressed_image


    # Get rects for the buttons
    pause_button_rect = pause_button_image.get_rect()
    resume_button_rect = resume_button_image.get_rect()
    exit_menu_button_rect = resume_button_image.get_rect()


    # Set the buttons' positions (center of the screen)
    pause_button_rect.x = 25
    pause_button_rect.y = 25
    resume_button_rect.centerx = screen.get_rect().centerx
    exit_menu_button_rect.centerx = screen.get_rect().centerx


    # Position the Resume button a little bit above the Exit button
    resume_button_rect.centery = screen.get_rect().centery - 50
    exit_menu_button_rect.centery = screen.get_rect().centery + 50


    # Show and hide the Resume and Exit buttons
    show_pause_menu = False
    pause_button_pressed = False
    resume_button_pressed = False
    exit_menu_button_pressed = False
    show_restart_button = False

        # Define font for the button text
    font = pygame.font.Font(None, 36)
    
    # Render the text for the buttons
    resume_text = font.render("Resume", True, black)
    exit_text = font.render("Exit", True, black)


    # Get the rects for the text to center them on the buttons
    resume_text_rect = resume_text.get_rect(center=resume_button_rect.center)
    exit_text_rect = exit_text.get_rect(center=exit_menu_button_rect.center)







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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle pause, resume, restart, and exit button events
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Check if the pause button is clicked
                if not show_restart_button and pause_button_rect.collidepoint(mouse_pos):
                    pause_button_pressed = True

                # Check if the Resume button is clicked
                if show_pause_menu and resume_button_rect.collidepoint(mouse_pos):
                    resume_button_pressed = True

                # Check if the Exit button is clicked
                if show_pause_menu and exit_menu_button_rect.collidepoint(mouse_pos):
                    exit_menu_button_pressed = True


            # Detect mouse button up and switch back to normal images
            if event.type == pygame.MOUSEBUTTONUP:
                if pause_button_pressed:
                    pause_button_pressed = False
                    show_pause_menu = True

                if resume_button_pressed:
                    resume_button_pressed = False
                    show_pause_menu = False

                if exit_menu_button_pressed:
                    exit_menu_button_pressed = False
                    from Project import main
                    main(screen)


            # Check if the game is not paused
            if not show_pause_menu and not show_restart_button:
                # Handle game logic (flipping cards)
                if event.type == pygame.MOUSEBUTTONDOWN:  # Capture mouse click events
                    pos = pygame.mouse.get_pos()  # Get the position of the mouse click
                    for card in cards:
                        if card.rect.collidepoint(pos) and not card.is_flipped and not card.is_matched:
                            card.flip()
                            if first_flipped_card is None:
                                first_flipped_card = card  # Store the first flipped card
                            elif second_flipped_card is None:
                                second_flipped_card = card
                                tries += 1  # Increment the tries counter when a second card is flipped

        # Check if two cards are flipped
        if first_flipped_card and second_flipped_card:
            screen.blit(bg_img, bg_img_rect)
            for card in cards:
                card.draw(screen)
            pygame.display.update()
            pygame.time.wait(500)  # Briefly show the cards for 0.5 seconds
            if first_flipped_card.identifier == second_flipped_card.identifier:
                first_flipped_card.is_matched = True
                second_flipped_card.is_matched = True
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
            # Update the leaderboard
            update_leaderboard(player_name, tries, "memory_match", scoring_type= "lowest")

            pygame.time.wait(1000)
            cards = initialize_game()
            tries = 0

        # Generate the tries_text here before calling screen.blit()
        tries_text = font.render(f"Tries: {tries}", True, (255, 255, 255))

        # Draw the game screen
        screen.blit(bg_img, bg_img_rect)
        for card in cards:
            card.draw(screen)

        # Draw the pause button and the tries text
        screen.blit(pause_button_image, pause_button_rect)
        screen.blit(tries_text, ((screen.get_width()/2 - 30), 20))

        # Draw pause menu if needed
        if show_pause_menu:
            screen.blit(resume_button_image, resume_button_rect)
            screen.blit(exit_menu_button_image, exit_menu_button_rect)

            # Draw text on buttons
            screen.blit(resume_text, resume_text_rect)
            screen.blit(exit_text, exit_text_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()