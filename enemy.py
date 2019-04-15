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
        alien_copy = self.aliens[:]
        for alien in alien_copy:
            if not alien.alive:
                self.aliens.remove(alien)
        for alien in self.aliens:
            alien.move_down()

    def draw(self):
        for alien in self.aliens:
            alien.draw()

    def get_alien_alive_count(self):
        count = 0
        for alien in self.aliens:
            if alien.alive:
                count = count + 1

        self.alive_alien_count = count
        return count

    def hit(self, bullet_pos):
        hit_count = 0
        for alien in self.aliens:
            if alien.alive:
                if alien.rect.colliderect(bullet_pos):
                    alien.die()
                    hit_count += 1

        return hit_count

    def touch_down(self):
        for alien in self.aliens:
            if alien.get_touch_down():
                return True
        return False

    def kill_all(self):
        for alien in self.aliens:
            alien.alive = False
