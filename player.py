# player.py
import pygame

def get_player_name(screen, current_name=""):
    """Capture player name via keyboard input. If current_name is provided, allow changing it."""
    font = pygame.font.Font(None, 36)
    player_name = current_name  # Start with the current name if available
    input_active = True

    while input_active:
        screen.fill((0, 0, 0))  # Clear the screen
        prompt_text = font.render(f"Enter your name and press Enter: {player_name}", True, (255, 255, 255))
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
