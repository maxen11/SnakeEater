import pygame
import sys
import random

# Init Pygame
pygame.init()

# Setup Display Stuff
WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

CLOCK = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define Snake and Food data structures
snake = [[100, 50], [90, 50], [80, 50]]
APPLE_POS = [random.randrange(1, WIDTH//10)*10, random.randrange(1, HEIGHT//10)*10]
direction = "RIGHT"
change_to = direction
score = 0

def game_over():
    pygame.quit()
    sys.exit()

def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (WIDTH//2, 15)
    SCREEN.blit(score_surface, score_rect)

# Main game loop
while True:
    SCREEN.fill((0, 0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        # keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Direction validation
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Update snake position
    if direction == 'UP':
        snake.insert(0, [snake[0][0], snake[0][1] - 10])
    if direction == 'DOWN':
        snake.insert(0, [snake[0][0], snake[0][1] + 10])
    if direction == 'LEFT':
        snake.insert(0, [snake[0][0] - 10, snake[0][1]])
    if direction == 'RIGHT':
        snake.insert(0, [snake[0][0] + 10, snake[0][1]])

    # Snake apple scenario
    if snake[0] == APPLE_POS:
        score += 1
        APPLE_POS = [random.randrange(1, WIDTH//10)*10, random.randrange(1, HEIGHT//10)*10]
    else:
        snake.pop()

    # Snake boundary collision scenario
    if snake[0][0] >= WIDTH or snake[0][0] < 0 or snake[0][1] >= HEIGHT or snake[0][1] < 0:
        game_over()

    # Snake self collision scenario
    for part in snake[1:]:
        if snake[0] == part:
            game_over()

    # Draw snake and apple
    for part in snake:
        pygame.draw.rect(SCREEN, GREEN, pygame.Rect(part[0], part[1], 10, 10))
    pygame.draw.rect(SCREEN, WHITE, pygame.Rect(APPLE_POS[0], APPLE_POS[1], 10, 10))

    # Show score
    show_score((255, 255, 255), 'arial', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame rate
    CLOCK.tick(30)
