from turtle import Turtle, Screen
class Controls(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.screen = Screen()
    
    def activate(self, player1, player2):
        self.screen.onkeypress(player1.up, "w")
        self.screen.onkeypress(player1.down, "s")
        
        self.screen.onkeypress(player2.up, "Up")
        self.screen.onkeypress(player2.down, "Down")
    
    def deactivate(self):
        self.screen.onkeypress(None, "w")
        self.screen.onkeypress(None, "s")
        self.screen.onkeypress(None, "Up")
        self.screen.onkeypress(None, "Down")