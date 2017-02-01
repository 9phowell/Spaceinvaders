
import pygame


class endscreen():

    """
    This class creates a new window with the game over screen printed on it.
    """
    def update(self):
        screen = pygame.display.set_mode(800, 1)
        pygame.display.set_caption("Game Over")
