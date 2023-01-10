# main.py
import pygame
import sys

from constants import *
from game import Game


def main():
    pygame.init()
    clock = pygame.time.Clock()

    surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake")

    game = Game()

    while True:
        game.handle_events()
        game.update()
        game.draw(surface)
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
