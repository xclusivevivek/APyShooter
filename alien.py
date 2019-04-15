import pygame


class Alien:

    def __init__(self, screen, settings, spawn_position, speed):
        self.touch_down = False
        self.screen = screen

        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.left = spawn_position
        self.rect.top = self.screen_rect.top
        self.settings = settings
        self.alive = True
        self.center = float(self.rect.centery)
        self.speed = speed

    def draw(self):
        """Render the alien on the screen"""
        if self.alive:
            self.screen.blit(self.image, self.rect)

    def move_down(self):
        self.center = self.center + self.speed
        self.rect.centery = self.center
        if self.rect.bottom >= self.screen_rect.bottom:
            self.alive = False
            self.touch_down = True

    def update(self):
        self.move_down()

    def die(self):
        self.alive = False

    def get_touch_down(self):
        return self.touch_down
