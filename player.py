from turtle import Turtle
START_POSITION = (0,-280)
STEP = 10
DEFAULT_DIRECTION = 90
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.seth(DEFAULT_DIRECTION)
        self.goto(START_POSITION)

    def move(self):
        self.forward(STEP)