import random

from alien import Alien


class Enemy:

    # TODO add a level later
    def __init__(self, screen, settings):
        self.aliens = []
        self.settings = settings
        self.screen = screen
        self.alive_alien_count = 0;

    def spawn_aliens(self):
        alien_count = random.randrange(3, 6, 1)
        self.alive_alien_count += alien_count

        for alien_index in range(1, alien_count):
            self.aliens.append(Alien(self.screen, self.settings, self.get_alien_position()))

    def get_alien_position(self):
        return random.randrange(0, self.settings.screen_width, 1)

    def update(self):
        for alien in self.aliens:
            alien.move_down()

    def draw(self):
        for alien in self.aliens:
            alien.draw()
