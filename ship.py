import pygame

from bullet import Bullet


class Ship:
    """The Ship to defend all"""

    def __init__(self, screen, settings):
        self.score = 0
        self.screen = screen

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.movingRight = False
        self.movingLeft = False
        self.settings = settings
        self.center = float(self.rect.centerx)
        self.lives = settings.max_lives


    def draw(self):
        """Render the ship on the screen"""
        self.screen.blit(self.image, self.rect)

    def moveLeft(self):
        self.center = float(self.center) - self.settings.ship_speed
        self.rect.centerx = self.center
        if self.rect.left < self.screen_rect.left:
            self.rect.left = self.screen_rect.left

    def moveRight(self):
        self.center = float(self.center) + self.settings.ship_speed
        self.rect.centerx = self.center
        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right

    def update(self):

        if self.movingLeft:
            self.moveLeft()
        elif self.movingRight:
            self.moveRight()

    def fire(self, bullets):
        top_center_x = self.rect.left + int(self.rect.width / 2)
        top_center_y = self.rect.top
        bullets.append(Bullet(self.screen, self.settings, (top_center_x, top_center_y)))

    def reduce_live(self):
        self.lives -= 1

    def get_score(self):
        return self.score

    def add_score(self,hit_count):
        self.score += hit_count

    def no_lives(self):
        return self.lives == 0
