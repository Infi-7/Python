import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pd.read_csv("50_states.csv")
data["state"] = data['state'].str.lower()

count = 0
correct_guess = []

while count != len(data["state"]):
    answer_state = screen.textinput(title=f"{count}/{len(data["state"])} State Correct",
                                    prompt="What's another state's name?").lower()

    for x in range(len(data["state"])):
        if data["state"][x] == answer_state:
            correct_guess.append(answer_state)

            new_turtle = turtle.Turtle()
            new_turtle.penup()
            new_turtle.hideturtle()
            new_turtle.goto(data["x"][x], data["y"][x])
            new_turtle.write(f"{answer_state.title()}", False, "center", ("Arial", 6, "normal"))

            count += 1

        elif answer_state == "exit":
            missing_states = [x for x in data["state"] if x not in correct_guess]
            count = 50

            new_states = pd.DataFrame(missing_states)
            new_states.to_csv("states_to_learn.csv")

            break

