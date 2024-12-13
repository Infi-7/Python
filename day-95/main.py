import turtle
import random
import math

# Screen setup
screen = turtle.Screen()
screen.title("Space Invaders")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Player setup
player = turtle.Turtle()
player.shape("triangle")
player.color("white")
player.penup()
player.goto(0, -250)
player.setheading(90)
player_speed = 15

# Enemy setup
enemies = []
num_of_enemies = 6
for _ in range(num_of_enemies):
    enemy = turtle.Turtle()
    enemy.shape("circle")
    enemy.color("red")
    enemy.penup()
    enemy.goto(random.randint(-300, 300), random.randint(100, 250))
    enemies.append(enemy)
enemy_speed = 0.1

# Bullet setup
bullet = turtle.Turtle()
bullet.shape("square")
bullet.color("yellow")
bullet.penup()
bullet.shapesize(stretch_wid=0.5, stretch_len=1)
bullet.goto(0, -400)  # Off-screen initially
bullet_speed = 5
bullet_state = "ready"  # "ready" or "fire"

# Score setup
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.color("white")
score_display.penup()
score_display.goto(-350, 260)
score_display.write(f"Score: {score}", align="left", font=("Arial", 16, "normal"))

# Functions

def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -380:
        x = -380
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 380:
        x = 380
    player.setx(x)

def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        bullet.goto(player.xcor(), player.ycor() + 10)
        bullet.showturtle()

def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    return distance < 20

# Key bindings
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(fire_bullet, "space")

# Main game loop
running = True
while running:
    screen.update()

    # Enemy movement
    for enemy in enemies:
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        # Reverse enemy direction and move down
        if enemy.xcor() > 380 or enemy.xcor() < -380:
            enemy_speed *= -1
            for e in enemies:
                y = e.ycor()
                y -= 20
                e.sety(y)

        # Check for collision with bullet
        if is_collision(bullet, enemy):
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.goto(0, -400)
            enemy.goto(random.randint(-300, 300), random.randint(100, 250))
            score += 1
            score_display.clear()
            score_display.write(f"Score: {score}", align="left", font=("Arial", 16, "normal"))

        # Check for game over
        if enemy.ycor() < -250:
            running = False
            score_display.goto(0, 0)
            score_display.write("GAME OVER", align="center", font=("Arial", 24, "bold"))

    # Bullet movement
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # Reset bullet if it goes off screen
    if bullet.ycor() > 280:
        bullet.hideturtle()
        bullet_state = "ready"

# Close the window when the game ends
screen.mainloop()
