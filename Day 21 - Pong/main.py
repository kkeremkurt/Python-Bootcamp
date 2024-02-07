from turtle import Turtle, Screen
from middleline import MiddleLine
from paddle import Paddle
from ball import Ball
from controls import Controls
from scoreboard import Scoreboard
import time
TOP_Y = 280
BOT_Y = -280


#Screen Setup
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong Game!")
screen.tracer(0)

#Draw the middle line
middleline = MiddleLine()

#Create the paddles
paddle_left = Paddle("left")
paddle_right = Paddle("right")

#Create the ball
ball = Ball()

#Create the scoreboard
score_left = Scoreboard("left")
score_right = Scoreboard("right")

controls = Controls()
screen.listen()
controls.activate(paddle_left, paddle_right)


def game():
    is_game_on = True
    while is_game_on:
        ball.move()
        screen.update()
        
        #Detect collision with the wall
        if ball.ycor() > TOP_Y or ball.ycor() < -TOP_Y:
            ball.bounce()
        
        ######################RIGHT PADDLE######################
        #Detect collision with right paddle
        right_collision = ball.xcor() > 330 and ball.xcor() < 335 and ball.distance(paddle_right) < 65
        if right_collision:
            ball.paddle_bounce()
            print("Right paddle")
            print(f"xcor: {ball.xcor()}, ycor: {ball.ycor()}")
            
        #Ball bounce from the top of right paddle    
        elif ball.xcor() > 335 and ball.distance(paddle_right) < 70:
            ball.bounce()
        ######################RIGHT PADDLE######################
        
        
        ######################LEFT PADDLE######################
        left_collision =ball.xcor() < -330 and ball.xcor() > -335 and ball.distance(paddle_left) < 65
        if left_collision:
            ball.paddle_bounce()
            print("Left paddle")
            print(f"xcor: {ball.xcor()}, ycor: {ball.ycor()}")
            
        #Ball bounce from the top of left paddle    
        elif ball.xcor() < -335 and ball.distance(paddle_right) < 70:
            ball.bounce()
        ######################LEFT PADDLE######################
        
        
        #Detect if ball is out of bounds
        if ball.xcor() > 401:
            score_left.update_score()
            ball.reset_position()
            if score_left.score >=5 or score_right.score >= 5:
                is_game_on = False
                score_left.game_over(score1= score_left.score, score2=score_right.score)
        elif ball.xcor() < -401:
            score_right.update_score()
            ball.reset_position()
            if score_left.score >=5 or score_right.score >= 5:
                is_game_on = False
                score_right.game_over(score1=score_left.score, score2=score_right.score)
    
game()
    











screen.exitonclick()