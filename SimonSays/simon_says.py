import pygame
import sys
from SimonSays.name_handler import get_player_names, choose_random_referee, draw_text
from SimonSays.command_handler import get_commands, pick_commands_for_round
from Project import main

pygame.init()

# Set up display
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Simon Says')

# Set up font
font = pygame.font.Font(None, 30)
large_font = pygame.font.Font(None, 100)

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 236, 101)
BLUE = (0,0,255)

# Menu
menu_bg = pygame.image.load("SimonSays/ChristmasAssets/bgSnowyWindow.png")
menu_rect = menu_bg.get_rect(topleft=(0,0))

# Background
xmas_bg = pygame.image.load("SimonSays/ChristmasAssets/bgChristmasLights.png")
xmas_bg_rz = pygame.transform.smoothscale(xmas_bg,(screen.get_width(), screen.get_height() - 30)) # Fix height so it is not as stretched.
xmas_bg = xmas_bg_rz
xmas_bg_rect = xmas_bg.get_rect(topleft=(0,0))

class Button:
    def __init__(self, x, y, width, height, text, color, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color

    def draw(self, screen, font):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = font.render(self.text, True, self.text_color)
        screen.blit(text_surface, (self.rect.x + (self.rect.width - text_surface.get_width()) // 2,
                                   self.rect.y + (self.rect.height - text_surface.get_height()) // 2))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

pause_button = Button(900, 20, 100, 50, 'Pause', GREEN, BLACK)
resume_button = Button(400, 300, 200, 50, 'Resume', GREEN, BLACK)
exit_button = Button(400, 400, 200, 50, 'Exit', RED, WHITE)
restart_button = Button(400, 500, 200, 50, 'Restart', GREEN, BLACK)  

# Game loop
def game_loop(players, referee, commands_for_round):
    current_command_index = 0
    round_in_progress = True
    paused = False

    while round_in_progress:
        screen.blit(xmas_bg, xmas_bg_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if pause_button.is_clicked(pos):
                    paused = True

                if paused:
                    if resume_button.is_clicked(pos):
                        paused = False
                    if exit_button.is_clicked(pos):
                        main(screen)
                        return
                    if restart_button.is_clicked(pos):
                        main_game()  

        if not paused:
            # Display referee and current command
            draw_text(screen, f"Referee: {referee}", font, BLUE, 50, 50)
            if current_command_index < len(commands_for_round):
                command = commands_for_round[current_command_index]
                draw_text(screen, f"Simon Says: {command}", font, RED, 50, 100)
            else:
                round_in_progress = False
                draw_text(screen, "Round Over!", font, YELLOW, 50, 150)

            current_command_index += 1 if current_command_index < len(commands_for_round) else 0
            pygame.time.wait(1000)  # Wait for 1 second between commands

        pause_button.draw(screen, font)

        if paused:
            draw_pause_menu()

        pygame.display.update()

    if not round_in_progress:
        pygame.time.wait(2000)  
        start_new_round()

def draw_pause_menu():
    screen.blit(menu_bg, menu_rect)
    print("PAUSED DRAWN")
    draw_text(screen, "Game Paused", font, GREEN, 400, 200)

    resume_button.draw(screen, font)
    exit_button.draw(screen, font)
    restart_button.draw(screen, font)

    pygame.display.flip()

def start_new_round():
    players = get_player_names(screen, font, WHITE, YELLOW)

    referee = choose_random_referee(players)

    commands = get_commands(screen, font, WHITE, YELLOW)

    # Pick 5 random commands for this round
    commands_for_round = pick_commands_for_round(commands)

    # Start the main game loop again with fresh data
    game_loop(players, referee, commands_for_round)

# Main function
def main_game():
    start_new_round()

if __name__ == "__main__":
    main_game()
