# Import pygame library
import pygame
from sys import exit
import random
from WhackAMole.sprites import Mole
# Cursor
from WhackAMole.mallet_cursor import draw_cursor
# Sprites
from WhackAMole.draw_assets import draw_holes



pygame.init()


def main_game():
    clock = pygame.time.Clock()

    # Music
    pygame.mixer.music.load('Game_Sounds/game_xmas_music.mp3')
    pygame.mixer.music.play(-1, 0.0, 1000)



    # Define window size.
    windowWidth = 1024
    windowHeight = 768

    # MANU: Set up font and points counter.
    points = 0
    font = pygame.font.SysFont(None,55)

    # Spawn setup
    spawnDict = {0:(100, 200), 1:(450, 200), 2:(800, 200), 3:(100, 500), 4:(450, 500), 5:(800, 500)}
    #moles_sprites = pygame.sprite.GroupSingle()

    # Mole Setup
    active_mole_position = None
    mole_spawn_time = 0
    mole_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(mole_timer, 2000) # Set timer to every 2 seconds.    

    # Game Timer Setup
    game_active = True # For menu later.
    start_ticks = pygame.time.get_ticks()
    game_time_limit = 10000 # 10

    # Create app window.
    screen = pygame.display.set_mode((windowWidth, windowHeight))

    # Define a christmas mode!
    xmas_mode = True #None
    xmas_bg_surf = pygame.image.load('Game_Art/christmas_bg.png')
    xmas_bg_resized = pygame.transform.smoothscale_by(xmas_bg_surf, (0.8, 0.8))
    xmas_bg_rect = xmas_bg_resized.get_rect(topleft = (0,0))

    while True:
        Game_time= pygame.time.get_ticks()

        for event in pygame.event.get():


            draw_cursor()
        
            # Draw sprites using groups.
            #mole = Mole()
            # moleGroup =
            # moleGroup.add(mole)
            # mole.draw(screen)
            ###

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if active_mole_position and mole_rect.collidepoint(event.pos):

                    if xmas_mode == False:
                        mole_death = pygame.mixer.Sound('Game_Sounds/mole_squeak_sound.WAV')
                        pygame.mixer.Sound.play(mole_death)

                    else:
                        grinch_death = pygame.mixer.Sound('Game_Sounds/mole_squeak_sound.WAV') # Change sound later.                
                
                    points += 1
                    active_mole_position = None

            if event.type == mole_timer and game_active:
                if not active_mole_position:
                    # Select a random spawn location to generate a mole.
                    active_mole_position = random.choice(list(spawnDict.values()))
                    mole_spawn_time = Game_time

            #Manu: this condition removes moles if not clicked after 3 seconds 
            if active_mole_position and (Game_time - mole_spawn_time > 3000):
                    active_mole_position = None


            if xmas_mode == True:
                screen.blit(xmas_bg_resized, xmas_bg_rect)

                draw_holes(spawnDict, screen)

                # Draw the mole at the selected random location.
                if active_mole_position:
                    mole_sprite = pygame.image.load('Game_Art/R (9).png').convert_alpha()
                    # Get rect and resize mole sprite
                    mole_rect = mole_sprite.get_rect(topleft=active_mole_position)
                    mole_sprite = pygame.transform.smoothscale_by(mole_sprite, (0.1, 0.1))
                    mole_rect = mole_sprite.get_rect(topleft=active_mole_position)  # Update rect after resizing. Positioning/placing from top left pixel of image.

                    screen.blit(mole_sprite, mole_rect.topleft)

            else:
                pygame.Surface.fill(screen, (0,255,0))

                draw_holes(spawnDict, screen)

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


            seconds = (game_time_limit - Game_time)/1000
            time_left_surf = font.render(f"Time: {seconds}", True,(0,0,0))
            time_left_rect = time_left_surf.get_rect(topleft = (700,20))
            screen.blit(time_left_surf,time_left_rect)


            # Define end screen.
            #if seconds > game_time_limit:
            if seconds < 0:
                # gameactive set to false to stop mole spawning.
                game_active = False
                pygame.mixer.music.stop()

                # Draw green over screen.
                pygame.Surface.fill(screen, (0,255,0))

                # Display final score.
                font = pygame.font.SysFont(None,80)
                final_score_surf = font.render(f"Times Up! Final Score: {points}", True, (0,0,0))
                final_score_rect = final_score_surf.get_rect(topleft = (150,300))
                screen.blit(final_score_surf, final_score_rect)
                #pygame.time.wait(5000)
            
    

        # Update display screen.
        pygame.display.update()
        clock.tick(60)










