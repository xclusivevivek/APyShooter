import pygame
import sys


def hit_aliens(enemy, bullets):
    for bullet in bullets:
        if bullet.alive:
            if enemy.hit(bullet.rect):
                bullet.alive = False


def check_event(ship, enemy, bullets):
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
                ship.fire(bullets)

    # check for collosion
    hit_aliens(enemy, bullets)

    # check for spawning enemy
    if enemy.get_alien_alive_count() == 0:
            enemy.spawn_aliens()


def update_screen(setting, screen, ship, enemy, bullets):
    screen.fill(setting.bg_color)
    ship.draw()
    enemy.draw()
    for bullet in bullets:
        bullet.draw()
    pygame.display.flip()
