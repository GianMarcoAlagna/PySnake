import pygame
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
        self.spawn_snake()
    
    def spawn_snake(self):
        #How many blocks of snake to spawn 
        self.length = 10
        #Each tuple in body array is one individual block of the snake
        #index[0] being the back end of the snake.
        self.body = [(20,20),(20,40),(20,60)]
        self.direction = Direction.DOWN
    
    def draw_snake(self,game,surface):
        #loop through body array
        for part in self.body:
            #at each index is array, draw a rectangle
            #x axis = first item in current array index(part[0])
            #y axis = second item in current array index(part[1])
            game.draw.rect(surface,self.color,(part[0],part[1],self.snake_size,self.snake_size))
    
    def mov_snake(self):
            head = self.body[-1]
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

            if self.length < len(self.body):
                self.body.pop(0)

    def debug(self):
        head = self.body[-1]
        print("X-Coordinate:{0}\n Y-Coordinate{1}".format(head[0],head[1]))

    def reset_snake(self):
        for body_part in self.body:
            if body_part[0] >= 1280:
                self.body.append((0,body_part[1]))
                self.body.pop()
                