"""
This creates the settings file, and can be imported in the main running file
Note that each large variable has it's own file.
"""

import random
color = [(220, 20, 60), (155, 48, 255), (0, 0, 255), (30, 144, 255), (0, 201, 87), (0, 255, 0), (255, 255, 0),(255, 165, 0), (255, 0, 0), (255,255,255), (145,145,145)]


class Settings():

    def __init__(self):
        """Initialize settings that are static"""
        # Initialize the game's settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Ship Settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = random.choice(color)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed_factor = 3
        self.fleet_drop_speed = 10
        # 1 means right, -1 means left
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.2
        self.initialize_dynamic_settings()

        # How quickly the points value speeds up
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.bullets_allowed = 5

        # Fleet_directions of 1 represents right, -1 represents left'
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase the speed and alien point values"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        # Point value increase
        self.alien_points = int(self.alien_points * self.score_scale)

# End VII
