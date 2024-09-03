import random
import pygame
import sys


def game_screen(screen):

    # Background
    background_imgage = pygame.image.load("FreeAssets/Background/background2.jpg")
    background_height = background_imgage.get_height()

    # Player
    player = Player(screen)

    # Enemy
    enemies = []
    enemy_spawn_interval = 1500
    last_enemy_spawn_time = pygame.time.get_ticks()
    enemy_speed = 0.2

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
    resume_button_image = pygame.transform.scale(menu_button_image, (menu_button_image.get_width() * 2, menu_button_image.get_height() * 2))
    exit_menu_button_image = pygame.transform.scale(menu_button_image, (menu_button_image.get_width() * 2, menu_button_image.get_height() * 2))
    
    
    
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
    show_pause_menu = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Only allow player movement when the game is not paused
            if not show_pause_menu:
                player.handle_input(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Check if the pause button is clicked
                if pause_button_rect.collidepoint(mouse_pos):
                    show_pause_menu = True
                    scroll_speed = 0
                # Check if the Resume button is clicked    
                if show_pause_menu and resume_button_rect.collidepoint(mouse_pos):
                    show_pause_menu = False
                    scroll_speed = 0.1
                # Check if the Exit to Main Menu button is clicked
                if show_pause_menu and exit_menu_button_rect.collidepoint(mouse_pos):
                    from shooter import main_menu
                    main_menu(screen)
        
        # Update player position if the game is not paused
        if not show_pause_menu:
            player.update_position()

            scroll_y += scroll_speed
            if scroll_y >= background_height:
                scroll_y = 0

            # Only spawn enemies when the game is not paused
            current_time = pygame.time.get_ticks()
            if current_time - last_enemy_spawn_time > enemy_spawn_interval:
                enemy_x = random.randint(0, screen.get_width() - 64)
                enemies.append(Enemy(screen, enemy_x, -64))
                last_enemy_spawn_time = current_time

            for enemy in enemies[:]:
                enemy.move(enemy_speed)
                if enemy.is_off_screen():
                    enemies.remove(enemy)

        # Draw Scrolling background
        screen.blit(background_imgage, (0, scroll_y - background_height))
        screen.blit(background_imgage, (0, scroll_y))

        for enemy in enemies:
            enemy.draw()

        # Draw player to the screen
        player.draw()
        
        # Draw buttons to the screen
        screen.blit(pause_button_image, pause_button_rect)
        if show_pause_menu:
            screen.blit(resume_button_image, resume_button_rect)
            screen.blit(exit_menu_button_image, exit_menu_button_rect)
            screen.blit(resume_text, resume_text_rect)
            screen.blit(exit_text, exit_text_rect)

        pygame.display.flip()

    pygame.quit()
    sys.exit()



class Player:
    def __init__(self, screen):
        self.image = pygame.image.load("FreeAssets/PlayerCharacter/playerShip1_blue.png")
        self.x = 450
        self.y = 650
        self.x_change = 0
        self.screen = screen

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.x_change = -0.5
            elif event.key == pygame.K_RIGHT:
                self.x_change = 0.5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.x_change = 0

    def update_position(self):
        self.x += self.x_change
        if self.x <= 0:
            self.x = 0
        elif self.x >= 925:
            self.x = 925

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))



class Enemy:
    def __init__(self, screen, x, y):
        self.image = pygame.image.load("FreeAssets/Enemies/enemyBlack1.png")
        self.x = x
        self.y = y
        self.screen = screen

    def move(self, speed):
        self.y += speed

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def is_off_screen(self):
        return self.y >= self.screen.get_height()
