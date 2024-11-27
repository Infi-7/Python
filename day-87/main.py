import random
import time
from turtle import *

PADDLE_SPEED = 20
BALL_SPEED = 2
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Paddle:
    def __init__(self):
        self.paddle = Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=1, stretch_len=5)
        self.paddle.penup()
        self.paddle.goto(0, -250)

    def move_left(self):
        x = self.paddle.xcor() - PADDLE_SPEED

        if x < -SCREEN_WIDTH // 2 + 50:
            x = -SCREEN_WIDTH // 2 + 50
        self.paddle.setx(x)

    def move_right(self):
        x = self.paddle.xcor() + PADDLE_SPEED

        if x > SCREEN_WIDTH // 2 - 50:
            x = SCREEN_WIDTH // 2 - 50
        self.paddle.setx(x)

class Ball:
    def __init__(self):
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.color("yellow")
        self.ball.speed(0)
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = BALL_SPEED * random.choice([-1, 1])
        self.ball.dy = BALL_SPEED

    def move(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

    def bounce_x(self):
        self.ball.dx *= -1

    def bounce_y(self):
        self.ball.dy *= -1

    def reset_pos(self):
        self.ball.goto(0, 0)
        self.ball.dx = BALL_SPEED * random.choice([-1, 1])
        self.ball.dy = BALL_SPEED

class BrickManager:
    def __init__(self):
        self.bricks = []
        self.create_bricks()

    def create_bricks(self):
        colors = ["red", "orange", "green", "blue"]
        rows = 4
        columns = 10
        brick_width = 60
        brick_height = 20
        spacing = 10
        total_width = (brick_width * columns) + (spacing * (columns - 1))

        x_start = -total_width // 2 + brick_width // 2
        y_start = 200

        for row in range(rows):
            for column in range(columns):
                brick = Turtle()
                brick.speed(0)
                brick.shape("square")
                brick.color(colors[row % len(colors)])
                brick.shapesize(stretch_wid=1, stretch_len=3)
                brick.penup()
                x_pos = x_start + column * (brick_width + spacing)
                y_pos = y_start - row * (brick_height + spacing)
                brick.goto(x_pos, y_pos)
                self.bricks.append(brick)


class BreakoutGame:
    def __init__(self):
        self.win = Screen()
        self.win.title("Breakout Game")
        self.win.bgcolor("black")
        self.win.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.win.tracer(0)

        self.paddle = Paddle()
        self.ball = Ball()
        self.brick_manager = BrickManager()

        self.score = 0
        self.lives = 3

        self.score_display = Turtle()
        self.score_display.speed(0)
        self.score_display.color("white")
        self.score_display.penup()
        self.score_display.hideturtle()
        self.score_display.goto(-350, 260)
        self.update_score()

        self.win.listen()
        self.win.onkeypress(self.paddle.move_left, "Left")
        self.win.onkeypress(self.paddle.move_right, "Right")

    def update_score(self):
        self.score_display.clear()
        self.score_display.write(f"Score: {self.score} Lives: {self.lives}", font=("Arial", 16, "normal"))

    def check_collisions(self):
        if self.ball.ball.xcor() > SCREEN_WIDTH // 2 - 10:
            self.ball.ball.setx(SCREEN_WIDTH // 2 - 10)
            self.ball.bounce_x()

        if self.ball.ball.xcor() < -SCREEN_WIDTH // 2 + 10:
            self.ball.ball.setx(-SCREEN_WIDTH // 2 + 10)
            self.ball.bounce_x()

        if self.ball.ball.ycor() > SCREEN_HEIGHT // 2 - 10:
            self.ball.ball.sety(SCREEN_HEIGHT // 2 - 10)
            self.ball.bounce_y()

        if (self.ball.ball.ycor() > -240 and self.ball.ball.ycor() < -230) and (self.paddle.paddle.xcor() - 50 < self.ball.ball.xcor() < self.paddle.paddle.xcor() + 50):
            self.ball.bounce_y()

        for brick in self.brick_manager.bricks:
            if brick.isvisible() and (brick.ycor() - 10 < self.ball.ball.ycor() < brick.ycor() + 10) and (brick.xcor() - 30 < self.ball.ball.xcor() < brick.xcor() + 30):
                self.ball.bounce_y()
                brick.hideturtle()
                self.brick_manager.bricks.remove(brick)
                self.score += 10
                self.update_score()
                break

    def play(self):
        while self.lives > 0:
            self.win.update()
            self.ball.move()
            self.check_collisions()

            if self.ball.ball.ycor() < -SCREEN_HEIGHT // 2:
                self.lives -= 1
                self.update_score()
                self.ball.reset_pos()
                time.sleep(1)

            if not self.brick_manager.bricks:
                self.score_display.clear()
                self.score_display.write("You Win", align="center", font=("Arial",24,"bold"))
                time.sleep(3)
                self.win.bye()
            time.sleep(0.01)

if __name__ == "__main__":
    game = BreakoutGame()
    game.play()
