import random
from flask import Flask

random_number  = random.randint(0,9)


app = Flask(__name__)

@app.route("/")
def home():
    return ("<b>Guess the right number between 0 to 9 and write it in the url after '/'.</br>"
            " E.g if your guess is 1 enter '/1' in url after current url.</b></br>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif', width=200>")

@app.route("/<int:number>")
def user_input(number):
    if number == random_number:
        return "<h1 style='color:green'>You found me!</h1></br><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif', width=200>"
    elif number < random_number:
        return "<h1 style='color:red'>Too low, try again!</h1></br><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif', width=200>"
    elif number > random_number:
        return "<h1 style='color:purple'>Too high, try again!</h1></br><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif', width=200>"


if __name__ == "__main__":
    app.run(debug=True)