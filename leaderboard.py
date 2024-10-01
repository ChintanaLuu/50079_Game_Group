# leaderboard.py
import json
import os
import pygame

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
    screen.fill((0, 0, 0))  # Clear screen with black

    # Display the top 5 players for the specific game
    for index, entry in enumerate(leaderboard[:5]):
        name_text = font.render(f"{index + 1}. {entry['name']} - {entry['tries']} tries", True, (255, 255, 255))
        screen.blit(name_text, (200, y_offset))
        y_offset += 50

    pygame.display.flip()
    pygame.time.wait(3000)  # Display for 3 seconds
