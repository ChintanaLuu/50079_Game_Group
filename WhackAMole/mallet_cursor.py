import pygame
pygame.init()

# Mouse Cursor
def draw_cursor(gameMode):

    # Regular mode.
        if gameMode == False:
            cursor_surf = pygame.image.load('Game_Art/mallet.png').convert_alpha()
            cursor_surf = pygame.transform.smoothscale_by(cursor_surf, (0.5, 0.5))
            cursor_rect = cursor_surf.get_rect(topleft= (0,0))

            cursor = pygame.cursors.Cursor((50,100), cursor_surf) # Whole image size is (288, 152).
            pygame.mouse.set_cursor(cursor)

    # Christmas Mode
        if gameMode == True:
            cursor_surf = pygame.image.load('Game_Art/candy_cane.png').convert_alpha()
            cursor_surf = pygame.transform.smoothscale_by(cursor_surf, (0.5, 0.5))
            cursor_rect = cursor_surf.get_rect(topleft= (0,0))

            cursor = pygame.cursors.Cursor((50,100), cursor_surf) # Whole image size is (288, 152).
            pygame.mouse.set_cursor(cursor)
