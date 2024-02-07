from snake import Snake
from turtle import Screen, Turtle
from food import Food
from scoreboard import Scoreboard
from wall import Wall
from controls import Controls
import time

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


screen = Screen()
screen.setup(width = 620, height = 640)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
wall = Wall()
controls = Controls()


game_is_on = True
while game_is_on:
    screen.listen()
    controls.activate(snake) 
    screen.update() 
    time.sleep(0.08)
    snake.move()
    
    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()
    
    #Detect collision with wall
    if snake.head.xcor() < wall.wall_x() or snake.head.xcor() > (-1 * wall.wall_x()):
        scoreboard.game_over()
        game_is_on = False
        controls.deactivate()
    elif snake.head.ycor() > wall.wall_y() or snake.head.ycor() < (-1 * wall.wall_y()):
        scoreboard.game_over()
        game_is_on = False
        controls.deactivate()
    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            controls.deactivate()
            scoreboard.game_over()
   
    
    
    

    
    
        
        
        

    









screen.exitonclick()
