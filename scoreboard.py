import pygame.font

class Scoreboard():
    """A class to report scoring information"""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #font settings for scoring information.
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        # prepare the initial score image
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.test_color, self.ai_settings.bg_color)

        #displays the score at the bottom right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)