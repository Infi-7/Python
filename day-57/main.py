from flask import *
import random
import datetime


app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now()
    return render_template("index.html", num = random_number, year= current_year.strftime("%Y"))


if __name__ == "__main__":
    app.run(debug=True)