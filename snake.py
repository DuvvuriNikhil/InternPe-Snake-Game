import pygame
import time
import random

# Initialize pygame
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red   = (213, 50, 80)
green = (0, 255, 0)
blue  = (50, 153, 213)

# Screen size
width = 600
height = 400

# Create display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("🐍 Snake Game")

# Clock
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 20)

# Score display
def Your_score(score):
    value = score_font.render(f"Score: {score}", True, white)
    screen.blit(value, [0, 0])

# Draw snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

# Display message
def message(msg, color, y_offset=0):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3 + y_offset])

# Game loop
def gameLoop():
    game_over = False
    game_close = False
    show_thanks = False  # flag to show "Thanks for playing"

    x = width / 2
    y = height / 2
    dx = 0
    dy = 0

    snake_List = []
    length = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(black)
            message("Game Over! Press Q-Quit or C-Play Again", red)
            Your_score(length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                    show_thanks = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                        show_thanks = True
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                show_thanks = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -snake_block
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = snake_block
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -snake_block
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = snake_block
                    dx = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += dx
        y += dy
        screen.fill(blue)
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

        snake_Head = [x, y]
        snake_List.append(snake_Head)
        if len(snake_List) > length:
            del snake_List[0]

        for block in snake_List[:-1]:
            if block == snake_Head:
                game_close = True

        draw_snake(snake_block, snake_List)
        Your_score(length - 1)

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length += 1

        clock.tick(snake_speed)

    # Show "Thanks for playing" message only on quit
    if show_thanks:
        screen.fill(black)
        message("Thanks for playing!", white)
        pygame.display.update()
        time.sleep(2)

    pygame.quit()
    quit()

gameLoop()
