def main_game():
    # Import pygame library
    import pygame
    from sys import exit
    import random
    #from pygame.image import load
    pygame.init()


    clock = pygame.time.Clock()


    # Cursor
    from WhackAMole.mallet_cursor import draw_cursor

    # Sprites
    from WhackAMole.draw_assets import draw_holes
    from WhackAMole.sprites import Mole
    # Mole.onclick

    # Define window size.
    windowWidth = 1024
    windowHeight = 768

    # MANU: Set up font and points counter.
    points = 0
    font = pygame.font.SysFont(None,55)

    # Dynamic Spawn Setup
    # windowWidth = 1920
    # windowHeight = 1080
    # middleSpawnX = windowWidth/2
    # middleSpawnY = windowHeight/2
    # leftSpawnX = middleSpawnX/-2.left


    # spawnDict = {0:(middleSpawnX, middleSpawnY)}

    spawnDict = {0:(100, 100), 1:(450, 100), 2:(800, 100), 3:(100, 250), 4:(450, 250), 5:(800, 250)}

    # Mole Setup
    active_mole_position = None
    mole_spawn_time = 0
    mole_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(mole_timer, 2000) # Set timer to every 2 seconds.    

    # Game Timer Setup
    game_active = True # For menu later.
    start_ticks = pygame.time.get_ticks()
    game_time_limit = 20000 # 20 seconds.

    # Create app window.
    screen = pygame.display.set_mode((windowWidth, windowHeight))

    # Backgrounds Setup
    xmas_mode = True # SHOULD BE TRUE FOR CHRISTMAS MODE!!
    xmas_bg_surf = pygame.image.load('Game_Art/christmas_bg.png')
    xmas_bg_resized = pygame.transform.smoothscale_by(xmas_bg_surf, (0.6, 0.8)) # 0.8 width, 0.8 height
    xmas_bg_rect = xmas_bg_resized.get_rect(topleft=(0,0))


    regular_bg_surf = pygame.image.load('Game_Art/regular_bg.png')
    regular_bg_resized = pygame.transform.smoothscale_by(regular_bg_surf, (0.75, 0.8))
    regular_bg_rect = regular_bg_resized.get_rect(topleft=(-130,0))



    # Music
    if xmas_mode == True:
        pygame.mixer.music.load("Game_Sounds/game_xmas_music.mp3")
        pygame.mixer.music.play(-1, 0.0, 1000)
        # pygame.mixer.music.set_volume(0.1)


    else:
        pygame.mixer.music.load('Game_Sounds/regular_game_music.WAV')
        pygame.mixer.music.play(-1, 0.0, 1000)

    # Groups
    # Draw sprites using groups.    
    moleGroup = pygame.sprite.GroupSingle()
    while True:
        Game_time= pygame.time.get_ticks()


        for event in pygame.event.get():
            draw_cursor(xmas_mode)
            

            # Game loop:

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


            if event.type == pygame.MOUSEBUTTONDOWN:
                # "sprite" is defined in the game_active loop.
                if active_mole_position and sprite.rect.collidepoint(event.pos):

                    if xmas_mode == True:
                        grinch_death = pygame.mixer.Sound('Game_Sounds/grinch_hit_sound.WAV')
                        pygame.mixer.Sound.play(grinch_death)

                    else:
                        mole_death = pygame.mixer.Sound('Game_Sounds/mole_squeak_sound.WAV')
                        pygame.mixer.Sound.play(mole_death)   

                    
                    points += 1
                    active_mole_position = None


            # Select a random spawn location to generate a mole.
            if event.type == mole_timer and game_active:
                if not active_mole_position:
                    active_mole_position = random.choice(list(spawnDict.values()))
                    mole_spawn_time = Game_time
                    # Add a Mole object to GroupSingle after mole is given a new position.
                    sprite = Mole(xmas_mode, active_mole_position, Mole.onclick)
                    moleGroup.add(sprite)

            #Manu: this condition removes moles if not clicked after 3 seconds 
            if active_mole_position and (Game_time - mole_spawn_time > 3000):
                    active_mole_position = None # Allow mole to be spawned again.


            if xmas_mode == True:
                screen.blit(xmas_bg_resized, xmas_bg_rect)
                draw_holes(spawnDict, screen, "Game_Art/xmas_hole.png")

                if active_mole_position:
                    # Draw group onto screen.
                    moleGroup.draw(screen)
                    moleGroup.update(pygame.event.get()) # Updates mole animation and checks if mole has been hit.

            else:

                screen.blit(regular_bg_resized, regular_bg_rect)
                draw_holes(spawnDict, screen, "Game_Art/hole.png")
                
                # Draw the mole at the selected random location.
                if active_mole_position:
                    moleGroup.draw(screen)
                    moleGroup.update(pygame.event.get())



        #Manu: displays the score of moles caught
            score_value = font.render(f"moles captured: {points}", True,(0,0,0))
            score_position = score_value.get_rect(topleft = (20,20))
            screen.blit(score_value,score_position)

            # Display game time left.
            seconds = (game_time_limit - Game_time)/1000
            time_left_surf = font.render(f"Time: {seconds}", True,(0,0,0))
            time_left_rect = time_left_surf.get_rect(topleft = (700,20))
            screen.blit(time_left_surf,time_left_rect)


            # Define end screen.
            if seconds < 0:
                # gameactive set to false to stop mole spawning.
                game_active = False
                pygame.mixer.music.stop()

                # Draw end screen.
                pygame.Surface.fill(screen, (0,130,255))

                # Display final score.
                font = pygame.font.SysFont(None,80)
                final_score_surf = font.render(f"Times Up! Final Score: {points}", True, (0,0,0))
                final_score_rect = final_score_surf.get_rect(topleft = (150,300))
                screen.blit(final_score_surf, final_score_rect)
                #pygame.time.wait(5000)
                
        

        # Update display screen.
        pygame.display.update()
        clock.tick(60)




