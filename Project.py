import sys
import pygame

import MemoryCards.memory_cards
import SimonSays.simon_says
import Shooter.shooter
import WhackAMole.whack_a_mole

def main(screen):

    #Load the game logo
    game_logo_image = pygame.image.load("Logo.PNG")
    logo_width = game_logo_image.get_width() // 2
    logo_height = game_logo_image.get_height() // 2
    game_logo_image = pygame.transform.scale(game_logo_image, (logo_width, logo_height))
    game_logo_image_rect = game_logo_image.get_rect()
    game_logo_image_rect.centerx = screen.get_rect().centerx - 10
    game_logo_image_rect.centery = screen.get_rect().centery - 200

    # Load the background image
    background_image = pygame.image.load("Game_Art/christmas_bg.png")
    
    # Scale the background image to fit the screen size
    background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))


    # Load button images
    game_button_image = pygame.image.load("Shooter/FreeAssets/UI/button/buttonLong_blue.png")

    # Get the size of the button images
    memory_cards_button_rect = game_button_image.get_rect()
    shooter_button_rect = game_button_image.get_rect()
    simon_says_button_rect = game_button_image.get_rect()
    whack_a_mole_button_rect = game_button_image.get_rect()

    # Adjust the button positions
    memory_cards_button_rect.x = screen.get_width() / 2.5
    memory_cards_button_rect.y = screen.get_height() - memory_cards_button_rect.height - 400

    shooter_button_rect.x = screen.get_width() / 2.5
    shooter_button_rect.y = screen.get_height() - shooter_button_rect.height - 300

    simon_says_button_rect.x = screen.get_width() / 2.5
    simon_says_button_rect.y = screen.get_height() - simon_says_button_rect.height - 200

    whack_a_mole_button_rect.x = screen.get_width() / 2.5
    whack_a_mole_button_rect.y = screen.get_height() - whack_a_mole_button_rect.height - 100

    # Define font for button text
    font = pygame.font.Font(None, 25)
    text_color = (0, 0, 0)

    memory_cards_button_text = font.render("Play Memory Cards", True, text_color)
    shooter_button_text = font.render("Play Space Defender", True, text_color)
    simon_says_button_text = font.render("Play Simon Says", True, text_color)
    whack_a_mole_button_text = font.render("Play Whack a Mole", True, text_color)

    # Get the position for the text to be centered on the buttons
    memory_cards_text_rect = memory_cards_button_text.get_rect(center=memory_cards_button_rect.center)
    shooter_text_rect = shooter_button_text.get_rect(center=shooter_button_rect.center)
    simon_says_text_rect = simon_says_button_text.get_rect(center=simon_says_button_rect.center)
    whack_a_mole_text_rect = whack_a_mole_button_text.get_rect(center=whack_a_mole_button_rect.center)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if memory_cards_button_rect.collidepoint(mouse_pos):
                    MemoryCards.memory_cards.main_game()
                elif shooter_button_rect.collidepoint(mouse_pos):
                    Shooter.shooter.main_menu(screen)
                elif simon_says_button_rect.collidepoint(mouse_pos):
                    SimonSays.simon_says.main_game()
                elif whack_a_mole_button_rect.collidepoint(mouse_pos):
                    WhackAMole.whack_a_mole.main_game()

        screen.blit(background_image, (0, 0))

        # Draw the buttons
        screen.blit(game_button_image, memory_cards_button_rect.topleft)
        screen.blit(game_button_image, shooter_button_rect.topleft)
        screen.blit(game_button_image, simon_says_button_rect.topleft)
        screen.blit(game_button_image, whack_a_mole_button_rect.topleft)

        # Draw the button texts
        screen.blit(memory_cards_button_text, memory_cards_text_rect)
        screen.blit(shooter_button_text, shooter_text_rect)
        screen.blit(simon_says_button_text, simon_says_text_rect)
        screen.blit(whack_a_mole_button_text, whack_a_mole_text_rect)
        
        # Draw the game logo
        screen.blit(game_logo_image, game_logo_image_rect)

        # Update the display
        pygame.display.flip()

    # Quit pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    # Initialize pygame
    pygame.init()

    # Define screen dimensions
    screen_width = 1024
    screen_height = 768

    # Create the game screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("FUN-ctional Fitness Games")

    # Start the main menu
    main(screen)
