from pygame import draw
from pygame.rect import Rect


class Bullet:

    def __init__(self, screen, settings, shot_from):

        self.settings = settings
        self.screen = screen
        self.height = 10
        self.width = 5
        self.rect = self.get_bullet_rect(shot_from)
        self.alive = True
        self.position = float(self.rect.centery)

    def draw(self):
        if self.alive:
            draw.ellipse(self.screen, (255, 0, 0), self.rect, 0)

    def move_up(self):
        self.position = self.position - self.settings.bullet_speed
        self.rect.centery = self.position
        if self.rect.top < self.get_screen_rect().top:
            self.alive = False

    def update(self):
        self.move_up()

    def die(self):
        self.alive = False

    def get_bullet_rect(self, shot_from):
        return Rect(shot_from[0] - self.width / 2, shot_from[1] - self.height, self.width, self.height)

    def get_screen_rect(self):
        return self.screen.get_rect()
