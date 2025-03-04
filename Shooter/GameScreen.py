import random
import pygame
import sys
from leaderboard import update_leaderboard


def game_screen(screen, difficulty, player_name):
    
    # Xmas Mode:

    # Initialize the mixer for music
    pygame.mixer.init()
    
    # Load the music and loop it
    pygame.mixer.music.load("Shooter/FreeAssets/Sound/xmas_game_music.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    # Load the button click sound
    button_click_sound = pygame.mixer.Sound("Shooter/FreeAssets/Sound/ButtonClick.wav")
    button_click_sound.set_volume(0.1)

    # Load the get hit sound
    hit_sound = pygame.mixer.Sound("Shooter/FreeAssets/Sound/crashSound.wav")
    hit_sound.set_volume(0.05)

    # Load the game over sound
    game_over_sound = pygame.mixer.Sound("Shooter/FreeAssets/Sound/gameOverSound.wav")
    game_over_sound.set_volume(0.03)

    # Background
    background_imgage = pygame.image.load("Shooter/FreeAssets/Background/christmas_bg.png")
    # Resize background.
    # background_image = pygame.transform.smoothscale(background_image, (screen.get_width(), screen.get_height()))
    background_resized = pygame.transform.smoothscale(background_imgage, (1024, 768))
    background_imgage = background_resized
    background_rect = background_imgage.get_rect(topleft=(0,0))
    background_height = background_imgage.get_height()

    # Player
    player = Player(screen)

    # Enemy
    enemies = []
    enemy_spawn_interval = 1500
    last_enemy_spawn_time = pygame.time.get_ticks()
    enemy_speed = 2

    if difficulty == "Easy Mode":
        enemy_speed = 2
    elif difficulty == "Normal Mode":
        player.health = 3
    elif difficulty == "Hard Mode":
        player.health = 2


    # Score
    score = 0

    # Define color
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Load the pause button images
    pause_button_image = pygame.image.load("Shooter/FreeAssets/UI/button/pause_button.png")
    pause_button_pressed_image = pygame.image.load("Shooter/FreeAssets/UI/button/pause_button_press.png")
    
    # Load the menu button images
    menu_button_image = pygame.image.load("Shooter/FreeAssets/UI/button/menu_button.png")
    menu_button_pressed_image = pygame.image.load("Shooter/FreeAssets/UI/button/menu_button_press.png")
    
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
    restart_button_image = resume_button_image
    restart_button_pressed_image = resume_button_pressed_image

    # Get rects for the buttons
    pause_button_rect = pause_button_image.get_rect()
    resume_button_rect = resume_button_image.get_rect()
    exit_menu_button_rect = resume_button_image.get_rect()
    restart_button_rect = restart_button_image.get_rect()

    # Set the buttons' positions (center of the screen)
    pause_button_rect.x = 25
    pause_button_rect.y = 25
    resume_button_rect.centerx = screen.get_rect().centerx
    exit_menu_button_rect.centerx = screen.get_rect().centerx
    restart_button_rect.centerx = screen.get_rect().centerx
    restart_button_rect.centery = screen.get_rect().centery

    # Position the Resume button a little bit above the Exit button
    resume_button_rect.centery = screen.get_rect().centery - 50
    exit_menu_button_rect.centery = screen.get_rect().centery + 50


    # Show and hide the Resume and Exit buttons
    show_pause_menu = False
    pause_button_pressed = False
    resume_button_pressed = False
    exit_menu_button_pressed = False
    restart_button_pressed = False
    show_restart_button = False

    # Define font for the button text
    font = pygame.font.Font(None, 36)
    
    # Render the text for the buttons
    resume_text = font.render("Resume", True, black)
    exit_text = font.render("Exit", True, black)
    restart_text = font.render("Restart", True, black)

    # Get the rects for the text to center them on the buttons
    resume_text_rect = resume_text.get_rect(center=resume_button_rect.center)
    exit_text_rect = exit_text.get_rect(center=exit_menu_button_rect.center)
    restart_text_rect = restart_text.get_rect(center=restart_button_rect.center)

    scroll_y = 0
    scroll_speed = 0.1
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Only allow player movement when the game is not paused
            if not show_pause_menu and not show_restart_button:
                player.handle_input(event)

            # Detect mouse button down and switch to the pressed images
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Check if the pause button is clicked
                if not show_restart_button and pause_button_rect.collidepoint(mouse_pos):
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

                # Check if the Restart button is clicked
                if show_restart_button and restart_button_rect.collidepoint(mouse_pos):
                    restart_button_pressed = True
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
                    from Shooter.shooter import main_menu
                    main_menu(screen, player_name)

                if restart_button_pressed:
                    restart_button_pressed = False
                    game_screen(screen,difficulty,player_name)

        # Update player position if the game is not paused
        if not show_pause_menu and not show_restart_button:
            player.update_position()
            player.update_bullets()

            # Scroll is for regular space mode.
            # scroll_y += scroll_speed
            # if scroll_y >= background_height:
            #     scroll_y = 0

            # Only spawn enemies when the game is not paused
            current_time = pygame.time.get_ticks()
            if current_time - last_enemy_spawn_time > enemy_spawn_interval:
                enemy_x = random.randint(0, screen.get_width() - 64)

                if difficulty == "Normal Mode":
                    enemy_speed = random.uniform(3, 5)
                    enemy_spawn_interval = random.randint(700, 1300)
                elif difficulty == "Hard Mode":
                    enemy_speed = random.uniform(5, 7)
                    enemy_spawn_interval = random.randint(500, 1200)
            
                enemies.append(Enemy(screen, enemy_x, 110, enemy_speed)) # Spawn monster.ypos at the city.
                last_enemy_spawn_time = current_time


            for enemy in enemies[:]:
                enemy.move(enemy_speed)
                if enemy.is_off_screen():
                    enemies.remove(enemy)
                if enemy.collides_with(player):
                    enemies.remove(enemy)
                    player.lose_health()
                    hit_sound.play()

            for bullet in player.bullets[:]:
                for enemy in enemies[:]:
                    if bullet.collides_with(enemy):
                        player.bullets.remove(bullet)
                        enemies.remove(enemy)
                        if difficulty == "Easy Mode":
                            score += 5
                        elif difficulty == "Normal Mode":
                            score += 10
                        elif difficulty == "Hard Mode":
                            score += 15
                        break


            if player.health <= 0:
                show_restart_button = True
                scroll_speed = 0
                pygame.mixer_music.stop()
                game_over_sound.play()
                update_leaderboard(player_name, score, "space_defender", scoring_type="highest")

        
        # Draw Static background
        screen.blit(background_imgage, background_rect) # Monsters will spawn from the town.

        # Draw Scrolling background
        # screen.blit(background_imgage, (0, scroll_y - background_height))
        # screen.blit(background_imgage, (0, scroll_y))

        for enemy in enemies:
            enemy.draw()

        # Only draw player character if game is not over yet
        if not show_restart_button:
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
        
        # Draw restart button when player health is <= 0
        if show_restart_button:
            if restart_button_pressed:
                screen.blit(restart_button_pressed_image, restart_button_rect)
            else:
                screen.blit(restart_button_image, restart_button_rect)
            
            # Draw restart button text
            screen.blit(restart_text, restart_text_rect)


        
        score_text = font.render(f"Score: {score}", True, black)
        screen.blit(score_text, (40, screen.get_height() - 40))     

        pygame.display.flip()

    pygame.quit()
    sys.exit()




class Player:
    def __init__(self, screen):
        self.image = pygame.image.load("Shooter/FreeAssets/PlayerCharacter/xmas_player_99x75_resize.png")
        self.x = 450
        self.y = 650
        self.x_change = 0
        self.screen = screen
        self.bullets = []
        self.bullet_sound = pygame.mixer.Sound("Shooter/FreeAssets/Sound/shootingSound.wav")
        self.health = 4
        self.health_image = pygame.image.load("Shooter/FreeAssets/UI/health/playerLife_xmas.png")
        self.health_image_spacing = 10
        self.moveSpeed = 8

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.x_change = -self.moveSpeed
            elif event.key == pygame.K_RIGHT:
                self.x_change = self.moveSpeed
            elif event.key == pygame.K_j:
                bullet_x = self.x + (self.image.get_width() // 2) - 10
                bullet_y = self.y
                self.bullets.append(Bullet(self.screen, bullet_x, bullet_y))
                self.bullet_sound.set_volume(0.05)
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
        
        for i in range(self.health):
            health_x = self.screen.get_width() - (i + 1) * (self.health_image.get_width() + self.health_image_spacing)
            health_y = 10
            self.screen.blit(self.health_image, (health_x, health_y))
    
    def lose_health(self):
        self.health -= 1
        if self.health <= 0:
            print("Game Over")

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

            


class Enemy:
    def __init__(self, screen, x, y, speed):
        self.image = pygame.image.load("Shooter/FreeAssets/Enemies/christmas_enemy.png")
        self.x = x
        self.y = y
        self.screen = screen
        self.speed = speed

    def move(self, speed):
        self.y += speed

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def is_off_screen(self):
        return self.y >= self.screen.get_height()
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def collides_with(self, player):
        return self.get_rect().colliderect(player.get_rect())

class Bullet:
    def __init__(self, screen, x, y):
        self.image = pygame.image.load("Shooter/FreeAssets/Bullets/player_xmas_bullet.png")
        bullet_width = self.image.get_width() // 2
        bullet_height = self.image.get_height() // 2
        self.image = pygame.transform.scale(self.image, (bullet_width, bullet_height))
        self.x = x
        self.y = y
        self.screen = screen
        self.speed = -5

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