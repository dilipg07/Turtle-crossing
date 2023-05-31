from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(-200,265)
        self.update_score()
        

    def update_score(self):
        self.write(f"Level: {self.score}",align = 'center', font = ('courier',20, 'normal'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.hideturtle()
        self.goto(0,0)
        self.write(f"Game Over!", align = "center", font = ('ariel', 30, 'bold'))