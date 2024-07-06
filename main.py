import pygame
import sys

from asteroid import Asteroid
from settings import *
from ship import Ship
from tesla import Tesla

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


def game():
    """
    Simulates a game where you control a spaceship. The goal is to avoid asteroids falling from the top of the screen.
    :return: None
    """

    score = 0
    score_font = pygame.font.SysFont(None, 25)

    asteroids = [Asteroid() for _ in range(ASTEROID_NUMBER)]
    teslas = [Tesla() for _ in range(TESLA_NUMBER)]
    game_over = False
    frame_counter = 0

    ship = Ship()

    while not game_over:
        frame_counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                ship.control(event)

        screen.fill(BG_COLOR)

        # Score display
        score_display = score_font.render('Score: ' + str(score), True, (255, 255, 255))
        screen.blit(score_display, (20, 20))

        ship.update()
        ship.draw(screen)

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
