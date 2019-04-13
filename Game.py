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
    enemy.spawn_aliens()

    while True:
        gameF.check_event(ship)
        ship.update()
        enemy.update()
        gameF.update_screen(settings, screen, ship, enemy)


run_game()
