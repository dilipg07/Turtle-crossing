from turtle import Turtle
import time
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(0,-280)
        self.seth(90)

    def move(self):
        self.forward(10)