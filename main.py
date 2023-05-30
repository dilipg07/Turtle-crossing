from turtle import Turtle, Screen
from carmanager import car_manager
from random import randint
import time
from player import Player
from scoreboard import scoreboard
screen = Screen()
screen.setup(600,600)
screen.title("Turtle crossing 🐢")
screen.tracer(0)
score = scoreboard()
game_on = True
new_player = Player()
screen.listen()
screen.onkey(new_player.move,'Up')
cars = []
while game_on:
    screen.update()
    time.sleep(0.9)
    car = car_manager()
    cars.append(car)
    for _ in cars:
        _.backward(10)
        if new_player.distance(_) < 20:
            game_on = False
    if new_player.ycor() == 250:
        score.update_score()
        
screen.exitonclick()