import pygame

import game_functions as gameF
import setting
from enemy import Enemy
from ship import Ship


def reset_game(screen, settings):
    ship = Ship(screen, settings)
    enemy = Enemy(screen, settings)
    bullets = []
    enemy.spawn_aliens()
    return (ship, enemy, bullets)


def run_game():
    settings = setting.Setting()
    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    font = pygame.font.Font(settings.score_font, settings.score_size)

    ship = Ship(screen, settings)
    enemy = Enemy(screen, settings)
    bullets = []
    enemy.spawn_aliens()

    while True:
        restart = gameF.check_event(ship, enemy, bullets)
        if restart:
            (ship, enemy, bullets) = reset_game( screen, settings)
        if not ship.no_lives():
            ship.update()
            enemy.update()
            for bullet in bullets:
                bullet.update()

        gameF.update_screen(settings, screen, ship, enemy, bullets, font)
        bullet_copy = bullets[:]
        for bullet in bullet_copy:
            if not bullet.alive:
                bullets.remove(bullet)


run_game()
