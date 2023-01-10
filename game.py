# game.py
import pygame
import random
import sys

from constants import *
from food import Food
from snake import Snake


class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.game_over = False
        # Choose a random initial move direction
        direction = random.randint(1, 4)
        if direction == 1:
            self.move_direction = "left"
        elif direction == 2:
            self.move_direction = "right"
        elif direction == 3:
            self.move_direction = "up"
        else:
            self.move_direction = "down"
        self.last_move_direction = self.move_direction

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.last_move_direction != "right":
                        self.move_direction = "left"
                elif event.key == pygame.K_RIGHT:
                    if self.last_move_direction != "left":
                        self.move_direction = "right"
                elif event.key == pygame.K_UP:
                    if self.last_move_direction != "down":
                        self.move_direction = "up"
                elif event.key == pygame.K_DOWN:
                    if self.last_move_direction != "up":
                        self.move_direction = "down"

    def update(self):
        if self.game_over:
            return

        self.snake.update(self.move_direction, self.food)
        self.food.update(self.snake)
        self.last_move_direction = self.move_direction

        if self.snake.check_collision():
            self.game_over = True

    def draw(self, surface):
        # Draw a red border around the window
        pygame.draw.line(surface, RED, (0, 0), (WINDOW_WIDTH, 0), 20)  # Top
        pygame.draw.line(surface, RED, (0, 0), (0, WINDOW_HEIGHT), 20)  # Left
        pygame.draw.line(surface, RED, (WINDOW_WIDTH, 0),
                         (WINDOW_WIDTH, WINDOW_HEIGHT), 20)  # Right
        pygame.draw.line(surface, RED, (0, WINDOW_HEIGHT),
                         (WINDOW_WIDTH, WINDOW_HEIGHT), 20)  # Bottom

        surface.fill(BLACK)
        self.snake.draw(surface)
        self.food.draw(surface)
