from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.goto(-200,270)
        self.write(f"Level: {self.score}", align = 'center',font =  ('courier', 15, 'normal'))