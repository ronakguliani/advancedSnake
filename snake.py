# snake.py
import pygame
from pygame.rect import Rect

from constants import *


class Snake:
    def __init__(self):
        self.color = WHITE
        self.segments = [Rect(0, 0, SNAKE_WIDTH, SNAKE_HEIGHT)]
        self.add_segment()
        self.add_segment()

        # Set the initial position and direction of the snake
        self.segments[0].x = WINDOW_WIDTH // 2 - SNAKE_WIDTH // 2
        self.segments[0].y = WINDOW_HEIGHT // 2 - SNAKE_HEIGHT // 2
        self.move_direction = "right"
        self.prev_move_direction = "right"
        self.rect = self.segments[0]

    def add_segment(self):
        last_segment = self.segments[-1]
        new_segment = Rect(last_segment.x, last_segment.y,
                           SNAKE_WIDTH, SNAKE_HEIGHT)
        self.segments.append(new_segment)

    def update(self, move_direction, food):
        self.prev_move_direction = self.move_direction
        self.move_direction = move_direction

        if self.move_direction == "left":
            self.segments[0].x -= SNAKE_SPEED
        elif self.move_direction == "right":
            self.segments[0].x += SNAKE_SPEED
        elif self.move_direction == "up":
            self.segments[0].y -= SNAKE_SPEED
        elif self.move_direction == "down":
            self.segments[0].y += SNAKE_SPEED

        self.rect = self.segments[0]

        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i] = self.segments[i - 1].copy()

    def check_collision(self):
        # Check if the snake has collided with a wall
        if (
            self.segments[0].x < 0
            or self.segments[0].x > WINDOW_WIDTH - SNAKE_WIDTH
            or self.segments[0].y < 0
            or self.segments[0].y > WINDOW_HEIGHT - SNAKE_HEIGHT
        ):
            return True

        # Check if the snake has collided with itself
        # for i in range(1, len(self.segments)):
        #     if self.segments[0].colliderect(self.segments[i]):
        #         return True

        # return False

    def draw(self, surface):
        for segment in self.segments:
            pygame.draw.rect(surface, self.color, segment)
