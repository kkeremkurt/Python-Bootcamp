from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")
FONT2 = ("Courier", 35, "normal")

class Scoreboard(Turtle):
    def __init__(self, player_side):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player_side = player_side
        self.score = 0
        self.print_score()
        
    def print_score(self):
        if self.player_side == "left":
            self.goto(-35, 180)
        elif self.player_side == "right":
            self.goto(35, 180)
        self.write(self.score, align = ALIGNMENT, font = FONT)
    
    def update_score(self):
        self.clear()
        self.score += 1
        self.print_score()
        
    def game_over(self, score1, score2):
        self.goto(0,0)
        if score1 > score2:
            self.write(arg = "Player LEFT wins!", align = ALIGNMENT, font = FONT2)
        else:
            self.write(arg = "Player RIGHT wins!", align = ALIGNMENT, font = FONT2)
        