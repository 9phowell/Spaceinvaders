#                       --= Space Invaders =--

"""
This is the main running file for the Space Invaders game. This file, as
seen in the import section, gets all of it's information from other files.
From those files, the code is compiled and ran to form the game.
"""
# Primary Imports
import sys

import pygame
from pygame.sprite import Group

import gf as gf
from Aliens import Alien
from Button import Button
from Gamestats import GameStats
from scoreboard import Scoreboard
from Settings import Settings
from Spaceship import Ship


# run_game function
def run_game():
    # Initialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Space Invaders")

    # Make a play button
    play_button = Button(ai_settings, screen, "Play")

    # creates an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    """
    This part makes a ship, a group of bullets, and a group of aliens
    """
    # Initialize and draw the ship
    ship = Ship(ai_settings, screen)

    # Initialize and draw the alien
    alien = Alien(ai_settings, screen)

    # Make a groups to store bullets and aliens in
    bullets = Group()
    aliens = Group()

    # Create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    """
    This is the main code that is to happen over and over again until the
    game finishes
    """

    def restart():
        # This is to be determined later, for now we will just have it exit the program
        sys.exit()

    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active == True:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()

# End
