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
        return random.randrange(0, self.settings.screen_width, 100)

    def update(self):
        for alien in self.aliens:
            alien.move_down()

        alien_copy = self.aliens[:]
        for alien in alien_copy:
            if not alien.alive :
                self.aliens.remove(alien)

    def draw(self):
        for alien in self.aliens:
            alien.draw()

    def get_alien_alive_count(self):
        count = 0
        for alien in self.aliens:
            if alien.alive:
                count=count + 1

        self.alive_alien_count = count
        return count

    def hit(self, bullet_pos):
        is_hit=False
        for alien in self.aliens:
            if alien.alive:
                if alien.rect.colliderect(bullet_pos):
                    alien.die()
                    is_hit = True
                    return is_hit
        return is_hit
