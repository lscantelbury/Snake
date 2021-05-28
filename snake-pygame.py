import pygame
import random
import time

# Size of the window
window_width = 720
window_height = 480

# Colors
green = pygame.Color(16, 56, 6)  # phthalo green
white = pygame.Color((255, 255, 255))
black = pygame.Color((0, 0, 0))

# Starting module
pygame.init()

# Creating window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake")
fps = pygame.time.Clock()

snake_starting_point = [100, 50]
snake_body = [[100, 50],  # Each tuple is a segment
              [90, 50],  # of the snake's body
              [80, 50],
              [70, 50]
              ]
snake_speed = 5

# Variables for fruit's placement in the screen
fruit_coordinate = [
    random.randrange(1, (window_width // 10) * 10),
    random.randrange(1, (window_height // 10) * 10)
]
spawn = True

# Assigning variables for snake's orientation

direction = 'RIGHT'
change_to = direction


score = 0

# Function for displaying score on the screen


def score_displaying(choice, color, font, size):
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, white)
    window.blit(text, (20, 10))


# Function for displaying game over message on the screen
def game_over():
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, white)
    window.blit(text, (20, 10))

    # Wait 2 seconds, quit pygame, then quit code
    time.sleep(2)
    pygame.quit()
    quit()


# Main Function
while True:

    # Keyboard commands
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # If two keys pressed simultaneously
    # we don't want snake to move into two directions
    # simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Snake's vectors
    if direction == 'UP':
        snake_starting_point[1] -= 10
    if direction == 'DOWN':
        snake_starting_point[1] += 10
    if direction == 'LEFT':
        snake_starting_point[0] -= 10
    if direction == 'RIGHT':
        snake_starting_point[0] += 10

    # Snake body growing mechanism
    # if fruits and snakes collide then scores will be
    # incremented by 10
    snake_body.insert(0, list(snake_starting_point))
    if snake_starting_point[0] == fruit_coordinate[0] and snake_starting_point[1] == fruit_coordinate[1] :
        score += 10
        spawn = False
    else:
        snake_body.pop()

    if not spawn:
        fruit_coordinate = [random.randrange(1, (window_width//10)) * 10,
                            random.randrange(1, (window_height//10)) * 10]

    spawn = True
    window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(window, green, pygame.Rect(
            pos[0], pos[1], 10, 10))

    pygame.draw.rect(window, white, pygame.Rect(
        fruit_coordinate[0], fruit_coordinate[1], 10, 10))

    # Game Over conditions
    if snake_starting_point[0] < 0 or snake_starting_point[0] > window_width-10:
        game_over()
    if snake_starting_point[1] < 0 or snake_starting_point[1] > window_height-10:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_starting_point[0] == block[0] and snake_starting_point[1] == block[1]:
            game_over()

    # displaying score countinuously
    score_displaying(1, white, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refres Rate
    fps.tick(snake_speed)


pygame.quit()
