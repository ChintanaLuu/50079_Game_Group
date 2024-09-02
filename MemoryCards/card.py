import pygame

class Card:
    def __init__(self, x, y, width, height, image) -> None:
        self.rect = pygame.Rect(x, y, width, height) # Defines the card position and size
        self.image = image # The display image when the card is flipped
        self.is_flipped = False # Flag to check if the card is flipped
        self.is_matched = False # Flag to check if the cards are matched
        
    """Draw the cards on the screen"""
    def draw(self, surface):
        if self.is_flipped or self.is_matched:
            surface.blit(self.image, self.rect.topleft)
        else:
            pygame.draw.rect(surface, (0, 0, 0), self.rect)