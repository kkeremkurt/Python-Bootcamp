import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = []
scoreboard = Scoreboard()

game_counter = 0
dice = random.randint(1,6)

screen.listen()
screen.onkeypress(player.move, "w")

car_speed = 5

game_is_on = True
while game_is_on:
    game_counter += 1
    time.sleep(0.1)
    screen.update()
    
    if game_counter % 6 == 0:
        new_car = CarManager(car_speed)
        cars.append(new_car)
    
    #Detect collision with a car
    for car in cars:
        car.move()
        if player.ycor() > car.ycor() and player.distance(car) < 20:
            game_is_on = False
            scoreboard.gameover()
            
            print("Tail crash!")
        elif player.ycor() < car.ycor() and player.distance(car) < 25:
            game_is_on = False
            scoreboard.gameover()
            
            print("Head crash!")
        
        
    #Check if the player passes the level
    if player.ycor() > 300:
        scoreboard.update()
        player.reset()
        car_speed +=5
            

screen.exitonclick()   
    
    
