import pygame

from bullet import Bullet


class Ship:
    """The Ship to defend all"""

    def __init__(self, screen, settings):
        self.screen = screen

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.movingRight = False
        self.movingLeft = False
        self.settings = settings
        self.bullets = []

    def draw(self):
        """Render the ship on the screen"""
        self.screen.blit(self.image, self.rect)
        for bullet in self.bullets:
            bullet.draw()

    def moveLeft(self):

        self.rect.centerx = self.rect.centerx - self.settings.ship_speed
        if self.rect.left < self.screen_rect.left:
            self.rect.left = self.screen_rect.left

    def moveRight(self):
        self.rect.centerx = self.rect.centerx + self.settings.ship_speed
        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right

    def update(self):

        if self.movingLeft:
            self.moveLeft()
        elif self.movingRight:
            self.moveRight()

        for bullet in self.bullets:
            bullet.update()

    def fire(self):
        top_center_x = self.rect.left + int(self.rect.width / 2)
        top_center_y = self.rect.top
        self.bullets.append(Bullet(self.screen, self.settings, (top_center_x, top_center_y)))
