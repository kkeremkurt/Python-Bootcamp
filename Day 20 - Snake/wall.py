from turtle import Turtle
BORDER_START_X = -295
BORDER_START_Y = 290
DISTANCE = -1 * BORDER_START_X + BORDER_START_Y

class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.create_wall()
        
    def create_wall(self):
        self.penup()
        self.goto(BORDER_START_X, BORDER_START_Y)
        for _ in range(4):
            self.pendown()
            self.forward(DISTANCE)
            self.right(90)
    
    def wall_x(self):
        return (BORDER_START_X)
    
    def wall_y(self):
        return (BORDER_START_Y)
        
        