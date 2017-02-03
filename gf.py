
# Primary Imports
import sys
from time import sleep

import pygame

from Aliens import Alien
from bullet import Bullet

""" PART I - EVENTS AND SCREEN"""
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """respond to the ship being hit by an alien."""
    if stats.ships_left > 0:
        # decrement ships left.
        stats.ships_left -= 1

        # empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)

        # pause
        sleep(.5)

    else:
        stats.game_active = False

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to key presses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True

    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ai_settings, screen, ship, bullets):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

    # Quitting the program
    elif event.key == pygame.K_q:
        sys.exit()


def check_events(ai_settings, screen, ship, aliens, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_settings, screen, ship, bullets)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Draw the objects
    ship.blitme()
    aliens.draw(screen)

    # Make the most recently drawn screen visible.
    pygame.display.flip()


""" PART II - BULLETS """


def fire_bullets(ai_settings, screen, ship, bullets):
    """Fire a bullet if the limit is not reached yet"""
    if len(bullets) < ai_settings.bullets_allowed:
        # Create a new bullet and add it to the bullets group.
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Update the position of the bullets and get rd of old bullets"""

    # Update the position
    bullets.update()

    # Delete old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    # Check for any bullets that have hit aliens
    # If so, get rid of the bullet and the alien
    if pygame.sprite.spritecollideany(bullets, aliens):
        collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
        points = points + 1000
    if len(aliens) == 0:
        # Destroy existing bullets and create a new fleet
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

""" PART III - ALIENS """


def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien, and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    # Create an alien, and find number of aliens in a row.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)

    # Create the fleet of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                         row_number)

    ship.center_ship_x()
    ship.center_ship_y()


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Drop the fleet and change it's direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for aliens in aliens.sprites():
        if aliens.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship.hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """Check if the fleet is at an edge, then
    update the position of all aliens in the fleet"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    # Look for any aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)