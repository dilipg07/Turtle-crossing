from turtle import Turtle
STEP = 10
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.seth(90)
        self.goto(0,-280)

    def move(self):
        self.forward(STEP)
