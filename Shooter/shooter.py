import pygame
import sys
from GameScreen import game_screen

def main_menu(screen):
    # Define color
    white = (255, 255, 255)

    # Load button images
    start_game_button_image = pygame.image.load("FreeAssets/UI/button/buttonLong_blue.png")
    exit_game_button_image = pygame.image.load("FreeAssets/UI/button/buttonLong_blue.png")

    # Get the size of the button images
    start_game_button_rect = start_game_button_image.get_rect()
    exit_game_button_rect = exit_game_button_image.get_rect()

    # Adjust the button positions
    start_game_button_rect.x = 50
    start_game_button_rect.y = screen.get_height() - start_game_button_rect.height - 150

    exit_game_button_rect.x = 50
    exit_game_button_rect.y = screen.get_height() - exit_game_button_rect.height - 50

    # Define font for button text
    font = pygame.font.Font(None, 36)
    text_color = (0, 0, 0)
    start_game_button_text = font.render("Start Game", True, text_color)
    exit_game_button_text = font.render("Exit", True, text_color)

    # Get the position for the text to be centered on the buttons
    start_game_text_rect = start_game_button_text.get_rect(center=start_game_button_rect.center)
    exit_game_text_rect = exit_game_button_text.get_rect(center=exit_game_button_rect.center)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_game_button_rect.collidepoint(mouse_pos):
                    # Switch to the game screen when Start Game button is clicked
                    game_screen(screen)
                if exit_game_button_rect.collidepoint(mouse_pos):
                    running = False

        # Set the background to white for now, change later
        screen.fill(white)

        # Draw the button images
        screen.blit(start_game_button_image, (start_game_button_rect.x, start_game_button_rect.y))
        screen.blit(exit_game_button_image, (exit_game_button_rect.x, exit_game_button_rect.y))

        # Update the text rect after changing button positions
        start_game_text_rect = start_game_button_text.get_rect(center=start_game_button_rect.center)
        exit_game_text_rect = exit_game_button_text.get_rect(center=exit_game_button_rect.center)

        # Draw the text on the buttons
        screen.blit(start_game_button_text, start_game_text_rect)
        screen.blit(exit_game_button_text, exit_game_text_rect)

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
    pygame.display.set_caption("Shooter Game")

    # Start the main menu
    main_menu(screen)
