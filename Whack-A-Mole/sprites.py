import pygame
pygame.init()


# Mole
class Mole(pygame.sprite.Sprite):
    def __init__(self, gameMode, molePos, callback):
        super().__init__()

        self.callback = callback # Calls methods.

        # Grinch
        if gameMode == True:
            
            # Import grinch assets.
            grinch_frame_1 = pygame.image.load("Game_Art/grinch_1.png")
            grinch_frame_2 = pygame.image.load("Game_Art/grinch_2.png")
            grinch_frame_3 = pygame.image.load("Game_Art/grinch_3.png")
            grinch_frame_4 = pygame.image.load("Game_Art/grinch_4.png")

            # Store them into an array for animation.
            grinch_frames = [grinch_frame_1, grinch_frame_2, grinch_frame_3, grinch_frame_4]
            self.frames = grinch_frames


        # Regular mole
        else:
            mole_frame_1 = pygame.image.load("Game_Art/mole_1.png")
            mole_frame_2 = pygame.image.load("Game_Art/mole_2.png")
            mole_frame_3 = pygame.image.load("Game_Art/mole_3.png")
            mole_frame_4 = pygame.image.load("Game_Art/mole_4.png")
            mole_frames = [mole_frame_1, mole_frame_2, mole_frame_3, mole_frame_4]
            self.frames = mole_frames
            # mole_frame_index = 0
            # mole_surf = grinch_frames[mole_frame_index]
            # self.surf = mole_surf

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(topleft=(0,0))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0 # Reset once animation is done. I won't be doing this!
        self.image = self.frames[int(self.animation_index)]


    # def update(self):
    #     self.animation_state()

    def update(self, events):
        # Update animation.
        self.animation_state()
        # Update events.
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.callback() # Calls the method that is init in Mole(XYZ) class.


    def onclick():
        print("MOLE HIT!!! G-RAHHHH!!")
            

    # def collision_sprite(self):
    #     pygame.sprite.spritecollide(moleGroup.sprite)

