# Import pygame library
import pygame
from sys import exit
import random
# import pygame.freetype
pygame.init()


clock = pygame.time.Clock()

# Define window size.
windowWidth = 1024
windowHeight = 768

# Set up font and points counter.
#pygame.font.init()

points = 0

# my_font = pygame.font.SysFont('Game_Fonts/PixelType.ttf', 30)

# def display_score():
#     current_time = pygame.time.get_ticks()
#     score_surf = my_font.render(f"{current_time}", False, (0, 0, 0))
#     score_rect = score_surf.get_rect()
#     screen.blit(score_surf, score_rect)


# font_surf = my_font.render(f"Moles Caught: {points}", True, (0, 0, 0))
# font_rect = font_surf.get_rect()

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
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if active_mole_position and mole_rect.collidepoint(event.pos):
                points += 1

                # Print in VS terminal.
                print(f"Moles Caught: {points}")

                #display_score()

                # Reset mole after spawned for 5 seconds.
                active_mole_position = None

        if event.type == mole_timer and game_active:
            if not active_mole_position:
                # Select a random spawn location to generate a mole.
                active_mole_position = random.choice(list(spawnDict.values()))

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

    # Update display screen.
    pygame.display.update()
    clock.tick(60)




