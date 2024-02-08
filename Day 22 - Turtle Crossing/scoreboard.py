FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.level = 1
        self.write(arg = f"Level: {self.level}", align = "left", font = FONT)
        
    def update(self):
        self.clear()
        self.level +=1
        self.write(arg = f"Level: {self.level}", align = "left", font = FONT)
    
    def gameover(self):
        self.goto(0,0)
        self.write(arg = f"GAME OVER", align = "center", font = FONT)
        
    
