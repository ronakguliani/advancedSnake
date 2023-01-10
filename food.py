# food.py
import pygame
import random
from pygame.rect import Rect

from constants import *


class Food:
    def __init__(self):
        self.color = GREEN
        self.rect = Rect(0, 0, FOOD_WIDTH, FOOD_HEIGHT)
        self.spawn()

    def update(self, snake):
        # Check if the snake has eaten the food
        if self.rect.colliderect(snake.rect):
            # Increase the length of the snake
            snake.add_segment()
            # Generate new food
            self.spawn()

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def spawn(self):
        # Place the food somewhere randomly on the screen
        self.rect.x = random.randint(0, WINDOW_WIDTH - FOOD_WIDTH)
        self.rect.y = random.randint(0, WINDOW_HEIGHT - FOOD_HEIGHT)
