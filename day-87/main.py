from time import sleep
from turtle import *

game_on = True
win = Screen()

class Game:

    def __init__(self):
        self.score = 0
        self.lives = 3
        self.player_turtle = Turtle()

    def window_create(self) -> None:
        win.setup(510, 500)
        win.title("Mic test")
        win.bgcolor("black")
        win.tracer(0)

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
        self.player_turtle.color("white")
        self.player_turtle.shape("square")
        self.player_turtle.shapesize(stretch_len=5)
        self.player_turtle.penup()
        self.player_turtle.goto(0,-220)

    def move_left(self):
        x_pos = self.player_turtle.xcor()
        x_pos -= 20

        if x_pos < -200:
            self.player_turtle.setx(-200)
        else:
            self.player_turtle.setx(x_pos)

    def move_right(self):
        x_pos = self.player_turtle.xcor()
        x_pos += 20

        if x_pos > 200:
            self.player_turtle.setx(200)
        else:
            self.player_turtle.setx(x_pos)

    def run(self):
        self.player()
        while game_on:
            win.update()
            sleep(0.01)

start = Game()
start.window_create()
start.turtle_settings()

win.listen()
win.onkeypress(start.move_left,"Left")
win.onkeypress(start.move_right, "Right")

start.run()