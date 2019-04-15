import pygame
import sys


def display_score(screen, font, ship, setting):
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    # Score
    score_text = font.render("Score:" + str(ship.get_score()), True, BLUE, RED)
    score_Rect = score_text.get_rect()
    score_Rect.top = screen.get_rect().top
    score_Rect.left = screen.get_rect().left
    screen.blit(score_text, score_Rect)

    # Lives
    lives_text = font.render("Lives:" + str(ship.get_lives()), True, BLUE, RED)
    lives_rect = lives_text.get_rect()
    lives_rect.top = score_Rect.bottom
    lives_rect.left = screen.get_rect().left
    screen.blit(lives_text, lives_rect)

    if ship.no_lives():
        font_end = pygame.font.Font(setting.score_font, setting.score_size * 5)
        end_text = font_end.render("Game Over \n Score : " + str(ship.get_score()), True, BLUE, RED)
        end_rect = end_text.get_rect()
        end_rect.center = screen.get_rect().center
        screen.blit(end_text, end_rect)
        # Restart Text
        font_restart = pygame.font.Font(setting.score_font, setting.score_size * 2)
        restart_text = font_restart.render("Press R to restart", True, GREEN, RED)
        restart_rect = restart_text.get_rect()
        restart_rect.centerx = screen.get_rect().centerx
        restart_rect.top = end_rect.bottom
        screen.blit(restart_text, restart_rect)


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
        # sys.exit()


def check_event(ship, enemy, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.movingRight = True
            elif event.key == pygame.K_LEFT:
                ship.movingLeft = True
            elif event.key == pygame.K_r:
                if ship.no_lives():
                    return True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.movingRight = False
            elif event.key == pygame.K_LEFT:
                ship.movingLeft = False
            elif event.key == pygame.K_UP:
                ship.fire(bullets)
    if not ship.no_lives():
        # check for collosion
        hit_aliens(enemy, bullets, ship)

        # check for aliens touchdown
        check_touchdown(enemy, ship)
        # check for spawning enemy
        if enemy.get_alien_alive_count() == 0:
            enemy.spawn_aliens()


def update_screen(setting, screen, ship, enemy, bullets, font):
    screen.fill(setting.bg_color)
    if not ship.no_lives():
        ship.draw()
        enemy.draw()
        for bullet in bullets:
            bullet.draw()
    display_score(screen, font, ship, setting)
    pygame.display.flip()
