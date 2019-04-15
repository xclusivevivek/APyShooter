import pygame

import game_functions as gameF
import setting
from enemy import Enemy
from ship import Ship


def run_game():
    settings = setting.Setting()
    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen, settings)
    enemy = Enemy(screen, settings)
    bullets = []
    enemy.spawn_aliens()

    while True:
        gameF.check_event(ship,enemy,bullets)
        ship.update()
        enemy.update()
        for bullet in bullets:
            bullet.update()

        gameF.update_screen(settings, screen, ship, enemy,bullets)
        bullet_copy = bullets[:]
        for bullet in bullet_copy:
            if not bullet.alive:
                bullets.remove(bullet)

run_game()
