import pygame
pygame.init()


# Mole
class Mole(pygame.sprite.Sprite):
    def __init__(self, gameMode, molePos, callback):
        super().__init__()

        self.callback = callback # Calls methods.
        self.molePos = molePos # Draw sprite at this location.

        # Grinch
        if gameMode == True:
            
            # Import grinch assets.
            grinch_frame_1 = pygame.image.load("Game_Art/grinch_1.png")
            grinch_frame_1 = pygame.transform.smoothscale_by(grinch_frame_1, (0.8, 0.8))
            
            grinch_frame_2 = pygame.image.load("Game_Art/grinch_2.png")
            grinch_frame_2 = pygame.transform.smoothscale_by(grinch_frame_2, (0.8, 0.8))
            
            grinch_frame_3 = pygame.image.load("Game_Art/grinch_3.png")
            grinch_frame_3 = pygame.transform.smoothscale_by(grinch_frame_3, (0.8, 0.8))

            grinch_frame_4 = pygame.image.load("Game_Art/grinch_4.png")
            grinch_frame_4 = pygame.transform.smoothscale_by(grinch_frame_4, (0.8, 0.8))

            # Store them into an array for animation.
            grinch_frames = [grinch_frame_1, grinch_frame_2, grinch_frame_3, grinch_frame_4]
            self.frames = grinch_frames


        # Regular mole
        else:
            mole_frame_1 = pygame.image.load("Game_Art/mole_1.png")
            mole_frame_1 = pygame.transform.smoothscale_by(mole_frame_1, (0.8, 0.8))

            mole_frame_2 = pygame.image.load("Game_Art/mole_2.png")
            mole_frame_2 = pygame.transform.smoothscale_by(mole_frame_2, (0.8, 0.8))

            mole_frame_3 = pygame.image.load("Game_Art/mole_3.png")
            mole_frame_3 = pygame.transform.smoothscale_by(mole_frame_3, (0.8, 0.8))

            mole_frame_4 = pygame.image.load("Game_Art/mole_4.png")
            mole_frame_4 = pygame.transform.smoothscale_by(mole_frame_4, (0.8, 0.8))

            mole_frames = [mole_frame_1, mole_frame_2, mole_frame_3, mole_frame_4]
            self.frames = mole_frames

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(topleft=(molePos)) # USE MOLEPOS HERE!!!

    def animation_state(self):
        self.animation_index += 0.5
        if self.animation_index >= len(self.frames): 
            self.animation_index = 3 # Once mole has popped up, stay in place.
        self.image = self.frames[int(self.animation_index)]

    def update(self, events):
        # Update animation.
        self.animation_state()
        # Update events.
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.callback() # Calls the method that is in Mole instantiation.


    def onclick():
        print("MOLE HIT!!! G-RAHHHH!!")
            

    # def collision_sprite(self):
    #     pygame.sprite.spritecollide(moleGroup.sprite)

