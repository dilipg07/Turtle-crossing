from turtle import Turtle, Screen
from player import Player
from carmanager import carManager
import time

screen = Screen()
screen.title("Turtle running Game 🐢🐢")
screen.setup(600,600)
screen.tracer(0)
new_player = Player()
screen.listen()
screen.onkey(new_player.move,"Up")
cars = carManager()

game_on =True
while game_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_car()

screen.exitonclick()