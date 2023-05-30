from turtle import Turtle, Screen
from carmanager import car_manager
from random import randint
import time

screen = Screen()
screen.setup(600,600)
screen.title("Turtle crossing 🐢")
screen.tracer(0)
game_on = True

cars = []
while game_on:
    screen.update()
    for x in range(1):
        car = car_manager()
        cars.append(car)
    for _ in cars:
        _.backward(20)
screen.exitonclick()