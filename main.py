import pygame
import sys

from asteroid import Asteroid
from settings import *


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

    x = SCREEN_WIDTH // 2
    y = SCREEN_HEIGHT - 60
    asteroids = [Asteroid() for _ in range(ASTEROID_NUMBER)]
    speed = 20
    game_over = False
    frame_counter = 0
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

        # Scoring every frame
        score += 1

        x = max(0, min(x, SCREEN_WIDTH - SHIP_WIDTH))
        screen.fill(BG_COLOR)

        # Score display
        score_display = score_font.render('Score: ' + str(score), True, (255, 255, 255))
        screen.blit(score_display, (20, 20))  # display at top left corner

        pygame.draw.rect(screen, SHIP_COLOR, pygame.Rect(x, y, SHIP_WIDTH, SHIP_HEIGHT))
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
