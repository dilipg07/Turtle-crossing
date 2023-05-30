from turtle import Turtle
from random import randint
import time

class car_manager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(1, 2, 0)
        self.goto(300,randint(-260,260))
        time.sleep(0.9)
