# Import pygame library
import pygame
from sys import exit
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

    # Grid setup.
    # hole_1 = pygame.image.load('Game_Art\Circle.png').convert_alpha()
    # # hole_2 = pygame.image.load('Game_Art\Circle.png').convert_alpha()
    # # hole_3 = pygame.image.load('Game_Art\Circle.png').convert_alpha()
    # # # hole_4 = pygame.image.load('Game_Art\Circle.png').convert_alpha()
    # # # hole_5 = pygame.image.load('Game_Art\Circle.png').convert_alpha()
    # # # hole_6 = pygame.image.load('Game_Art\Circle.png').convert_alpha()


    # # # Draw grid.
    # # for x in range(3):
    # #     for y in range(3):

    #hole_1 = pygame.transform.smoothscale_by(hole_1, (0.15,0.15))
    #screen.blit(hole_1, (500,500)) # WHY IS THERE A LIBPNG WARNING??
    # screen.blit(hole_2, (500,500))
    # screen.blit(hole_3, (600,500))

    # Draw the mole.
    mole_sprite = pygame.image.load('Game_Art\R (9).png').convert_alpha()

   # Make mole clickable. Get rect before resizing.
    mole_rect = mole_sprite.get_rect()
    mole_sprite = pygame.transform.smoothscale_by(mole_sprite, (0.1,0.1))

 

    screen.blit(mole_sprite, (500,500))
    

    # Update display screen.
    pygame.display.update()
    clock.tick(60)



