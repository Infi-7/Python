from time import sleep
from turtle import *

game_on = True

class Game:
    def __init__(self):
        self.score = 0
        self.lives = 3

    def window_create(self) -> None:
        win = Screen()
        win.setup(510, 500)
        win.title("Mic test")
        win.bgcolor("black")

    def turtle_settings(self):
        tur = Turtle()
        tur.color("white")
        tur.hideturtle()
        tur.pensize(10)
        tur.penup()
        tur.goto(-240,240)
        tur.pendown()

        lines = 9
        x_pos = -240

        for _ in range(4):
            for _ in range(lines):
                tur.forward(40)
                tur.penup()
                tur.forward(15)
                tur.pendown()

            tur.penup()
            tur.goto(x_pos,tur.ycor() - 20)
            tur.pendown()


    def player(self):
        player_turtle = Turtle()
        player_turtle.color("white")
        player_turtle.shape("square")
        player_turtle.shapesize(stretch_len=5)
        player_turtle.penup()
        player_turtle.goto(0,-220)

start = Game()
start.window_create()
start.turtle_settings()


while game_on:

    start.player()
    sleep(60)
    game_on = False
