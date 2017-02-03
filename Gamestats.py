
class GameStats():
    """Track statistics for Alien Invasion."""

    if __name__ == '__main__':
        def __init__(self, ai_settings):
            """Initialize statistics."""
            self.ai_settings = ai_settings
            self.reset_stats()
            # Start alien invasion in an active stats
            self.game_active = True

            # Start game in an inactive state
            self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
