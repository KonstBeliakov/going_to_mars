from time import perf_counter

import pygame
import sys

import settings
from asteroid import Asteroid
from settings import *
from ship import Ship
from tesla import Tesla
from speed_boost import SpeedBoost

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


def game():
    """
    Simulates a game where you control a spaceship. The goal is to avoid asteroids falling from the top of the screen.
    :return: None
    """

    score = 0
    font = pygame.font.SysFont(None, 25)

    asteroids = [Asteroid() for _ in range(ASTEROID_NUMBER)]
    teslas = [Tesla() for _ in range(TESLA_NUMBER)]
    speed_boosts = [SpeedBoost() for _ in range(SPEED_BOOST_NUMBER)]
    game_over = False
    frame_counter = 0

    ship = Ship()
    distance_to_mars = 257 * 10 ** 6
    t = perf_counter()

    while not game_over:
        distance_to_mars -= ship.speed * (perf_counter() - t)
        t = perf_counter()
        frame_counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                ship.control(event)

        screen.fill(BG_COLOR)

        score_display = font.render('Score: ' + str(score), True, (255, 255, 255))
        screen.blit(score_display, (20, 20))

        distance_display = font.render('Distance to Mars: ' + str(int(distance_to_mars)) + ' km', True,
                                       (255, 255, 255))
        screen.blit(distance_display, (20, 50))

        speed_display = font.render(f'Ship speed: {int(ship.speed)} km/s', True, (255, 255, 255))
        screen.blit(speed_display, (20, 80))

        ship.update()
        ship.draw(screen)

        for speed_boost in speed_boosts:
            speed_boost.update()
            speed_boost.draw(screen)
            if ship.collides_with(speed_boost):
                settings.FALLING_SPEED += 1
                ship.speed *= 1.5
                speed_boost.reset()

        for tesla in teslas:
            tesla.update()
            tesla.draw(screen)
            if ship.collides_with(tesla):
                score += 50
                ship.mask_happiness = 15
                tesla.reset()

        for asteroid in asteroids:
            if frame_counter % 60 == 0:
                asteroid.speedY += 0.5
            asteroid.update()
            asteroid.draw(screen)
            if ship.collides_with(asteroid):
                game_over = True
        pygame.display.flip()
        clock.tick(30)

    print('Game Over')
    print('Your score: ', score)


if __name__ == '__main__':
    game()
