import random
import pygame
import sys


def game_screen(screen):

    # Initialize the mixer for music
    pygame.mixer.init()
    
    # Load the music and loop it
    pygame.mixer.music.load("FreeAssets/Sound/InGameMusic.wav")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    # Load the button click sound
    button_click_sound = pygame.mixer.Sound("FreeAssets/Sound/ButtonClick.wav")
    button_click_sound.set_volume(0.1)

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

    # Score
    score = 0

    # Define color
    white = (255, 255, 255)

    # Load the pause button images
    pause_button_image = pygame.image.load("FreeAssets/UI/button/pause_button.png")
    pause_button_pressed_image = pygame.image.load("FreeAssets/UI/button/pause_button_press.png")
    
    # Load the menu button images
    menu_button_image = pygame.image.load("FreeAssets/UI/button/menu_button.png")
    menu_button_pressed_image = pygame.image.load("FreeAssets/UI/button/menu_button_press.png")
    
    # Resize the pause button since the asset is too small
    scale = 3
    pause_button_width = pause_button_image.get_width() * scale
    pause_button_height = pause_button_image.get_height() * scale
    pause_button_image = pygame.transform.scale(pause_button_image, (pause_button_width, pause_button_height))
    pause_button_pressed_image = pygame.transform.scale(pause_button_pressed_image, (pause_button_width, pause_button_height))
    
    # Resize the menu buttons
    menu_button_width = menu_button_image.get_width() * 2
    menu_button_height = menu_button_image.get_height() * 2
    resume_button_image = pygame.transform.scale(menu_button_image, (menu_button_width, menu_button_height))
    resume_button_pressed_image = pygame.transform.scale(menu_button_pressed_image, (menu_button_width, menu_button_height))
    exit_menu_button_image = resume_button_image
    exit_menu_button_pressed_image = resume_button_pressed_image

    # Get rects for the buttons
    pause_button_rect = pause_button_image.get_rect()
    resume_button_rect = resume_button_image.get_rect()
    exit_menu_button_rect = resume_button_image.get_rect()

    # Set the buttons' positions (center of the screen)
    pause_button_rect.x = 25
    pause_button_rect.y = 25
    resume_button_rect.centerx = screen.get_rect().centerx
    exit_menu_button_rect.centerx = screen.get_rect().centerx

    # Position the Resume button a little bit above the Exit button
    resume_button_rect.centery = screen.get_rect().centery - 50
    exit_menu_button_rect.centery = screen.get_rect().centery + 50

    # Show and hide the Resume and Exit buttons
    show_pause_menu = False
    pause_button_pressed = False
    resume_button_pressed = False
    exit_menu_button_pressed = False

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
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Only allow player movement when the game is not paused
            if not show_pause_menu:
                player.handle_input(event)

            # Detect mouse button down and switch to the pressed images
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Check if the pause button is clicked
                if pause_button_rect.collidepoint(mouse_pos):
                    pause_button_pressed = True
                    pygame.mixer.music.pause()
                    button_click_sound.play()

                # Check if the Resume button is clicked
                if show_pause_menu and resume_button_rect.collidepoint(mouse_pos):
                    resume_button_pressed = True
                    button_click_sound.play()
                    pygame.mixer.music.unpause()
                    

                # Check if the Exit button is clicked
                if show_pause_menu and exit_menu_button_rect.collidepoint(mouse_pos):
                    exit_menu_button_pressed = True
                    button_click_sound.play()

            # Detect mouse button up and switch back to the normal images
            if event.type == pygame.MOUSEBUTTONUP:
                if pause_button_pressed:
                    pause_button_pressed = False
                    show_pause_menu = True
                    scroll_speed = 0

                if resume_button_pressed:
                    resume_button_pressed = False
                    show_pause_menu = False
                    scroll_speed = 0.1

                if exit_menu_button_pressed:
                    exit_menu_button_pressed = False
                    from shooter import main_menu
                    main_menu(screen)

        # Update player position if the game is not paused
        if not show_pause_menu:
            player.update_position()
            player.update_bullets()

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

            for bullet in player.bullets[:]:
                for enemy in enemies[:]:
                    if bullet.collides_with(enemy):
                        player.bullets.remove(bullet)
                        enemies.remove(enemy)
                        score += 5
                        break

        # Draw Scrolling background
        screen.blit(background_imgage, (0, scroll_y - background_height))
        screen.blit(background_imgage, (0, scroll_y))

        for enemy in enemies:
            enemy.draw()

        # Draw player to the screen
        player.draw()

        # Draw pause button based on the pressed state
        if pause_button_pressed:
            screen.blit(pause_button_pressed_image, pause_button_rect)
        else:
            screen.blit(pause_button_image, pause_button_rect)

        if show_pause_menu:
            # Draw resume button based on the pressed state
            if resume_button_pressed:
                screen.blit(resume_button_pressed_image, resume_button_rect)
            else:
                screen.blit(resume_button_image, resume_button_rect)
            
            # Draw exit menu button based on the pressed state
            if exit_menu_button_pressed:
                screen.blit(exit_menu_button_pressed_image, exit_menu_button_rect)
            else:
                screen.blit(exit_menu_button_image, exit_menu_button_rect)

            # Draw text on the buttons
            screen.blit(resume_text, resume_text_rect)
            screen.blit(exit_text, exit_text_rect)
        
        score_text = font.render(f"Score: {score}", True, white)
        screen.blit(score_text, (40, screen.get_height() - 40))     

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
        self.bullets = []
        self.bullet_sound = pygame.mixer.Sound("FreeAssets/Sound/shootingSound.wav")

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.x_change = -0.5
            elif event.key == pygame.K_RIGHT:
                self.x_change = 0.5
            elif event.key == pygame.K_j:
                bullet_x = self.x + (self.image.get_width() // 2) - 10
                bullet_y = self.y
                self.bullets.append(Bullet(self.screen, bullet_x, bullet_y))
                self.bullet_sound.set_volume(0.2)
                self.bullet_sound.play()


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.x_change = 0

    def update_position(self):
        self.x += self.x_change
        if self.x <= 0:
            self.x = 0
        elif self.x >= 925:
            self.x = 925


    def update_bullets(self):
        for bullet in self.bullets[:]:
            bullet.move()
            if bullet.is_off_screen():
                self.bullets.remove(bullet)

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullets:
            bullet.draw()
            


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
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())


class Bullet:
    def __init__(self, screen, x, y):
        self.image = pygame.image.load("FreeAssets/Bullets/4.png")
        bullet_width = self.image.get_width() // 2
        bullet_height = self.image.get_height() // 2
        self.image = pygame.transform.scale(self.image, (bullet_width, bullet_height))
        self.x = x
        self.y = y
        self.screen = screen
        self.speed = -0.5

    def move(self):
        self.y += self.speed

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))


    def is_off_screen(self):
        return self.y < -self.image.get_height()    
    
    def collides_with(self, enemy):
        return self.get_rect().colliderect(enemy.get_rect())

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())