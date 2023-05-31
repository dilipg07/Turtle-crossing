from turtle import Turtle, Screen
from player import Player

screen = Screen()
screen.title("Turtle running Game 🐢🐢")
screen.setup(600,600)
screen.tracer(0)
new_player = Player()
screen.listen()
screen.onkey(new_player.move,"Up")


game_on =True
while game_on:
    screen.update()

screen.exitonclick()