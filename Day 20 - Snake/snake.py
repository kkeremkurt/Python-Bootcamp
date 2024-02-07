from turtle import Turtle, Screen
STARTING_POSITIONS = [(0, 0), (-0, 0), (-0, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
import time
screen = Screen()

class Snake():
    def __init__(self):
        self.snake_shape = "square"
        self.color = "white"
        self.speed ="fastest"
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
        
    def add_segment(self, position):
        new_segment = Turtle(shape = self.snake_shape)
        new_segment.color(self.color)
        new_segment.speed(self.speed)
        #new_segment.shapesize(0.5, 0.5)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
            
            
    def extend(self):
        self.add_segment(self.segments[-1].pos())
        
    
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        screen.update()
        time.sleep(0.01)
        
    def up(self):
        if self.head.heading() != DOWN and self.head.heading() != UP :
            self.head.setheading(UP)
            self.move()
            
    
    def down(self):
        if self.head.heading() != UP and self.head.heading() != DOWN:
            self.head.setheading(DOWN)
            self.move()
            
        
    def left(self):
        if self.head.heading() != RIGHT and self.head.heading() != LEFT:
            self.head.setheading(LEFT)
            self.move()
            
        
    def right(self):
        if self.head.heading() != LEFT and self.head.heading() != RIGHT:
            self.head.setheading(RIGHT)
            self.move()
            
    
        
        
        



