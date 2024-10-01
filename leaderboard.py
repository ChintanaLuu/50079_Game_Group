# leaderboard.py
import json
import os
import pygame
import sys

def load_leaderboard(game_name):
    """Load the leaderboard for a specific game from a JSON file."""
    leaderboard_file = f"leaderboard_{game_name}.json"
    if not os.path.exists(leaderboard_file):
        return []
    with open(leaderboard_file, "r") as f:
        return json.load(f)

def save_leaderboard(leaderboard, game_name):
    """Save the leaderboard for a specific game to a JSON file."""
    leaderboard_file = f"leaderboard_{game_name}.json"
    with open(leaderboard_file, "w") as f:
        json.dump(leaderboard, f)

def update_leaderboard(player_name, tries, game_name):
    """Update the leaderboard with the player's score for a specific game."""
    leaderboard = load_leaderboard(game_name)
    leaderboard.append({"name": player_name, "tries": tries})
    leaderboard = sorted(leaderboard, key=lambda x: x["tries"])  # Sort by number of tries
    save_leaderboard(leaderboard, game_name)

def display_leaderboard(screen, game_name):
    """Display the leaderboard for a specific game on the screen."""
    leaderboard = load_leaderboard(game_name)
    font = pygame.font.Font(None, 36)
    y_offset = 100
    # Load the background image
    background_image = pygame.image.load("Game_Art/christmas_bg.png")
    
    # Scale the background image to fit the screen size
    background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))

    # Display the top 5 players for the specific game
    for index, entry in enumerate(leaderboard[:5]):
        name_text = font.render(f"{index + 1}. {entry['name']} - {entry['tries']} tries", True, (255, 255, 255))
        screen.blit(name_text, (200, y_offset))
        y_offset += 50

    pygame.display.flip()
    pygame.time.wait(3000)  # Display for 3 seconds

def display_leaderboard_menu(screen):
    """Display the leaderboard menu where the player can choose which game's leaderboard to view."""
    font = pygame.font.Font(None, 25)
    text_color = (0, 0, 0)

    # Load the background image
    background_image = pygame.image.load("Game_Art/christmas_bg.png")
    
    # Scale the background image to fit the screen size
    background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))

    # Load button images
    game_button_image = pygame.image.load("Shooter/FreeAssets/UI/button/buttonLong_blue.png")

    # Define buttons for each game's leaderboard
    game1_button_rect = game_button_image.get_rect()
    game2_button_rect = game_button_image.get_rect()
    game3_button_rect = game_button_image.get_rect()
    
    game1_button_rect.x = screen.get_width() / 2.5
    game1_button_rect.y = 300  

    game2_button_rect.x = screen.get_width() / 2.5
    game2_button_rect.y = 400

    game3_button_rect.x = screen.get_width() / 2.5
    game3_button_rect.y = 500

    font = pygame.font.Font(None, 25)
    text_color = (0, 0, 0)

    game1_text = font.render("Memory Cards", True, text_color)
    game2_text = font.render("Space Defender", True, text_color)
    game3_text = font.render("Simon Says", True, text_color)

    game1_button_text_rect = game1_text.get_rect(center=game1_button_rect.center)
    game2_button_text_rect = game2_text.get_rect(center=game2_button_rect.center)
    game3_button_text_rect = game3_text.get_rect(center=game3_button_rect.center)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if game1_button_rect.collidepoint(mouse_pos):
                    display_leaderboard(screen, "game1")  # View Memory Cards leaderboard
                elif game2_button_rect.collidepoint(mouse_pos):
                    display_leaderboard(screen, "game2")  # View Space Defender leaderboard
                elif game3_button_rect.collidepoint(mouse_pos):
                    display_leaderboard(screen, "game3")  # View Simon Says leaderboard

        screen.blit(background_image, (0, 0))

        # Draw buttons
        screen.blit(game_button_image, game1_button_rect.topleft)
        screen.blit(game_button_image, game2_button_rect.topleft)
        screen.blit(game_button_image, game3_button_rect.topleft)

        # Draw text
        screen.blit(game1_text, game1_button_text_rect)
        screen.blit(game2_text, game2_button_text_rect)
        screen.blit(game3_text, game3_button_text_rect)

        pygame.display.flip()