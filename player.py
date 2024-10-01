# player.py
import pygame

def get_player_name(screen, current_name=""):
    """Capture player name via keyboard input. If current_name is provided, allow changing it."""
    font = pygame.font.Font(None, 36)
    player_name = current_name  # Start with the current name if available
    input_active = True

    # Load the background image
    background_image = pygame.image.load("Game_Art/christmas_bg.png")
    
    # Scale the background image to fit the screen size
    background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))

    while input_active:
        screen.blit(background_image, (0, 0))
        prompt_text = font.render(f"Enter your name and press Enter: {player_name}", True, (0, 0, 0))
        screen.blit(prompt_text, (200, 300))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and player_name:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode

    return player_name
