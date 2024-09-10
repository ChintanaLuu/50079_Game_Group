import pygame
import sys



# Initialize Pygame
pygame.init()


# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)


# Set up fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 40)

def ask_number_of_players():
    screen.fill(BLACK)
    text = font.render("Enter number of players:", True, WHITE)
    screen.blit(text, (50, 150))
    pygame.display.flip()
    
    input_active = True
    player_input = ""

    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    player_input = player_input[:-1]
                else:
                    player_input += event.unicode

        screen.fill(BLACK)
        screen.blit(text, (50, 150))
        input_field = font.render(player_input, True, YELLOW)
        screen.blit(input_field, (50, 250))
        pygame.display.flip()

    return int(player_input)

def ask_for_action(player):
    screen.fill(BLACK)
    text = font.render(f"{player}, Enter an action:", True, WHITE)
    screen.blit(text, (50, 150))
    pygame.display.flip()

    input_active = True
    action_input = ""

    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and action_input:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    action_input = action_input[:-1]
                else:
                    action_input += event.unicode

        screen.fill(BLACK)
        screen.blit(text, (50, 150))
        input_surface = font.render(action_input, True, YELLOW)
        screen.blit(input_surface, (50, 250))
        pygame.display.flip()

    return action_input

def display_message(message):
    screen.fill(BLACK)
    text = font.render(message, True, WHITE)
    screen.blit(text, (50, 250))
    pygame.display.flip()
    pygame.time.wait(2000)

def main():
    # Start the game
    num_players = ask_number_of_players()
    players = [f"Player {i+1}" for i in range(num_players)]
    
    round_number = 1
    running = True
    
    while running:
        display_message(f"Round {round_number}!")
        
        # Ask players to write their actions
        round_actions = []
        for player in players:
            action = ask_for_action(player)
            round_actions.append((player, action))
        
        # Ask players to do actions
        for player, action in round_actions:
            display_message(f"{player} : {action}")
            pygame.time.wait(2000)
        
        round_number += 1
        
        # Check if the player want to contine the game
        screen.fill(BLACK)
        text = small_font.render("Press Enter to continue, Esc to quit", True, WHITE)
        screen.blit(text, (50, 300))
        pygame.display.flip()

        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting_for_input = False
                    elif event.key == pygame.K_ESCAPE:
                        running = False
                        waiting_for_input = False

    pygame.quit()

if __name__ == "__main__":


    # Define screen dimensions
    screen_width = 1024
    screen_height = 768
    
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Simon Says Game")

    main()
