from turtle import Turtle
from random import choice, randint
import time
colors = ['red', 'green', 'cyan', 'blue', 'grey', 'brown', 'yellow']
class carManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        if randint(1,6) == 1:
            new_car = Turtle()
            new_car.color(choice(colors))
            new_car.shape('square')
            new_car.penup()
            new_car.shapesize(1,2,0)
            new_car.goto(300,randint(-250,250))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(10)