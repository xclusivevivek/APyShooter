import pygame
import sys


def hit_aliens(enemy, bullets, ship):
    for bullet in bullets:
        if bullet.alive:
            hit_count = enemy.hit(bullet.rect)
            if hit_count > 0:
                bullet.alive = False
                ship.add_score(hit_count)


def check_touchdown(enemy, ship):
    if enemy.touch_down():
        ship.reduce_live()
        enemy.kill_all()

    if ship.no_lives():
        print("Game over:Score " + str(ship.get_score()))
        sys.exit()


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
    hit_aliens(enemy, bullets, ship)

    # check for aliens touchdown
    check_touchdown(enemy, ship)
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
