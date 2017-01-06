"""
This creates the settings file, and can be imported in the main running file
Note that each large variable has it's own file.
"""

class Settings():
    def __init__(self):
        # Initialize the game's settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (210, 240, 255)

        # Ship Settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # 1 represents right, -1 represents left
        self.fleet_direction = 1
