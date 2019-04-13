import pygame
import sys


def check_event(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.movingRight = True
            elif event.key == pygame.K_LEFT:
                ship.movingLeft = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.movingRight = False
            elif event.key == pygame.K_LEFT:
                ship.movingLeft = False
            elif event.key == pygame.K_UP:
                ship.fire()


def update_screen(setting, screen, ship, enemy):
    screen.fill(setting.bg_color)
    ship.draw()
    enemy.draw()
    pygame.display.flip()
