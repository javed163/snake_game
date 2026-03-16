import pygame
import random
import numpy as np
from collections import deque
from enum import Enum

# Constants
BLOCK_SIZE = 20
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        self.snake = [Point(100, 50), Point(90, 50), Point(80, 50)]
        self.direction = Direction.RIGHT
        self.food = self.place_food()
        self.score = 0
        self.done = False

    def place_food(self):
        x = random.randint(0, (WINDOW_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (WINDOW_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        return Point(x, y)

    def is_collision(self, point):
        if point.x < 0 or point.x >= WINDOW_WIDTH or point.y < 0 or point.y >= WINDOW_HEIGHT:
            return True
        for segment in self.snake[1:]:
            if segment.x == point.x and segment.y == point.y:
                return True
        return False

    def play_step(self, action):
        self.handle_input(action)
        self.move()
        self.snake.insert(0, self.snake[0])
        
        if self.snake[0].x == self.food.x and self.snake[0].y == self.food.y:
            self.score += 1
            self.food = self.place_food()
            reward = 10
        else:
            self.snake.pop()
            reward = -1

        self.done = self.is_collision(self.snake[0])
        return reward, self.done, self.score

    def handle_input(self, action):
        if action[0] == 1 and self.direction != Direction.RIGHT:
            self.direction = Direction.LEFT
        elif action[1] == 1 and self.direction != Direction.LEFT:
            self.direction = Direction.RIGHT
        elif action[2] == 1 and self.direction != Direction.DOWN:
            self.direction = Direction.UP
        elif action[3] == 1 and self.direction != Direction.UP:
            self.direction = Direction.DOWN

    def move(self):
        head = self.snake[0]
        if self.direction == Direction.LEFT:
            new_head = Point(head.x - BLOCK_SIZE, head.y)
        elif self.direction == Direction.RIGHT:
            new_head = Point(head.x + BLOCK_SIZE, head.y)
        elif self.direction == Direction.UP:
            new_head = Point(head.x, head.y - BLOCK_SIZE)
        elif self.direction == Direction.DOWN:
            new_head = Point(head.x, head.y + BLOCK_SIZE)
        self.snake[0] = new_head

    def render(self):
        self.window.fill((0, 0, 0))
        for segment in self.snake:
            pygame.draw.rect(self.window, (0, 255, 0), pygame.Rect(segment.x, segment.y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(self.window, (255, 0, 0), pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.display.flip()
        self.clock.tick(10)  # Control the speed of the game

    def get_state(self):
        head = self.snake[0]
        point_l = Point(head.x - BLOCK_SIZE, head.y)
        point_r = Point(head.x + BLOCK_SIZE, head.y)
        point_u = Point(head.x, head.y - BLOCK_SIZE)
        point_d = Point(head.x, head.y + BLOCK_SIZE)

        dir_l = self.direction == Direction.LEFT
        dir_r = self.direction == Direction.RIGHT
        dir_u = self.direction == Direction.UP
        dir_d = self.direction == Direction.DOWN

        state = [
            (dir_r and self.is_collision(point_r)) or (dir_l and self.is_collision(point_l)) or
            (dir_u and self.is_collision(point_u)) or (dir_d and self.is_collision(point_d)),
            (dir_u and self.is_collision(point_r)) or (dir_d and self.is_collision(point_l)) or
            (dir_l and self.is_collision(point_u)) or (dir_r and self.is_collision(point_d)),
            (dir_d and self.is_collision(point_r)) or (dir_u and self.is_collision(point_l)) or
            (dir_r and self.is_collision(point_u)) or (dir_l and self.is_collision(point_d)),
            dir_l,
            dir_r,
            dir_u,
            dir_d,
            self.food.x < head.x,
            self.food.x > head.x,
            self.food.y < head.y,
            self.food.y > head.y
        ]

        return np.array(state, dtype=int)