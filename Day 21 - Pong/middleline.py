from turtle import Turtle

class MiddleLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pensize(5)
        self.drawline()
    
    def drawline(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.setheading(270)
        for _ in range(25):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(13)