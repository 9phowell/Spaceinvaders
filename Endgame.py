
import pygame

class Endscreen():
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('img/G_O_Screen.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Display the endscreen in the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def bltme(self):
        """Draws the endscreen"""
        self.screen.blit(self.image, self.rect)

        # End VII
