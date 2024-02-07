from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.print_score()
        
    def print_score(self):
        self.goto(0, 290)
        self.write(arg = f"score: {self.score}", align = ALIGNMENT, font = FONT)
    
    def update_score(self):
        self.clear()
        self.score += 1
        self.print_score()
        
    def game_over(self):
        self.goto(0,0)
        self.write(arg = f"GAME OVER!\nFinal score: {self.score}", align = ALIGNMENT, font = FONT)
        
        