from turtle import Turtle
from random import randint
import time

class car_manager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(1, 1.5, 0)
        self.goto(randint(200,250),randint(-260,250))
        self.sped = 0.9
