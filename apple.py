from random import randrange

class Apple:
    color = (255,0,0)
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
        coll_range = 20

        #getting a difference in range of a number makes the collision detection more forgiving-
        #the higher coll_range is, the further away you can reach apples, going too high will result in instability.
        if abs(snakeX - appleX) <= coll_range and abs(snakeY - appleY) <= coll_range:
            self.set_position([(randrange(0,1200),randrange(0,700))])
            snake.length += 1
            return True