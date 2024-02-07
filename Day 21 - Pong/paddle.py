from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, player_side):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.player_side = player_side
        self.create_paddle()
        
    def create_paddle(self):
        self.setheading(90)
        self.shapesize(stretch_wid = 1, stretch_len = 5)
        self.penup()
        if self.player_side == "left":
            self.goto(-350, 0)
        elif self.player_side == "right":
            self.goto(350, 0)
    
    def up(self):
        self.setheading(90)
        #Limiting the screen borders
        if self.ycor() <250:
            self.forward(20)
        
    def down(self):
        self.setheading(270)
        #Limiting the screen borders
        if self.ycor() > -230:
            self.forward(20)
        
        