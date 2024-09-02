# Import pygame library
import pygame
from sys import exit
import random
#from pygame.image import load
pygame.init()


clock = pygame.time.Clock()

# Music
pygame.mixer.music.load('Game_Sounds/whack_a_mole_music.WAV')
pygame.mixer.music.play(-1, 0.0, 1000)


# Define window size.
windowWidth = 1024
windowHeight = 768

# MANU: Set up font and points counter.
#pygame.font.init()

points = 0
font = pygame.font.SysFont(None,55)

# Spawn setup
spawnDict = {0:(100, 200), 1:(450, 200), 2:(800, 200), 3:(100, 500), 4:(450, 500), 5:(800, 500)}
#moles_sprites = pygame.sprite.Group()

active_mole_position = None
mole_spawn_time = 0

# Timer
mole_timer = pygame.USEREVENT + 1
pygame.time.set_timer(mole_timer, 5000) # Set timer to every 5 seconds.    
game_active = True # For menu later.

# Create app window.
screen = pygame.display.set_mode((windowWidth, windowHeight))

while True:
    Game_time= pygame.time.get_ticks()


    for event in pygame.event.get():

        # Mouse Cursor
        cursor_surf = pygame.image.load('Game_Art/mallet.png').convert_alpha()
        cursor_surf = pygame.transform.smoothscale_by(cursor_surf, (0.5, 0.5))
        cursor_rect = cursor_surf.get_rect(topleft= (0,0))

        cursor = pygame.cursors.Cursor((50,100), cursor_surf) # Whole image size is (288, 152).
        pygame.mouse.set_cursor(cursor)
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if active_mole_position and mole_rect.collidepoint(event.pos):

                mole_death = pygame.mixer.Sound('Game_Sounds/mole_squeak_sound.WAV')
                pygame.mixer.Sound.play(mole_death)
                
                points += 1

                # Reset mole after spawned for 5 seconds.
                active_mole_position = None

        if event.type == mole_timer and game_active:
            if not active_mole_position:
                # Select a random spawn location to generate a mole.
                active_mole_position = random.choice(list(spawnDict.values()))
                mole_spawn_time = Game_time
    #Manu: this condition removes moles if not clicked after 3 seconds 
    if active_mole_position and (Game_time - mole_spawn_time > 3000):
            active_mole_position = None

    screen.fill((0, 255, 0))


    pygame.Surface.fill(screen, (0,255,0))

    # def draw_holes():
    hole_sprite = pygame.image.load('Game_Art/Circle.png').convert_alpha()
    hole_sprite = pygame.transform.smoothscale_by(hole_sprite, (0.1,0.1))
    for position in spawnDict.values():
        screen.blit(hole_sprite, position)

    # Draw the mole at the selected random location.
    if active_mole_position:
        mole_sprite = pygame.image.load('Game_Art/R (9).png').convert_alpha()
        
        # Get rect and resize mole sprite
        mole_rect = mole_sprite.get_rect(topleft=active_mole_position)
        mole_sprite = pygame.transform.smoothscale_by(mole_sprite, (0.1, 0.1))
        mole_rect = mole_sprite.get_rect(topleft=active_mole_position)  # Update rect after resizing. Positioning/placing from top left pixel of image.

        screen.blit(mole_sprite, mole_rect.topleft)
#Manu: displays the score of moles caught
    score_value = font.render(f"moles captured: {points}", True,(0,0,0))
    score_position = score_value.get_rect(topleft = (20,20))
    screen.blit(score_value,score_position)

    # Update display screen.
    pygame.display.update()
    clock.tick(60)




