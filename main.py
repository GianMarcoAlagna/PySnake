import pygame
from colors import *
from snake import *
from apple import *
from score_system import *

def main():
    #init required modules
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()

    #basic game setup
    run = True
    dis_size = (1280, 720)
    screen = pygame.display.set_mode(dis_size)
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    #var_size is the width and height
    snake_size = 20
    apple_size = 20
    
    #init class objects and sound effect
    snake = Snake(snake_size, dis_size)
    apple = Apple(apple_size)
    score = Score(pygame)
    munch = pygame.mixer.Sound(file="apple_munch.wav")

    #main loop starts here
    while run:
        clock.tick(20)
        screen.fill(DARKBLUE)
        score.display_score(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.quit()
                run = False
            #movement logic
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and snake.direction != Direction.DOWN:
                    snake.direction = Direction.UP
                elif event.key == pygame.K_a and snake.direction != Direction.RIGHT:
                    snake.direction = Direction.LEFT
                elif event.key == pygame.K_s and snake.direction != Direction.UP:
                    snake.direction = Direction.DOWN
                elif event.key == pygame.K_d and snake.direction != Direction.LEFT:
                    snake.direction = Direction.RIGHT
        #update snake with mov_snake then draw new snake with updated variables
        snake.mov_snake()
        snake.draw_snake(pygame,screen)
        snake.reset_snake()
        #check if snake collides with itself, if so, reset game
        if snake.check_self_coll():
            snake.define_snake()
            score.reset()
        #draw an apple and check if the snake collides with it
        apple.draw_apple(pygame,screen)
        if apple.check_collision(snake):
            pygame.mixer.Sound.play(munch)
            score.inc_score()
        #snake.debug()
        pygame.display.flip()

if __name__ == "__main__":
    main()