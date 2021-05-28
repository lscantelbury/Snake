import pygame
import random
import time 

# Size of the window
window_width = 800
window_height = 600

# Colors
green = pygame.Color(16, 56, 6) # phthalo green
white = pygame.Color((255, 255, 255))
black = pygame.Color((0, 0, 0))

# Starting module
pygame.init()

# Creating window
window = pygame.display.set_mode((
                                window_width,
                                window_height
                                ))
pygame.display.set_caption("Snake")
fps = pygame.time.Clock(60)

snake_starting_point = [111, 62]
snake_body = [[111,62], # Each tuple is a segment
              [101, 62],# of the snake's body
              [91, 62],
              [81, 62]
              ]

# Variables for fruit's placement in the screen
fruit_coordinate = [random.randrange(1, (window_width // 10) * 10),
                    random.randrange(1, (window_height // 10) * 10)
                   ]
spawn = True

# Assigning variables for snake's orientation

