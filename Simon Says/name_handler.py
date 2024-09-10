import pygame
import sys
import random

#Function to get player names
def get_player_names(screen, font, WHITE, BLACK):
    players = []
    input_active = True
    player_name = ''
    while input_active:
        screen.fill(WHITE)
        draw_text(screen, "Enter player names. Press Enter after each name.", font, BLACK, 50, 50)
        draw_text(screen, "Leave blank and press Enter when done.", font, BLACK, 50, 80)
        draw_text(screen, "Current Input: " + player_name, font, BLACK, 50, 150)
        y_offset = 200
        for name in players:
            draw_text(screen, name, font, BLACK, 50, y_offset)
            y_offset += 30
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if player_name == '':
                        input_active = False
                    else:
                        players.append(player_name)
                        player_name = ''
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode

        pygame.display.update()

    return players

def draw_text(screen, text, font, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, (x, y))

# Function to choose a random referee
def choose_random_referee(players):
    referee = random.choice(players)
    return referee