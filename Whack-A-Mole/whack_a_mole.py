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
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
points = 0


# Create app window.
screen = pygame.display.set_mode((windowWidth, windowHeight))

while True:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            #mouse_pos = pygame.mouse.get_pos()
            if mole_rect.collidepoint(event.pos):
                points += 1

                # Print in VS terminal.
                print(f"Moles Caught: {points}")
                
                # Print points on screen.
                # text_surface = my_font.render(f"Caught: {points}", True, (255, 255, 255))
                # screen.blit(text_surface, (50,50))
                # pygame.display.set_caption(f"Points: {points}")



    pygame.Surface.fill(screen, (0,255,0))

    # Grid setup. Should refactor later.

    # Row 1:

    hole_1 = pygame.image.load('Game_Art\Circle.png').convert_alpha()
    hole_1 = pygame.transform.smoothscale_by(hole_1, (0.1,0.1))
    screen.blit(hole_1, (100,200))

    hole_2 = pygame.image.load('Game_Art\Circle.png').convert_alpha()
    hole_2 = pygame.transform.smoothscale_by(hole_2, (0.1,0.1))
    screen.blit(hole_2, (450,200))

    hole_3 = pygame.image.load('Game_Art\Circle.png').convert_alpha()
    hole_3 = pygame.transform.smoothscale_by(hole_3, (0.1,0.1))
    screen.blit(hole_3, (800,200))

    # Row 2:

    hole_4 = pygame.image.load('Game_Art\Circle.png').convert_alpha()
    hole_4 = pygame.transform.smoothscale_by(hole_4, (0.1,0.1))
    screen.blit(hole_4, (100,500))

    hole_5 = pygame.image.load('Game_Art\Circle.png').convert_alpha()
    hole_5 = pygame.transform.smoothscale_by(hole_5, (0.1,0.1))
    screen.blit(hole_5, (450,500))

    hole_6 = pygame.image.load('Game_Art\Circle.png').convert_alpha()
    hole_6 = pygame.transform.smoothscale_by(hole_6, (0.1,0.1))
    screen.blit(hole_6, (800,500))

    # Draw the mole.
    mole_sprite = pygame.image.load('Game_Art\R (9).png').convert_alpha()

   # Make mole clickable. Get rect before resizing.
    mole_rect = mole_sprite.get_rect()
    mole_sprite = pygame.transform.smoothscale_by(mole_sprite, (0.1,0.1))

    # Mole Spawn:

    spawnDict = {0:(100, 200), 1:(450, 200), 2:(800, 200), 3:(100, 500), 4:(450, 500), 5:(800, 500)}
    for spawn in spawnDict:
        screen.blit(mole_sprite, random.choice(spawnDict))
        pygame.time.wait(500) # Mole stays in same place for five seconds.


    # Update display screen.
    pygame.display.update()
    clock.tick(60)



