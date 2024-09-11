import pygame
import sys
from name_handler import get_player_names, choose_random_referee, draw_text
from command_handler import get_commands, pick_commands_for_round


pygame.init()

# Set up display
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Simon Says')

# Set up font
font = pygame.font.Font(None, 30)

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game loop
def game_loop(players, referee, commands_for_round):
    current_command_index = 0
    round_in_progress = True
    while round_in_progress:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        # Display referee and current command
        draw_text(screen, f"Referee: {referee}", font, BLACK, 50, 50)
        if current_command_index < len(commands_for_round):
            command = commands_for_round[current_command_index]
            draw_text(screen, f"Command: {command}", font, BLACK, 50, 100)
        else:
            round_in_progress = False
            draw_text(screen, "Round Over!", font, BLACK, 50, 150)

        current_command_index += 1 if current_command_index < len(commands_for_round) else 0

        pygame.display.update()
        pygame.time.wait(1000)  # Wait for 1 second between commands

# Main function
def main():
    players = get_player_names(screen, font, WHITE, BLACK)

    referee = choose_random_referee(players)

    commands = get_commands(screen, font, WHITE, BLACK)


    # Pick 5 random commands for this round
    commands_for_round = pick_commands_for_round(commands)

    # Start the main game loop
    game_loop(players, referee, commands_for_round)

if __name__ == "__main__":
    main()
