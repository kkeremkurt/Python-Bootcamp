from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
screen.bgpic("background.GIF")

user_bet = screen.textinput(title = "Make your bet", prompt = "Place your bet, who is going to win? Enter a color:  ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-150, -110, -70, -30, 10, 50]
all_turtles = []

#Drawing the finish line
finish_line = Turtle()
finish_line.hideturtle()
finish_line.pensize(10)
finish_line.speed("fastest")
finish_line.penup()
finish_line.goto(220, 90)
finish_line.right(90)
finish_line.pendown()
finish_line.forward(260)



for turtle_index in range(0,6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230,y_positions[turtle_index])
    all_turtles.append(new_turtle)
    
    

if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

        if turtle.xcor() > 200:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost. The {winning_color} turtle is the winner.")
    
    


screen.exitonclick()