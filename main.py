import pygame
from colors import *
from snake import *
from apple import *

def main():
    pygame.init()
    run = True
    dis_size = (1280, 720)
    #snake_size is the width and height
    snake_size = 20
    apple_size = 20
    screen = pygame.display.set_mode(dis_size)
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    snake = Snake(snake_size, dis_size)
    apple = Apple(apple_size)

    while run:
        clock.tick(20)
        screen.fill(DARKBLUE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    snake.direction = Direction.UP
                if event.key == pygame.K_a:
                    snake.direction = Direction.LEFT
                if event.key == pygame.K_s:
                    snake.direction = Direction.DOWN
                if event.key == pygame.K_d:
                    snake.direction = Direction.RIGHT
        snake.mov_snake()
        snake.draw_snake(pygame,screen)
        snake.reset_snake()
        snake.debug()
        apple.draw_apple(pygame,screen)
        apple.check_collision(snake)
        pygame.display.flip()

if __name__ == "__main__":
    main()