import random
import pygame
import sys


def game_screen(screen):
    
    # Background
    background_imgage = pygame.image.load("FreeAssets/Background/background2.jpg")
    background_height = background_imgage.get_height()

    # Player
    player_image = pygame.image.load("FreeAssets/PlayerCharacter/playerShip1_blue.png")
    player_x = 450
    player_y = 650
    player_x_change = 0

    # Enemy
    enemy_image = pygame.image.load("FreeAssets/Enemies/enemyBlack1.png")
    enemy_width, enemy_height = enemy_image.get_size()

    # Spawn enemy every 1.5s
    enemies = []
    enemy_spawn_interval = 1500
    last_enemy_spawn_time = pygame.time.get_ticks()

    def player():
        screen.blit(player_image, (player_x, player_y))

    # Spawn enemy at random x coordinate position
    def spawn_enemy():
        enemy_x = random.randint(0, screen.get_width() - enemy_width)
        enemy_y = -enemy_height
        enemies.append([enemy_x, enemy_y])


    # Define color
    white = (255, 255, 255)

    # Load the pause button image
    pause_button_image = pygame.image.load("FreeAssets/UI/button/pause_button.png")


    # Load the menu button image
    menu_button_image = pygame.image.load("FreeAssets/UI/button/menu_button.png")


    # Resize the pause button since the asset is too small
    scale = 3
    pause_button_width = pause_button_image.get_width() * scale
    pause_button_height = pause_button_image.get_height() * scale
    pause_button_image = pygame.transform.scale(pause_button_image, (pause_button_width, pause_button_height))

    # Get the size of the resized button image
    pause_button_rect = pause_button_image.get_rect()

    # Adjust the pause button position
    pause_button_rect.x = 25
    pause_button_rect.y = 25

    # Prepare the Resume and Exit to Main Menu buttons (but don't display them yet)
    resume_button_image = menu_button_image
    exit_menu_button_image = menu_button_image

    # Resize the pause and exit button since the asset is too small
    scale = 2
    resume_button_width = resume_button_image.get_width() * scale
    resume_button_height = resume_button_image.get_height() * scale
    resume_button_image = pygame.transform.scale(resume_button_image, (resume_button_width, resume_button_height))

    exit_button_width = exit_menu_button_image.get_width() * scale
    exit_button_height = exit_menu_button_image.get_height() * scale
    exit_menu_button_image = pygame.transform.scale(exit_menu_button_image, (exit_button_width, exit_button_height))

    # Get rects for the Resume and Exit buttons
    resume_button_rect = resume_button_image.get_rect()
    exit_menu_button_rect = exit_menu_button_image.get_rect()

    # Set the buttons' positions (center of the screen)
    resume_button_rect.centerx = screen.get_rect().centerx
    exit_menu_button_rect.centerx = screen.get_rect().centerx

    # Position the Resume button a little bit above the Exit button
    resume_button_rect.centery = screen.get_rect().centery - 50
    exit_menu_button_rect.centery = screen.get_rect().centery + 50

    # Show and hide the Resume and Exit buttons
    show_pause_menu = False

    # Define font for the button text
    font = pygame.font.Font(None, 36)

    # Render the text for the buttons
    resume_text = font.render("Resume", True, white)
    exit_text = font.render("Exit", True, white)

    # Get the rects for the text to center them on the buttons
    resume_text_rect = resume_text.get_rect(center=resume_button_rect.center)
    exit_text_rect = exit_text.get_rect(center=exit_menu_button_rect.center)


    scroll_y = 0
    scroll_speed = 0.1
    enemy_speed = 0.2


    # Main game loop for the game screen
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Player character can only move when pause menu is not shown
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and show_pause_menu == False:
                    player_x_change = -0.5
                if event.key == pygame.K_RIGHT and show_pause_menu == False:
                    player_x_change = 0.5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_x_change = 0

            
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                # Check if the pause button is clicked
                if pause_button_rect.collidepoint(mouse_pos):
                    show_pause_menu = True
                    scroll_speed = 0

                # Check if the Resume button is clicked
                if show_pause_menu and resume_button_rect.collidepoint(mouse_pos):
                    show_pause_menu = False  # Hide the pause menu (resume the game)
                    scroll_speed = 0.1

                # Check if the Exit to Main Menu button is clicked
                if show_pause_menu and exit_menu_button_rect.collidepoint(mouse_pos):
                    from shooter import main_menu
                    main_menu(screen)
        



        # Update player postion
        player_x += player_x_change
        if player_x <= 0:
            player_x = 0
        elif player_x >= 925:
            player_x = 925

        
        # Scroll the background
        scroll_y += scroll_speed
        if scroll_y >= background_height:
            scroll_y = 0 

        # Draw the scrolling background
        screen.blit(background_imgage, (0, scroll_y - background_height))
        screen.blit(background_imgage, (0, scroll_y))



        # Only spawn enemies when the game is not paused
        if not show_pause_menu:
            current_time = pygame.time.get_ticks()
            if current_time - last_enemy_spawn_time > enemy_spawn_interval:
                spawn_enemy()
                last_enemy_spawn_time = current_time

            # Move enemies
            for enemy in enemies:
                enemy[1] += enemy_speed

        # Draw all enemies
        for enemy in enemies:
            screen.blit(enemy_image, enemy)

        # Remove enemies moves out of the screen
        for enemy in enemies[:]:
            if enemy[1] >= screen.get_height():
                enemies.remove(enemy)




        # Draw the player
        player()

        # Draw the pause button image
        screen.blit(pause_button_image, (pause_button_rect.x, pause_button_rect.y))

        # If the pause menu is active, draw the Resume and Exit to Main Menu buttons
        if show_pause_menu:
            screen.blit(resume_button_image, resume_button_rect)
            screen.blit(exit_menu_button_image, exit_menu_button_rect)

            # Draw the text on the buttons
            screen.blit(resume_text, resume_text_rect)
            screen.blit(exit_text, exit_text_rect)


        # Update the display
        pygame.display.flip()
    
    # Exit the game screen
    pygame.quit()
    sys.exit()
