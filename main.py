import pygame
from colors import *
from snake import *
from apple import *
from score_system import *

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()

    run = True
    dis_size = (1280, 720)
    screen = pygame.display.set_mode(dis_size)
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    #var_size is the width and height
    snake_size = 20
    apple_size = 20
    
    
    snake = Snake(snake_size, dis_size)
    apple = Apple(apple_size)
    score = Score(pygame)
    munch = pygame.mixer.Sound(file="apple_munch.wav")

    while run:
        clock.tick(20)
        screen.fill(DARKBLUE)
        score.display_score(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.quit()
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
        apple.draw_apple(pygame,screen)
        if apple.check_collision(snake):
            pygame.mixer.Sound.play(munch)
            score.inc_score()
        #snake.debug()
        pygame.display.flip()

if __name__ == "__main__":
    main()