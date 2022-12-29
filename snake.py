from enum import Enum

class Direction(Enum):
  UP = 0
  DOWN = 1
  LEFT = 2
  RIGHT = 3

class Snake:
    color = (0,255,0)
    def __init__(self,snake_size,dis_size):
        self.snake_size = snake_size
        self.dis_size = dis_size
        self.define_snake()
    
    def define_snake(self):
        #How many blocks of snake to spawn 
        self.length = 10
        #Each tuple in body array is one individual block of the snake
        #index[0] being the back end of the snake.
        #the numbers 20,40,60 etc. are the x and y values of that block
        self.body = [(20,20),(20,40),(20,60)]
        self.direction = Direction.DOWN
    
    def draw_snake(self,game,surface):
        #loop through body array
        for indx, part in enumerate(self.body):
            #at each index is array, draw a rectangle
            #x axis = first item in current array index(part[0])
            #y axis = second item in current array index(part[1])
            if indx + 1 == self.length:
                game.draw.rect(surface,(0,0,0),(part[0],part[1],self.snake_size,self.snake_size))
            else:
                game.draw.rect(surface,self.color,(part[0],part[1],self.snake_size,self.snake_size))
            

    
    def mov_snake(self):
            #head variable is equal to the end tuple of body array aka the head of the snake
            head = self.body[-1]
            #checks snakes direction and compares it to the directions in the seperate Directions class.
            #if the direcion is down for instance, we create the next head,
            #x-coord(head[0]) stays the same, then we set the second item to current value plus the snake size. 
            if self.direction == Direction.DOWN:
                next_head = (head[0], head[1] + self.snake_size)
                self.body.append(next_head)
            elif self.direction == Direction.UP:
                next_head = (head[0], head[1] - self.snake_size)
                self.body.append(next_head)
            elif self.direction == Direction.RIGHT:
                next_head = (head[0] + self.snake_size, head[1])
                self.body.append(next_head)
            elif self.direction == Direction.LEFT:
                next_head = (head[0] - self.snake_size, head[1])
                self.body.append(next_head)

            #after all conditions are checked, we pop the first element in the array-
            #whenever more than self.length(10), blocks have been appended.
            #the higher self.length is, the more blocks that are allowed to be appended, making it longer.
            if self.length < len(self.body):
                self.body.pop(0)

    #prints debug information
    def debug(self):
        head = self.body[-1]
        print("X-Coordinate:{0}\n Y-Coordinate{1}".format(head[0],head[1]))
    
    #whenever this function is called, it will check if the x or y coordinate of the head are-
    #greater than the resolution or less than 0, if any of the statements return true, we will-
    #append a new block on the opposite side accordingly.
    def reset_snake(self):
        for body_part in self.body:
            if body_part[0] > 1280:
                self.body.append((1,body_part[1]))
                self.body.pop(0)
            elif body_part[0] < 0:
                self.body.append((1279,body_part[1]))
                self.body.pop(0)
            elif body_part[1] > 720:
                self.body.append((body_part[0],1))
                self.body.pop(0)
            elif body_part[1] < 0:
                self.body.append((body_part[0],719))
                self.body.pop(0)

    #this is another debug function
    # def add_block(self):
    #     self.body.append((self.body[-1][0],self.body[-1][1]))
    #     print("Block added")
                