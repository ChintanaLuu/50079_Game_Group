import pygame

class Card:
    def __init__(self, x, y, width, height, image, identifier) -> None:
        self.rect = pygame.Rect(x, y, width, height) # Defines the card position and size
        # Card Front
        self.image = image # The display image when the card is flipped
        self.image = pygame.transform.scale(image, (width, height))  # Resize the image to match the rect
        # Card Back
        #self.backImage = pygame.
        self.is_flipped = False # Flag to check if the card is flipped
        self.is_matched = False # Flag to check if the cards are matched
        self.identifier = identifier

        # Set up card flip animation array.
        #self.frames = [self.image, card_frame_half, card_frame_back]
        
    """Draw the cards on the screen"""
    def draw(self, surface):
        if self.is_flipped or self.is_matched:
            surface.blit(self.image, self.rect.topleft)
            #pygame.time.wait(0.5)
            #surface.blit(self.image, self.rect.topleft)
        else:
            pygame.draw.rect(surface, (0, 0, 0), self.rect)

    """Flip the card to reveal the image"""
    def flip(self):
        if not self.is_flipped and not self.is_matched:
            self.is_flipped = True


