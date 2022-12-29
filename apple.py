from random import randrange

class Apple:
    color = (255,0,0)
    exists = False
    position = [(randrange(0,1200),randrange(0,700))]
    def __init__(self,size):
        self.apple_size = size


    def draw_apple(self,game,surface):
        game.draw.rect(surface,self.color,(self.position[0][0],self.position[0][1],self.apple_size,self.apple_size))

    def set_position(self,pos):
        self.position = pos

    def check_collision(self,snake):
        snakeX = snake.body[-1][0]
        snakeY = snake.body[-1][1]
        appleX = self.position[0][0]
        appleY = self.position[0][1]
        if abs(snakeX - appleX) <= 20 and abs(snakeY - appleY) <= 20:
            self.set_position([(randrange(0,1200),randrange(0,700))])