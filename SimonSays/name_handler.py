import pygame
import sys
import random

#Function to get player names
def get_player_names(screen, font, WHITE, BLACK):
    players = []
    input_active = True
    player_name = ''
    while input_active:
        screen.fill(BLACK)
        draw_text(screen, "Enter player names.", font, WHITE, 40, 40)
        draw_text(screen, "Press Enter after each name.", font, WHITE, 40, 80)
        draw_text(screen, "Leave blank and press Enter when done.", font, WHITE, 40, 120)
        draw_text(screen, "Current Input: " + player_name, font, WHITE, 40, 160)
        y_offset = 200
        for name in players:
            draw_text(screen, name, font, WHITE, 40, y_offset)
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