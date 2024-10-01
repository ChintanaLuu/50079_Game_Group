import pygame
import random
import sys
from SimonSays.name_handler import draw_text

# Function to get a list of commands from the referee
def get_commands(screen, font, WHITE, BLACK):
    commands = []
    input_active = True
    current_command = ''
    
    while input_active:
        screen.fill(WHITE)
        draw_text(screen, "Current Command: " + current_command, font, BLACK, 50, 150)
        y_offset = 200
        for command in commands:
            draw_text(screen, command, font, BLACK, 50, y_offset)
            y_offset += 30

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if current_command == '' and len(commands) >= 3:
                        input_active = False
                    elif current_command != '':
                        commands.append(current_command)
                        current_command = ''
                elif event.key == pygame.K_BACKSPACE:
                    current_command = current_command[:-1]
                else:
                    current_command += event.unicode

        pygame.display.update()

    return commands


# Function to randomly pick 5 commands from the list for the current round
def pick_commands_for_round(commands, round_length=5):
    if len(commands) < 3:
        raise ValueError("There should be at least 3 commands.")
    
    return random.choices(commands, k=round_length)