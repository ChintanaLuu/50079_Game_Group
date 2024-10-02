import json
import pygame
import sys
from Shooter.GameScreen import game_screen





def load_game_rules():
    try:
        with open("Shooter/GameRules.txt", "r") as file:
            game_rules = file.read().splitlines()
    except FileNotFoundError:
        game_rules = ["Game rules not found!"]
    return game_rules


def draw_game_rules(screen, font, game_rules, game_rules_box_rect):
    line_height = font.get_height() + 5
    y_offset = game_rules_box_rect.y + 50
    for line in game_rules:
        rule_text = font.render(line, True, (255, 255, 255))
        screen.blit(rule_text, (game_rules_box_rect.x + 20, y_offset))
        y_offset += line_height





def main_menu(screen, player_name):

    # Define screen dimensions
    screen_width = 1024
    screen_height = 768

    # Create the game screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space Defender")


    pygame.init()

    # Initialize the mixer for music
    pygame.mixer.init()

    # Load the music and loop it
    pygame.mixer.music.load("Shooter/FreeAssets/Sound/xmas_menu_music.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    # Load the sound for starting the game
    start_game_sound = pygame.mixer.Sound("Shooter/FreeAssets/Sound/StartGameSound.wav")
    start_game_sound.set_volume(0.3)

    #Load the game logo
    game_logo_image = pygame.image.load("Shooter/FreeAssets/Background/gameLogo.PNG")
    logo_width = game_logo_image.get_width() // 2
    logo_height = game_logo_image.get_height() // 2
    game_logo_image = pygame.transform.scale(game_logo_image, (logo_width, logo_height))
    
    game_logo_image_rect = game_logo_image.get_rect()
    game_logo_image_rect.centerx = screen.get_rect().centerx
    game_logo_image_rect.centery = screen.get_rect().centery - 100
    

    # Load button images
    start_game_button_image = pygame.image.load("Shooter/FreeAssets/UI/button/buttonLong_blue.png")
    exit_game_button_image = pygame.image.load("Shooter/FreeAssets/UI/button/buttonLong_blue.png")
    set_difficulty_button_image = pygame.image.load("Shooter/FreeAssets/UI/button/buttonLong_blue.png")
    easy_button_image = set_difficulty_button_image
    normal_button_image = set_difficulty_button_image
    hard_button_image = set_difficulty_button_image
    game_rules_button_image = set_difficulty_button_image





    # Game rules
    game_rules_box_width = screen.get_width() // 3.2
    game_rules_box_height = screen.get_height() // 3
    game_rules_box_x = screen.get_width() // 20
    game_rules_box_y = screen.get_height() // 7
    game_rules_box_rect = pygame.Rect(game_rules_box_x, game_rules_box_y, game_rules_box_width, game_rules_box_height)
    show_game_rules = False
    game_rules_button_pressed = False


    # Get the size of the button images
    start_game_button_rect = start_game_button_image.get_rect()

    exit_game_button_rect = exit_game_button_image.get_rect()
    set_difficulty_button_rect = set_difficulty_button_image.get_rect()
    easy_button_rect = easy_button_image.get_rect()
    normal_button_rect = normal_button_image.get_rect()
    hard_button_rect = hard_button_image.get_rect()
    game_rules_button_rect = game_rules_button_image.get_rect()



    # Adjust the button positions
    start_game_button_rect.x = 50
    start_game_button_rect.y = screen.get_height() - start_game_button_rect.height - 170

    exit_game_button_rect.x = 50
    exit_game_button_rect.y = screen.get_height() - exit_game_button_rect.height - 30

    set_difficulty_button_rect.x = 50
    set_difficulty_button_rect.y = screen.get_height() - set_difficulty_button_rect.height - 100

    easy_button_rect.x = 300
    easy_button_rect.y = start_game_button_rect.y

    normal_button_rect.x = 300
    normal_button_rect.y = set_difficulty_button_rect.y

    hard_button_rect.x = 300
    hard_button_rect.y = exit_game_button_rect.y

    game_rules_button_rect.x = 50
    game_rules_button_rect.y = screen.get_height() - game_rules_button_rect.height - 690

    # Define font for button text
    font = pygame.font.Font(None, 36)
    text_color = (0, 0, 0)
    white = (255,255,255)
    start_game_button_text = font.render("Start Game", True, text_color)
    exit_game_button_text = font.render("Back To Menu", True, text_color)
    set_difficulty_button_text = font.render("Set Difficulty", True, text_color)
    easy_button_text = font.render("Easy Mode", True, text_color)
    normal_button_text = font.render("Normal Mode", True, text_color)
    hard_button_text = font.render("Hard Mode", True, text_color)
    game_rules_button_text = font.render("Read Rules", True, text_color)
    game_rules_text = font.render("Game Rules: ", True, white)
    game_rules_text_rect = game_rules_text.get_rect(center=game_rules_box_rect.center)
    game_rules_text_rect.y -= 100

    # Get the position for the text to be centered on the buttons
    start_game_text_rect = start_game_button_text.get_rect(center=start_game_button_rect.center)
    exit_game_text_rect = exit_game_button_text.get_rect(center=exit_game_button_rect.center)
    set_difficulty_text_rect = set_difficulty_button_text.get_rect(center=set_difficulty_button_rect.center)

    easy_button_text_rect = easy_button_text.get_rect(center=easy_button_rect.center)
    normal_button_text_rect = normal_button_text.get_rect(center=normal_button_rect.center)
    hard_button_text_rect = hard_button_text.get_rect(center=hard_button_rect.center)

    game_rules_button_text_rect = game_rules_button_text.get_rect(center=game_rules_button_rect.center)


    # Difficulty selection status
    show_difficulty_buttons = False

    current_difficulty = "Easy Mode"

    game_rules = load_game_rules()

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if start_game_button_rect.collidepoint(mouse_pos):
                    # Start the game and pass the player name
                    game_screen(screen, current_difficulty, player_name)     

                if not show_difficulty_buttons:
                    if exit_game_button_rect.collidepoint(mouse_pos):
                        pygame.mixer.music.stop()
                        screen.fill((0, 0, 0))
                        pygame.display.flip()
                        from Project import main
                        main(screen, player_name)
                        return
                        
                    elif set_difficulty_button_rect.collidepoint(mouse_pos):
                        show_difficulty_buttons = True


                if show_difficulty_buttons:
                    if easy_button_rect.collidepoint(mouse_pos):
                        current_difficulty = "Easy Mode"
                        show_difficulty_buttons = False
                    elif normal_button_rect.collidepoint(mouse_pos):
                        current_difficulty = "Normal Mode"
                        show_difficulty_buttons = False
                    elif hard_button_rect.collidepoint(mouse_pos):
                        current_difficulty = "Hard Mode"
                        show_difficulty_buttons = False
                
                
                if game_rules_button_rect.collidepoint(mouse_pos):
                    show_game_rules = not show_game_rules
                    game_rules_button_pressed = True
            
            if event.type == pygame.MOUSEBUTTONUP:
                
                if game_rules_button_pressed:
                    game_rules_button_pressed = False




        # Set the background image
        background_imgage = pygame.image.load("Shooter/FreeAssets/Background/background2.jpg")
        screen.blit(background_imgage, (0,0))

        # Draw the game logo
        screen.blit(game_logo_image, game_logo_image_rect)
        
        # Draw the button
        
        if show_game_rules:
            pygame.draw.rect(screen, (45,45,45), game_rules_box_rect)
            screen.blit(game_rules_text, game_rules_text_rect)
            draw_game_rules(screen, font, game_rules, game_rules_box_rect)    



        elif not show_difficulty_buttons:
            # Draw the button images
            screen.blit(start_game_button_image, (start_game_button_rect.x, start_game_button_rect.y))
            screen.blit(exit_game_button_image, (exit_game_button_rect.x, exit_game_button_rect.y))
            screen.blit(set_difficulty_button_image, (set_difficulty_button_rect.x, set_difficulty_button_rect.y))
            #screen.blit(game_rules_button_image,(game_rules_button_rect.x, game_rules_button_rect.y))

            # Draw the text on the buttons
            screen.blit(start_game_button_text, start_game_text_rect)
            screen.blit(exit_game_button_text, exit_game_text_rect)
            screen.blit(set_difficulty_button_text, set_difficulty_text_rect)
            #screen.blit(game_rules_button_text, game_rules_button_text_rect)

            

        
        else:

            # Draw the button images
            screen.blit(start_game_button_image, (start_game_button_rect.x, start_game_button_rect.y))
            screen.blit(exit_game_button_image, (exit_game_button_rect.x, exit_game_button_rect.y))
            screen.blit(set_difficulty_button_image, (set_difficulty_button_rect.x, set_difficulty_button_rect.y))
            #screen.blit(game_rules_button_image,(game_rules_button_rect.x, game_rules_button_rect.y))

            # Draw the text on the buttons
            screen.blit(start_game_button_text, start_game_text_rect)
            screen.blit(exit_game_button_text, exit_game_text_rect)
            screen.blit(set_difficulty_button_text, set_difficulty_text_rect)
            #screen.blit(game_rules_button_text, game_rules_button_text_rect)

            
            
            screen.blit(easy_button_image, (easy_button_rect.x, easy_button_rect.y))
            screen.blit(normal_button_image, (normal_button_rect.x, normal_button_rect.y))
            screen.blit(hard_button_image, (hard_button_rect.x, hard_button_rect.y))

            screen.blit(easy_button_text, easy_button_text_rect)
            screen.blit(normal_button_text, normal_button_text_rect)
            screen.blit(hard_button_text, hard_button_text_rect)

        
        
        diffculty_text = font.render(current_difficulty, True, white)
        screen.blit(diffculty_text, (screen.get_width() - 200, screen.get_height() - 70))



        # Update the display
        pygame.display.flip()




    # Quit pygame
    pygame.quit()
    sys.exit()
