from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle") 
        self.penup()
        self.direction_x = random.choice([-0.3, 0.3])
        self.direction_y = random.choice([-0.3, 0.3])
        
    
    def move(self):
        new_x = self.xcor() + self.direction_x
        new_y = self.ycor() + self.direction_y
        self.goto(new_x, new_y)
    
    def bounce(self):
        self.direction_y *= -1
        
    def paddle_bounce(self):
        self.direction_x *= -1
        self.direction_x *= 1.2
        self.direction_y *= 1.2
    
    
    def reset_position(self):
        #Reset the position of the ball and shot it towards the other side(other x direction)
        self.goto(0,0)
        self.direction_y = random.choice([-0.3, 0.3])
        self.direction_x = random.choice([-0.3, 0.3])
        
        
        
             
    