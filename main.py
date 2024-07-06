import pygame
import sys

from asteroid import Asteroid
from settings import *
from tesla import Tesla

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

texture_default = pygame.image.load('mask_default.png').convert_alpha()
texture_default = pygame.transform.scale(texture_default, (SHIP_WIDTH, SHIP_HEIGHT))

texture_happy = pygame.image.load('mask_happy.png').convert_alpha()
texture_happy = pygame.transform.scale(texture_happy, (SHIP_WIDTH, SHIP_HEIGHT))


def draw_ship(is_mask_happy, x, y):
    if is_mask_happy:
        screen.blit(texture_happy, (x, y))
    else:
        screen.blit(texture_default, (x, y))


def game():
    """
    Simulates a game where you control a spaceship. The goal is to avoid asteroids falling from the top of the screen.
    :return: None
    """

    score = 0
    score_font = pygame.font.SysFont(None, 25)

    x = SCREEN_WIDTH // 2
    y = SCREEN_HEIGHT - 60
    asteroids = [Asteroid() for _ in range(ASTEROID_NUMBER)]
    teslas = [Tesla() for _ in range(TESLA_NUMBER)]
    speed = 20
    game_over = False
    frame_counter = 0

    mask_happiness = 0

    while not game_over:
        frame_counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x -= speed
                if event.key == pygame.K_RIGHT:
                    x += speed

        x = max(0, min(x, SCREEN_WIDTH - SHIP_WIDTH))
        screen.fill(BG_COLOR)

        mask_happiness -= 1

        # Score display
        score_display = score_font.render('Score: ' + str(score), True, (255, 255, 255))
        screen.blit(score_display, (20, 20))  # display at top left corner

        draw_ship(mask_happiness > 0, x, y)

        for tesla in teslas:
            tesla.move()
            if tesla.y > SCREEN_HEIGHT:
                tesla.reset()
            tesla.draw(screen)
            if tesla.collides_with(x, y):
                score += 50
                mask_happiness = 15
                tesla.reset()

        for asteroid in asteroids:
            if frame_counter % 60 == 0:
                asteroid.speed += 0.5
            asteroid.move()
            if asteroid.y > SCREEN_HEIGHT:
                asteroid.reset()

            asteroid.draw(screen)
            if asteroid.collides_with(x, y):
                game_over = True
        pygame.display.flip()
        clock.tick(30)

    print('Game Over')
    print('Your score: ', score)


if __name__ == '__main__':
    game()
