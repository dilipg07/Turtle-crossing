from turtle import Turtle, Screen
from player import Player
from carmanager import carManager
import time
from scorecard import scoreboard

screen = Screen()
screen.title("Turtle running Game 🐢🐢")
screen.setup(600,600)
screen.tracer(0)
new_player = Player()
score = scoreboard()
screen.listen()
screen.onkey(new_player.move,"Up")
cars = carManager()
x = 0.1
game_on =True
while game_on:
    time.sleep(x)
    screen.update()
    cars.create_car()
    cars.move_car()

    # #Detect collision with car
    for car in cars.all_cars:
        if car.distance(new_player) < 20:
            score.game_over()
            game_on = False
    
    if new_player.ycor() == 250:
        score.increase_score()
        new_player.start_line()
        x *= 0.8
        print(x)
screen.exitonclick()