
# Importing
import pygame
from pygame.sprite import Sprite

# Class for Importing in other files
class Alien(Sprite):
    """This class represents a single alien in the fleet"""

    def __init__(self, ai_settings, screen):
        """Innitialise the alien and set it's starting position"""

        # Supering the function for the Sprite
        super(Alien, self).__init__()

        # Loading in the screen and settings
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set it's rect
        self.image = pygame.image.load('img/alien.png')
        self.rect = self.image.get_rect()

        # Store the alien's position
        self.x = float(self.rect.x)

    """ Drawing the alien on the screen """
    def blitme(self):
        """Draw the alien at it's current location"""
        self.screen.blit(self.image, self.rect)


    def check_edges(self):
        """ Return tue if an alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif screen_rect.left <= 0:
            return True


    def update(self):
        """move the alien right"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
