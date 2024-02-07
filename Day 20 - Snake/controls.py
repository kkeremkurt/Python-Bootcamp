from turtle import Turtle, Screen
class Controls(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
    
    def activate(self, object_name):
        self.screen.onkeypress(object_name.up, "w")
        self.screen.onkeypress(object_name.down, "s")
        self.screen.onkeypress(object_name.left, "a")
        self.screen.onkeypress(object_name.right, "d") 
    
    def deactivate(self):
        self.screen.onkeypress(None, "w")
        self.screen.onkeypress(None, "s")
        self.screen.onkeypress(None, "a")
        self.screen.onkeypress(None, "d") 