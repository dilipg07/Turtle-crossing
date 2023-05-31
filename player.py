from turtle import Turtle
START_POSITION = (0,-280)
STEP = 10
DEFAULT_DIRECTION = 90
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.start_line()
        self.seth(DEFAULT_DIRECTION)
        

    def move(self):
        self.forward(STEP)

    def start_line(self):
        self.goto(START_POSITION)