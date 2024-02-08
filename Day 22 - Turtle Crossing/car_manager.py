COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_Y = list(range(-250, 250))

from turtle import Turtle
import random

class CarManager(Turtle):
    def __init__(self, car_speed):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=2)
        self.starting_x = 300
        self.starting_y = random.choice(STARTING_Y)
        self.speed = car_speed
        self.goto(300, self.starting_y)
        
        
    def move(self):
        self.starting_x -= self.speed
        self.goto(self.starting_x, self.starting_y)
    
    
        
    
